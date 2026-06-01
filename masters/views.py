from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count, Avg, Q
from django.utils import timezone

from .models import Master, StudentEnrollment, Attendance, StudentPayment, Certificate
from .forms import MasterForm
from practice.models import PracticeAttempt
from homework.models import PandaGroup, Homework
from tutorial.models import Tutorial


@login_required
def master_list(request):
    masters = Master.objects.all().annotate(
        practice_count=Count('practices', distinct=True),
        student_count_live=Count('pandas', distinct=True),
    ).order_by('-created_at')
    return render(request, 'masters/master_list.html', {'masters': masters})


@login_required
def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    is_owner = (request.user == master.profile.user)

    practice_qs = master.practices if is_owner else master.practices.filter(is_published=True)
    practices = practice_qs.annotate(
        question_count=Count('questions', distinct=True),
        attempt_count=Count('attempts', distinct=True),
        avg_score=Avg('attempts__score'),
    )

    attempts_qs = PracticeAttempt.objects.filter(practice__master=master)
    avg_student_score = attempts_qs.aggregate(avg=Avg('score'))['avg'] or 0
    total_attempts = attempts_qs.count()
    total_questions = sum(p.question_count for p in practices)

    days_active = (timezone.now() - master.created_at).days
    experience_years = days_active // 365
    experience_months = (days_active % 365) // 30

    student_count = master.pandas.count()
    students = master.pandas.select_related('profile__user').order_by('-rating')

    groups = []
    homeworks = []
    if is_owner:
        groups = master.panda_groups.annotate(
            member_count_ann=Count('members')
        ).order_by('name')
        homeworks = (
            master.homeworks
            .select_related('practice')
            .prefetch_related('assignments')
            .order_by('-created_at')
        )

    tutorials = (
        Tutorial.objects
        .filter(author=master.profile.user, is_published=True)
        .order_by('-created_at')
    )

    return render(request, 'masters/master_detail.html', {
        'master': master,
        'is_owner': is_owner,
        'practices': practices,
        'avg_student_score': avg_student_score,
        'total_attempts': total_attempts,
        'total_questions': total_questions,
        'experience_years': experience_years,
        'experience_months': experience_months,
        'student_count': student_count,
        'students': students,
        'groups': groups,
        'homeworks': homeworks,
        'tutorials': tutorials,
    })


@login_required
def master_create(request):
    if hasattr(request.user.profile, 'master'):
        messages.info(request, "You already have a Master profile.")
        return redirect('masters-home')

    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            master = form.save(commit=False)
            master.profile = request.user.profile
            master.save()
            messages.success(request, "Your Master application has been submitted. You'll gain full access once an admin approves it.")
            return redirect('masters-home')
    else:
        form = MasterForm()
    return render(request, 'masters/master_form.html', {'form': form})


