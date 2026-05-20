from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    {
        'text': "<p><strong>A: Do we need to hurry?<br>B: Yes, we don't have ________ time left before the train departs.</strong></p>",
        'explanation': "<p><strong>much</strong>: 'time' (vaqt) sanalmaydigan ot (uncountable noun) bo'lib, inkor gaplarda odatda <code>much</code> ishlatiladi.</p>",
        'correct': "much",
        'choices': ["many", "a few", "much", "several"]
    },
    {
        'text': "<p><strong>A: Were there ________ people at the outdoor concert yesterday?<br>B: Yes, the stadium was completely full!</strong></p>",
        'explanation': "<p><strong>many</strong>: 'people' (odamlar) sanaladigan ko'plikdagi ot (countable plural). So'roq gaplarda uning miqdorini so'rash uchun <code>many</code> ishlatiladi.</p>",
        'correct': "many",
        'choices': ["much", "many", "a little", "any"]
    },
    {
        'text': "<p><strong>A: I am going to the supermarket. Do you need anything?<br>B: Could you buy ________ fresh apples, please?</strong></p>",
        'explanation': "<p><strong>some</strong>: Darak gaplarda yoki kimgadir iltimos qilganda (Could you buy...?) sanaladigan va sanalmaydigan otlar bilan <code>some</code> ishlatiladi.</p>",
        'correct': "some",
        'choices': ["any", "a little", "some", "much"]
    },
    {
        'text': "<p><strong>A: Did you find ________ useful information on that old website?<br>B: No, nothing at all.</strong></p>",
        'explanation': "<p><strong>any</strong>: So'roq va inkor gaplarda \"hech qanday\" ma'nosini berish uchun <code>any</code> ishlatiladi.</p>",
        'correct': "any",
        'choices': ["any", "some", "a lot", "many"]
    },
    {
        'text': "<p><strong>A: I only have ________ close friends in this city, but we are very happy together.<br>B: That's wonderful to hear.</strong></p>",
        'explanation': "<p><strong>a few</strong>: Sanaladigan otlar bilan \"bir nechta, ozgina bo'lsa ham yetarli\" (ijobiy ma'no) deyish uchun <code>a few</code> qo'llaniladi.</p>",
        'correct': "a few",
        'choices': ["a little", "few", "much", "a few"]
    },
    {
        'text': "<p><strong>A: Why is he so sad today?<br>B: Unfortunately, he has ________ hope of passing the final exam.</strong></p>",
        'explanation': "<p><strong>little</strong>: 'hope' (umid) sanalmaydigan ot. \"Juda kam, deyarli yo'q\" (salbiy ma'no) deyish uchun artiklsiz <code>little</code> ishlatiladi.</p>",
        'correct': "little",
        'choices': ["little", "a little", "few", "many"]
    },
    {
        'text': "<p><strong>A: Would you like ________ extra milk in your hot coffee?<br>B: Yes, just a drop, please.</strong></p>",
        'explanation': "<p><strong>some</strong>: Kimgadir biror narsa taklif qilinganda (Would you like...?) so'roq gap bo'lishiga qaramay <code>some</code> ishlatiladi.</p>",
        'correct': "some",
        'choices': ["any", "some", "many", "few"]
    },
    {
        'text': "<p><strong>A: The weather was absolutely terrible yesterday.<br>B: Yes, that's why hardly ________ tourists visited the museum.</strong></p>",
        'explanation': "<p><strong>any</strong>: 'hardly' (arangs, deyarli yo'q) so'zi o'zida inkor ma'nosini tashigani uchun undan keyin doim <code>any</code> keladi.</p>",
        'correct': "any",
        'choices': ["some", "no", "any", "many"]
    },
    {
        'text': "<p><strong>A: Can you speak Spanish?<br>B: Yes, but only ________. I am still learning.</strong></p>",
        'explanation': "<p><strong>a little</strong>: Tilni bilish darajasi sanalmaydi. \"Ozgina, biroz\" (ijobiy ma'no) deyish uchun <code>a little</code> ishlatiladi.</p>",
        'correct': "a little",
        'choices': ["a few", "a little", "many", "few"]
    },
    {
        'text': "<p><strong>A: Don't rush! We still have ________ time to finish this project.<br>B: Oh, that's a huge relief.</strong></p>",
        'explanation': "<p><strong>plenty of</strong>: \"Keragidan ham ko'p, bemalol yetadigan\" ma'nosini berish uchun <code>plenty of</code> ishlatiladi. U ham sanaladigan, ham sanalmaydigan otlarga tushadi.</p>",
        'correct': "plenty of",
        'choices': ["many", "plenty of", "a few", "several"]
    },
    {
        'text': "<p><strong>A: Are there ________ chairs in the conference room for everyone?<br>B: Yes, I brought five extra ones.</strong></p>",
        'explanation': "<p><strong>enough</strong>: \"Yetarli\" degan ma'noni beradi. Otlardan oldin kelib, miqdorning talabga javob berishini ko'rsatadi.</p>",
        'correct': "enough",
        'choices': ["much", "little", "enough", "a little"]
    },
    {
        'text': "<p><strong>A: How ________ sugar do you usually put in your green tea?<br>B: Just one spoon.</strong></p>",
        'explanation': "<p><strong>much</strong>: 'sugar' (shakar) sanalmaydigan ot. Miqdorini so'rash uchun <code>How much</code> ishlatiladi.</p>",
        'correct': "much",
        'choices': ["much", "many", "often", "any"]
    },
    {
        'text': "<p><strong>A: Look at those clouds! Should we take a taxi?<br>B: Good idea, we only have ________ minutes before the heavy rain starts.</strong></p>",
        'explanation': "<p><strong>a few</strong>: 'minutes' sanaladigan ot. \"Only\" (faqatgina) so'zi bilan odatda <code>a few</code> yoki <code>a little</code> keladi, bu yerda sanaladigan ot bo'lgani uchun <code>a few</code>.</p>",
        'correct': "a few",
        'choices': ["a little", "few", "a few", "much"]
    },
    {
        'text': "<p><strong>A: Building that new modern bridge required ________ money and planning.<br>B: I can imagine!</strong></p>",
        'explanation': "<p><strong>a great deal of</strong>: Katta miqdordagi sanalmaydigan otlar (money, planning) bilan rasmiyroq ohangda <code>a great deal of</code> ishlatiladi.</p>",
        'correct': "a great deal of",
        'choices': ["a great deal of", "a large number of", "many", "several"]
    },
    {
        'text': "<p><strong>A: Where are my keys?<br>B: I have absolutely ________ idea. I haven't seen them.</strong></p>",
        'explanation': "<p><strong>no</strong>: Darak shaklidagi fe'l (have) bilan inkor ma'no berish uchun <code>no</code> ishlatiladi. \"I have no idea\" - \"Hech qanday fikrim yo'q\".</p>",
        'correct': "no",
        'choices': ["not", "any", "no", "none"]
    },
    {
        'text': "<p><strong>A: Which of these two buses goes to the city center?<br>B: You can take ________ bus. They both go there.</strong></p>",
        'explanation': "<p><strong>either</strong>: Ikkita narsadan xohlagan birini tanlash mumkin bo'lganda \"ikkovidan biri / farqi yo'q\" ma'nosida <code>either</code> ishlatiladi.</p>",
        'correct': "either",
        'choices': ["neither", "all", "both", "either"]
    },
    {
        'text': "<p><strong>A: Did both candidates pass the tough interview?<br>B: No, ________ of them was qualified for the position.</strong></p>",
        'explanation': "<p><strong>neither</strong>: Ikkita narsaning ikkalasi ham inkor qilinganda \"ikkoviyam emas\" ma'nosida <code>neither</code> qo'llaniladi.</p>",
        'correct': "neither",
        'choices': ["either", "neither", "none", "both"]
    },
    {
        'text': "<p><strong>A: How many tickets are left for the evening show?<br>B: ________. They sold out completely this morning.</strong></p>",
        'explanation': "<p><strong>None</strong>: \"Qancha?\" savoliga \"hech qancha / umuman yo'q\" deb to'g'ridan-to'g'ri qisqa javob berilganda mustaqil olmosh sifatida <code>None</code> ishlatiladi.</p>",
        'correct': "None",
        'choices': ["No", "None", "Any", "Nothing"]
    },
    {
        'text': "<p><strong>A: He has visited that beautiful island ________ times during his summer holidays.<br>B: He must really love it there!</strong></p>",
        'explanation': "<p><strong>several</strong>: \"Bir necha\" (ikkitadan ko'p, lekin juda ko'p emas) degan ma'noni beradi va sanaladigan ko'plikdagi otlar bilan ishlatiladi.</p>",
        'correct': "several",
        'choices': ["much", "several", "a little", "every"]
    },
    {
        'text': "<p><strong>A: I am extremely thirsty. Can I have ________ water, please?<br>B: Of course, here you go.</strong></p>",
        'explanation': "<p><strong>some</strong>: Birovdan biror narsani iltimos qilib so'raganda (Can I have...?) so'roq gap bo'lishiga qaramay <code>some</code> ishlatiladi.</p>",
        'correct': "some",
        'choices': ["some", "any", "few", "many"]
    },
    {
        'text': "<p><strong>A: Are you going to eat ________ the cookies by yourself?<br>B: No, I will share them with my little sister.</strong></p>",
        'explanation': "<p><strong>all</strong>: Biror narsaning to'liq hammasini (100%) ifodalash uchun <code>all</code> ishlatiladi.</p>",
        'correct': "all",
        'choices': ["each", "every", "all", "much"]
    },
    {
        'text': "<p><strong>A: The teacher gave a special gold star to ________ student in the classroom.<br>B: That's so encouraging!</strong></p>",
        'explanation': "<p><strong>every</strong>: Gurohdagi barcha a'zolarni umumlashtirib, har biriga nisbatan aytilganda birlikdagi sanaladigan otlar bilan <code>every</code> keladi.</p>",
        'correct': "every",
        'choices': ["all", "many", "every", "some"]
    },
    {
        'text': "<p><strong>A: ________ of the people in this quiet neighborhood are incredibly friendly.<br>B: I totally agree.</strong></p>",
        'explanation': "<p><strong>Most</strong>: \"Aksariyat, ko'pchilik\" ma'nosini berish uchun <code>Most of</code> qurilmasi ishlatiladi.</p>",
        'correct': "Most",
        'choices': ["Most", "Much", "Every", "Any"]
    },
    {
        'text': "<p><strong>A: Which dress should I buy? The red one or the blue one?<br>B: Honestly, ________ of them look amazing on you. Buy the two!</strong></p>",
        'explanation': "<p><strong>both</strong>: Ikkita narsaning ikkalasi ham kiritilganda \"ikkalasi ham\" ma'nosida <code>both</code> ishlatiladi.</p>",
        'correct': "both",
        'choices': ["either", "both", "neither", "all"]
    },
    {
        'text': "<p><strong>A: Does your new luxury car use ________ petrol?<br>B: Yes, it's very expensive to maintain.</strong></p>",
        'explanation': "<p><strong>a lot of</strong>: Darak va so'roq gaplarda katta miqdorni ko'rsatish uchun ham sanaladigan, ham sanalmaydigan (petrol) otlar bilan <code>a lot of</code> kelishi mumkin.</p>",
        'correct': "a lot of",
        'choices': ["many", "a few", "a lot of", "several"]
    },
    {
        'text': "<p><strong>A: Sadly, ________ students passed the extremely difficult math exam today.<br>B: The teacher should probably make it easier next time.</strong></p>",
        'explanation': "<p><strong>few</strong>: \"Juda kam, deyarli hech kim\" (salbiy ma'no) deyish uchun sanaladigan otlar (students) bilan artiklsiz <code>few</code> ishlatiladi.</p>",
        'correct': "few",
        'choices': ["a little", "few", "much", "a few"]
    },
    {
        'text': "<p><strong>A: I'm free all weekend. We can meet on Saturday or Sunday.<br>B: Great! ________ day is perfectly fine for me.</strong></p>",
        'explanation': "<p><strong>Either</strong>: Ikkita variantdan \"xohlagan bittasi / qaysi biri bo'lsa ham\" ma'nosida birlikdagi ot bilan <code>Either</code> ishlatiladi.</p>",
        'correct': "Either",
        'choices': ["Both", "Neither", "Either", "All"]
    },
    {
        'text': "<p><strong>A: Can I grab a pen from your desk?<br>B: Sure, take ________ pen you like. I have dozens of them.</strong></p>",
        'explanation': "<p><strong>any</strong>: Darak gaplarda <code>any</code> \"istalgan, xohlagan bittasi\" degan kuchli ma'noni anglatib kelishi mumkin.</p>",
        'correct': "any",
        'choices': ["some", "any", "many", "few"]
    },
    {
        'text': "<p><strong>A: She spent ________ money on her brand new sports car.<br>B: I heard it cost over a hundred thousand dollars!</strong></p>",
        'explanation': "<p><strong>a lot of</strong>: Darak gaplarda ko'p miqdorni ifodalash uchun sanalmaydigan otlar bilan eng tabiiy tanlov <code>a lot of</code> (yoki lots of) hisoblanadi.</p>",
        'correct': "a lot of",
        'choices': ["many", "few", "a lot of", "several"]
    },
    {
        'text': "<p><strong>A: I have to translate ________ documents before I can leave the office.<br>B: Do you need some help with them?</strong></p>",
        'explanation': "<p><strong>a number of</strong>: \"Bir qancha, ko'pgina\" ma'nosini berib, faqat sanaladigan ko'plikdagi otlar (documents) bilan ishlatiladi.</p>",
        'correct': "a number of",
        'choices': ["a great deal of", "much", "a number of", "a little"]
    }
]
class Command(BaseCommand):
    help = 'Create an English grammar practice test (wh?)'

    def add_arguments(self, parser):
        parser.add_argument('--master', default='powerty', help='Username of the master to assign this practice to')

    def handle(self, *args, **options):
        master_username = options['master']
        try:
            user = User.objects.get(username=master_username)
        except User.DoesNotExist:
            raise CommandError(f"User '{master_username}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{master_username}'.")

        subject, _ = Subject.objects.get_or_create(
            name='English',
            defaults={'description': 'English grammar and vocabulary practice'},
        )

        # Create or get the practice and ensure it is published
        practice, created = Practice.objects.get_or_create(
            title='English Grammar Practice: Quantifiers and Determiners',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Practice using quantifiers and determiners in various contexts.',
                'subject': subject,
                'level': 'easy',
                'is_free': True,
                'is_published': True,
                'is_available_for_all': True,
                'pass_score': 60,
                'max_attempts': 0,
                'show_answers_after': True,
            },
        )

        if not created:
            # If it already exists, update it to make sure it is published
            practice.is_published = True
            practice.save()
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Set to published."
            ))
            # Delete old questions to replace with fresh ones if needed, or simply return.
            # Returning to avoid duplicates, assuming it's already populated.
            return

        for i, q in enumerate(QUESTIONS, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q['text'],
                #hint=q['hint'],
                explanation=q['explanation'],
                order=i,
                points=1,
                made_by=master,
            )
            for choice_text in q['choices']:
                PracticeChoice.objects.create(
                    question=question,
                    text=choice_text,
                    is_correct=(choice_text == q['correct']),
                )

        self.stdout.write(self.style.SUCCESS(
            f"Created and published practice '{practice.title}' with {len(QUESTIONS)} questions (id={practice.pk})."
        ))