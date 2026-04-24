from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q

from .models import Category, Thread, Reply, ThreadVote, ReplyVote
from .forms import ThreadForm, ReplyForm


def _is_privileged(user):
    return user.is_staff or getattr(getattr(user, 'profile', None), 'is_master', False)


def discussion_home(request):
    threads = Thread.objects.select_related('author', 'category').annotate(
        num_replies=Count('replies', distinct=True),
        score=Sum('votes__value'),
    )

    category_slug = request.GET.get('category')
    sort = request.GET.get('sort', 'latest')
    search = request.GET.get('q', '').strip()

    active_category = None
    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        threads = threads.filter(category=active_category)

    if search:
        threads = threads.filter(Q(title__icontains=search) | Q(body__icontains=search))

    if sort == 'votes':
        threads = threads.order_by('-is_pinned', '-score', '-created_at')
    elif sort == 'activity':
        threads = threads.order_by('-is_pinned', '-updated_at')
    elif sort == 'unanswered':
        threads = threads.filter(num_replies=0).order_by('-created_at')
    else:
        threads = threads.order_by('-is_pinned', '-created_at')

    categories = Category.objects.annotate(thread_count=Count('threads'))
    context = {
        'threads': threads,
        'categories': categories,
        'active_category': active_category,
        'sort': sort,
        'search': search,
    }
    return render(request, 'discussion/home.html', context)


def thread_detail(request, pk):
    thread = get_object_or_404(Thread.objects.select_related('author', 'category'), pk=pk)
    Thread.objects.filter(pk=pk).update(view_count=thread.view_count + 1)

    replies = thread.replies.select_related('author').all()

    user_thread_vote = 0
    if request.user.is_authenticated:
        user_thread_vote = thread.user_vote(request.user)
        for r in replies:
            r.user_vote_value = r.user_vote(request.user)
    else:
        for r in replies:
            r.user_vote_value = 0

    reply_form = ReplyForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        if thread.is_closed:
            messages.error(request, 'This thread is closed.')
            return redirect('thread_detail', pk=pk)
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.thread = thread
            reply.author = request.user
            reply.save()
            messages.success(request, 'Reply posted.')
            return redirect('thread_detail', pk=pk)

    context = {
        'thread': thread,
        'replies': replies,
        'reply_form': reply_form,
        'user_thread_vote': user_thread_vote,
        'can_manage': request.user.is_authenticated and (
            thread.author == request.user or _is_privileged(request.user)
        ),
        'is_thread_author': request.user.is_authenticated and thread.author == request.user,
    }
    return render(request, 'discussion/thread_detail.html', context)


@login_required
def create_thread(request):
    form = ThreadForm(user=request.user)
    if request.method == 'POST':
        form = ThreadForm(request.POST, user=request.user)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            if thread.is_announcement and not _is_privileged(request.user):
                thread.is_announcement = False
            thread.save()
            messages.success(request, 'Thread created!')
            return redirect('thread_detail', pk=thread.pk)
    return render(request, 'discussion/thread_form.html', {'form': form, 'action': 'Create'})


@login_required
def edit_thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if thread.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'You cannot edit this thread.')
        return redirect('thread_detail', pk=pk)
    form = ThreadForm(instance=thread, user=request.user)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread, user=request.user)
        if form.is_valid():
            thread = form.save(commit=False)
            if thread.is_announcement and not _is_privileged(request.user):
                thread.is_announcement = False
            thread.save()
            messages.success(request, 'Thread updated.')
            return redirect('thread_detail', pk=pk)
    return render(request, 'discussion/thread_form.html', {'form': form, 'action': 'Edit', 'thread': thread})


@login_required
def delete_thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if thread.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'You cannot delete this thread.')
        return redirect('thread_detail', pk=pk)
    if request.method == 'POST':
        thread.delete()
        messages.success(request, 'Thread deleted.')
        return redirect('discussion_home')
    return render(request, 'discussion/confirm_delete.html', {'object': thread, 'type': 'thread'})


@login_required
def edit_reply(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    if reply.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'You cannot edit this reply.')
        return redirect('thread_detail', pk=reply.thread.pk)
    form = ReplyForm(instance=reply)
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reply updated.')
            return redirect('thread_detail', pk=reply.thread.pk)
    return render(request, 'discussion/reply_form.html', {'form': form, 'reply': reply})


@login_required
def delete_reply(request, pk):
    reply = get_object_or_404(Reply, pk=pk)
    thread_pk = reply.thread.pk
    if reply.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'You cannot delete this reply.')
        return redirect('thread_detail', pk=thread_pk)
    if request.method == 'POST':
        reply.delete()
        messages.success(request, 'Reply deleted.')
        return redirect('thread_detail', pk=thread_pk)
    return render(request, 'discussion/confirm_delete.html', {'object': reply, 'type': 'reply', 'thread_pk': thread_pk})


@login_required
def vote_thread(request, pk, value=1):
    if request.method != 'POST':
        return redirect('thread_detail', pk=pk)
    thread = get_object_or_404(Thread, pk=pk)
    vote, created = ThreadVote.objects.get_or_create(user=request.user, thread=thread, defaults={'value': value})
    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save()
    return redirect(request.META.get('HTTP_REFERER') or 'discussion_home')


@login_required
def vote_reply(request, pk, value=1):
    if request.method != 'POST':
        return redirect('discussion_home')
    reply = get_object_or_404(Reply, pk=pk)
    vote, created = ReplyVote.objects.get_or_create(user=request.user, reply=reply, defaults={'value': value})
    if not created:
        if vote.value == value:
            vote.delete()
        else:
            vote.value = value
            vote.save()
    return redirect(request.META.get('HTTP_REFERER') or 'discussion_home')


@login_required
def mark_accepted(request, pk):
    if request.method != 'POST':
        return redirect('discussion_home')
    reply = get_object_or_404(Reply, pk=pk)
    thread = reply.thread
    if thread.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'Only the thread author can mark an accepted answer.')
        return redirect('thread_detail', pk=thread.pk)
    if reply.is_accepted:
        reply.is_accepted = False
        reply.save()
    else:
        thread.replies.update(is_accepted=False)
        reply.is_accepted = True
        reply.save()
    return redirect('thread_detail', pk=thread.pk)


@login_required
def toggle_close(request, pk):
    if request.method != 'POST':
        return redirect('thread_detail', pk=pk)
    thread = get_object_or_404(Thread, pk=pk)
    if thread.author != request.user and not _is_privileged(request.user):
        messages.error(request, 'Permission denied.')
        return redirect('thread_detail', pk=pk)
    thread.is_closed = not thread.is_closed
    thread.save()
    return redirect('thread_detail', pk=pk)


@login_required
def toggle_pin(request, pk):
    if request.method != 'POST':
        return redirect('thread_detail', pk=pk)
    if not _is_privileged(request.user):
        messages.error(request, 'Only masters or admins can pin threads.')
        return redirect('thread_detail', pk=pk)
    thread = get_object_or_404(Thread, pk=pk)
    thread.is_pinned = not thread.is_pinned
    thread.save()
    return redirect('thread_detail', pk=pk)