@login_required
def master_update(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('masters-detail', master_id=master.pk)
    else:
        form = MasterForm(instance=master)
    return render(request, 'masters/master_form.html', {'form': form, 'master': master})


@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        master.delete()
        messages.success(request, "Master profile deleted.")
        return redirect('masters-home')
    return render(request, 'masters/master_confirm_delete.html', {'master': master})


@login_required
def master_remove_student(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk)
    if request.method == 'POST':
        master.pandas.remove(panda)
        StudentEnrollment.objects.filter(master=master, panda=panda).delete()
        master.update_stats()
        messages.success(request, f'Removed {panda.profile.user.username} from your students.')
    return redirect('masters-my-students', pk=master.pk)


@login_required
def certificate_generator(request):
    is_master = hasattr(request.user, 'profile') and hasattr(request.user.profile, 'master')
    if not request.user.is_staff and not (is_master and request.user.profile.master.is_approved):
        raise PermissionDenied

    master = None
    students = []
    if is_master:
        master = request.user.profile.master
        students = (
            master.pandas
            .select_related('profile__user')
            .order_by('profile__user__first_name', 'profile__user__username')
        )

    return render(request, 'masters/certificate.html', {
        'master':   master,
        'students': students,
        'today':    timezone.now().date(),
    })


@login_required
def my_students(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    students = (
        master.pandas
        .select_related('profile__user')
        .annotate(
            attempt_count=Count('attempts', filter=Q(attempts__status='completed'), distinct=True),
            avg_score=Avg('attempts__score', filter=Q(attempts__status='completed')),
        )
        .order_by('-rating')
    )

    # Attach enrollment and payment data to each student
    enrollment_map = {
        e.panda_id: e for e in
        StudentEnrollment.objects.filter(master=master).select_related('panda')
    }
    last_payment_map = {}
    for p in students:
        last_pay = StudentPayment.objects.filter(master=master, panda=p).order_by('-created_at').first()
        last_payment_map[p.pk] = last_pay

    student_rows = []
    for s in students:
        enrollment = enrollment_map.get(s.pk)
        last_pay = last_payment_map.get(s.pk)
        attendance_summary = Attendance.objects.filter(master=master, panda=s)
        total_att = attendance_summary.count()
        present_att = attendance_summary.filter(status=Attendance.PRESENT).count()
        student_rows.append({
            'panda': s,
            'enrollment': enrollment,
            'last_payment': last_pay,
            'attendance_total': total_att,
            'attendance_present': present_att,
        })

    return render(request, 'masters/my_students.html', {
        'master': master,
        'student_rows': student_rows,
    })


@login_required
def student_detail(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk, masters=master)

    enrollment = StudentEnrollment.objects.filter(master=master, panda=panda).first()
    attendances = Attendance.objects.filter(master=master, panda=panda)
    payments = StudentPayment.objects.filter(master=master, panda=panda)
    certificates = Certificate.objects.filter(master=master, panda=panda)

    att_total = attendances.count()
    att_present = attendances.filter(status=Attendance.PRESENT).count()
    att_late = attendances.filter(status=Attendance.LATE).count()

    stats = panda.attempts.filter(status='completed').aggregate(
        total=Count('id'),
        avg_score=Avg('score'),
    )

    today = timezone.now().date()

    return render(request, 'masters/student_detail.html', {
        'master': master,
        'panda': panda,
        'enrollment': enrollment,
        'attendances': attendances[:20],
        'payments': payments,
        'certificates': certificates,
        'att_total': att_total,
        'att_present': att_present,
        'att_late': att_late,
        'stats': stats,
        'today': today,
    })


@login_required
def add_student(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        from django.contrib.auth.models import User
        from panda.models import Panda
        username = request.POST.get('username', '').strip()
        try:
            user = User.objects.get(username=username)
            panda = user.profile.panda
            if master.pandas.filter(pk=panda.pk).exists():
                messages.info(request, f'{username} is already your student.')
            else:
                master.pandas.add(panda)
                StudentEnrollment.objects.get_or_create(master=master, panda=panda)
                master.update_stats()
                messages.success(request, f'{username} has been added as your student.')
        except User.DoesNotExist:
            messages.error(request, f'No user found with username "{username}".')
        except Exception:
            messages.error(request, 'That user does not have a student profile.')

    return redirect('masters-my-students', pk=master.pk)


@login_required
def mark_attendance(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk, masters=master)

    if request.method == 'POST':
        date_str = request.POST.get('date', str(timezone.now().date()))
        status = request.POST.get('status', Attendance.PRESENT)
        notes = request.POST.get('notes', '')
        try:
            from datetime import date as date_type
            import datetime
            att_date = datetime.date.fromisoformat(date_str)
        except ValueError:
            att_date = timezone.now().date()

        att, created = Attendance.objects.update_or_create(
            master=master, panda=panda, date=att_date,
            defaults={'status': status, 'notes': notes},
        )
        action = 'Marked' if created else 'Updated'
        messages.success(request, f'{action} attendance for {panda.profile.user.username} on {att_date}.')

    return redirect('masters-student-detail', pk=master.pk, panda_pk=panda.pk)


@login_required
def add_payment(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk, masters=master)

    if request.method == 'POST':
        import decimal
        try:
            amount = decimal.Decimal(request.POST.get('amount', '0'))
        except decimal.InvalidOperation:
            messages.error(request, 'Invalid amount.')
            return redirect('masters-student-detail', pk=master.pk, panda_pk=panda.pk)

        period_label = request.POST.get('period_label', '')
        status = request.POST.get('status', StudentPayment.UNPAID)
        notes = request.POST.get('notes', '')
        due_date_str = request.POST.get('due_date', '')
        payment_date_str = request.POST.get('payment_date', '')

        import datetime
        due_date = None
        payment_date = None
        try:
            if due_date_str:
                due_date = datetime.date.fromisoformat(due_date_str)
            if payment_date_str:
                payment_date = datetime.date.fromisoformat(payment_date_str)
        except ValueError:
            pass

        StudentPayment.objects.create(
            master=master, panda=panda, amount=amount,
            period_label=period_label, status=status,
            notes=notes, due_date=due_date, payment_date=payment_date,
        )
        messages.success(request, f'Payment record added for {panda.profile.user.username}.')

    return redirect('masters-student-detail', pk=master.pk, panda_pk=panda.pk)


@login_required
def delete_payment(request, pk, payment_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    payment = get_object_or_404(StudentPayment, pk=payment_pk, master=master)
    panda_pk = payment.panda_id
    if request.method == 'POST':
        payment.delete()
        messages.success(request, 'Payment record deleted.')
    return redirect('masters-student-detail', pk=master.pk, panda_pk=panda_pk)


@login_required
def issue_certificate(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk, masters=master)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if not title:
            messages.error(request, 'Certificate title is required.')
        else:
            Certificate.objects.create(
                master=master, panda=panda,
                title=title, description=description,
            )
            messages.success(request, f'Certificate "{title}" issued to {panda.profile.user.username}.')

    return redirect('masters-student-detail', pk=master.pk, panda_pk=panda.pk)


@login_required
def delete_certificate(request, pk, cert_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    cert = get_object_or_404(Certificate, pk=cert_pk, master=master)
    panda_pk = cert.panda_id
    if request.method == 'POST':
        cert.delete()
        messages.success(request, 'Certificate revoked.')
    return redirect('masters-student-detail', pk=master.pk, panda_pk=panda_pk)
