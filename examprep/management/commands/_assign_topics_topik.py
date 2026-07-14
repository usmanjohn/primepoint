"""One-off: group existing TOPIK lessons into Topics (run via manage.py shell)."""
from examprep.models import ExamTrack, Topic, Lesson

track = ExamTrack.objects.get(name='TOPIK')

# (skill, topic title, summary, icon, order, lesson-title-prefix matchers)
PLAN = [
    ('reading', "Strategiya va metod (읽기 전략)",
     "O'qish bo'limiga umumiy yondashuv: tuzilma, asosiy fikr, so'z o'rganish metodi.",
     'bi-compass', 1,
     ['TOPIK Reading 1', 'TOPIK Reading 2', 'TOPIK Reading 3', 'TOPIK Reading 4']),

    ('writing', "51-savol: Bo'sh joyni to'ldirish (빈칸 채우기)",
     "Amaliy matndagi ikkita bo'sh joyga mos jumla yozish — shablonlar va namunalar.",
     'bi-input-cursor-text', 1, ['TOPIK Writing 51']),

    ('writing', "52-savol: Izohli matn (설명문)",
     "Ilmiy-ommabop matndagi bo'sh joylarni to'ldirish — yondashuv va grammatik shakllar.",
     'bi-card-text', 2, ['TOPIK Writing 52']),

    ('writing', "53-savol: Grafik tasvirlash (도표 분석)",
     "Grafik va jadval ma'lumotlarini 200–300 belgida tasvirlash.",
     'bi-bar-chart', 3, ['TOPIK Writing 53']),

    ('writing', "54-savol: Insho (논술문)",
     "600–700 belgilik insho: jumla yodlash metodi va mavzu jumlalari to'plami.",
     'bi-journal-richtext', 4, ['TOPIK Writing 54']),

    ('listening', "Podkast metodi (팟캐스트)",
     "Tinglashni podkast bilan mashq qilish — nega va qanday.",
     'bi-broadcast', 1, ['TOPIK Listening']),

    ('strategy', "TOPIK II bilan tanishuv (시험 소개)",
     "Imtihon tuzilmasi, vaqt, ball tizimi va savol turlari.",
     'bi-map', 1, ['TOPIK II — Kirish']),

    ('strategy', "O'rganish metodikasi (학습 전략)",
     "Qanday tayyorlanish kerak: bitta shablonni mukammal egallash va vaqt rejasi.",
     'bi-lightbulb', 2, ['TOPIK Strategy']),
]

for skill, title, summary, icon, order, prefixes in PLAN:
    topic, created = Topic.objects.get_or_create(
        track=track, skill=skill, title=title,
        defaults={'summary': summary, 'icon': icon, 'order': order},
    )
    if not created:
        topic.summary, topic.icon, topic.order = summary, icon, order
        topic.save()
    qs = Lesson.objects.filter(track=track, skill=skill)
    moved = 0
    for lesson in qs:
        if any(lesson.title.startswith(p) for p in prefixes):
            lesson.topic = topic
            lesson.save(update_fields=['topic'])
            moved += 1
    print(f"{'created' if created else 'updated'}: [{skill}] {title} — {moved} lessons")

orphans = Lesson.objects.filter(track=track, topic__isnull=True)
print('\nLessons left without a topic:', orphans.count())
for l in orphans:
    print(' -', l.skill, '|', l.title)
