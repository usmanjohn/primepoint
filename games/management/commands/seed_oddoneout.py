from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from games.models import OddOneOutPack, OddOneOutQuestion


PACKS = [
    {
        'title': 'English – Easy (IELTS Foundation)',
        'description': 'Basic verbs, adjectives, and adverbs for daily communication.',
        'language': 'en',
        'questions': [
            ('Sleep', 'Run', 'Walk', 'Sprint', 0, 'Sleep does not involve physical movement; the others are ways of moving.'),
            ('Happy', 'Joyful', 'Sad', 'Cheerful', 2, 'Sad is a negative emotion; the others are positive.'),
            ('Quickly', 'Fast', 'Rapidly', 'Slowly', 3, 'Slowly indicates low speed; the others indicate high speed.'),
            ('Tiny', 'Big', 'Large', 'Huge', 0, 'Tiny means small; the others mean very large.'),
            ('Eat', 'Chew', 'Blink', 'Swallow', 2, 'Blink is an action of the eyes; the others involve the mouth.'),
            ('Hot', 'Freezing', 'Warm', 'Boiling', 1, 'Freezing is extremely cold; the others are degrees of heat.'),
            ('Loudly', 'Quietly', 'Silently', 'Calmly', 0, 'Loudly involves making noise; the others do not.'),
            ('Look', 'Stare', 'Watch', 'Listen', 3, 'Listen is done with ears; the others are done with eyes.'),
            ('Hard', 'Soft', 'Smooth', 'Furry', 0, 'Hard is a firm, rigid texture; the others are gentle or yielding.'),
            ('Always', 'Forever', 'Never', 'Constantly', 2, 'Never means zero frequency; the others mean all the time.'),
            ('Push', 'Shove', 'Press', 'Pull', 3, 'Pull draws things closer; the others move things away.'),
            ('Ugly', 'Beautiful', 'Pretty', 'Gorgeous', 0, 'Ugly means unattractive; the others mean aesthetically pleasing.'),
            ('Very', 'Extremely', 'Slightly', 'Incredibly', 2, 'Slightly indicates a small degree; the others indicate a high degree.'),
            ('Sing', 'Hum', 'Chant', 'Dance', 3, 'Dance involves moving the body; the others use the vocal cords.'),
            ('Sweet', 'Salty', 'Sour', 'Loud', 3, 'Loud is an auditory description; the others are tastes.'),
            ('Laugh', 'Cry', 'Weep', 'Sob', 0, 'Laugh expresses joy; the others express sadness.'),
            ('Carefully', 'Cautiously', 'Recklessly', 'Safely', 2, 'Recklessly means acting without care or caution.'),
            ('Short', 'Tall', 'High', 'Elevated', 0, 'Short indicates low height; the others indicate great height.'),
            ('Bright', 'Shiny', 'Luminous', 'Dark', 3, 'Dark lacks light; the others radiate or reflect light.'),
            ('Mute', 'Speak', 'Talk', 'Say', 0, 'Mute means silent; the others involve verbalizing.'),
            ('Upward', 'Downward', 'Above', 'Higher', 1, 'Downward moves lower; the others relate to going up.'),
            ('Open', 'Close', 'Shut', 'Seal', 0, 'Open makes accessible; the others are actions of securing or locking.'),
            ('Early', 'Prematurely', 'Soon', 'Late', 3, 'Late is after the expected time; the others are before or on time.'),
            ('Straight', 'Round', 'Circular', 'Spherical', 0, 'Straight lacks curves; the others describe curved shapes.'),
            ('Melt', 'Freeze', 'Thaw', 'Dissolve', 1, 'Freeze turns liquid to solid; the others involve becoming liquid or soft.'),
            ('Wet', 'Damp', 'Moist', 'Dry', 3, 'Dry lacks moisture; the others have moisture.'),
            ('Dirty', 'Clean', 'Wash', 'Scrub', 0, 'Dirty means to soil; the others are verbs for removing dirt.'),
            ('Strong', 'Powerful', 'Mighty', 'Weak', 3, 'Weak lacks strength; the others possess it.'),
            ('Work', 'Play', 'Amuse', 'Entertain', 0, 'Work is labor; the others relate to leisure or fun.'),
            ('Catch', 'Grab', 'Drop', 'Hold', 2, 'Drop means to let go; the others mean to secure in the hands.'),
        ],
    },
    {
        'title': 'English – Hard (IELTS Academic)',
        'description': 'Essential academic verbs, adjectives, and adverbs for higher bands.',
        'language': 'en',
        'questions': [
            ('Ignore', 'Analyze', 'Evaluate', 'Assess', 0, 'Ignore means to pay no attention; the others are actions of careful examination.'),
            ('Increase', 'Expand', 'Shrink', 'Grow', 2, 'Shrink means to get smaller; the others mean to get larger.'),
            ('Accurately', 'Precisely', 'Exactly', 'Vaguely', 3, 'Vaguely means unclearly; the others mean with exact correctness.'),
            ('Crucial', 'Significant', 'Minor', 'Important', 2, 'Minor means of little importance; the others mean very important.'),
            ('Create', 'Destroy', 'Ruin', 'Demolish', 0, 'Create means to make; the others mean to tear down or break.'),
            ('Rapidly', 'Swiftly', 'Gradually', 'Quickly', 2, 'Gradually means slowly over time; the others mean very fast.'),
            ('Improve', 'Worsen', 'Enhance', 'Upgrade', 1, 'Worsen means to decline; the others mean to make better.'),
            ('Simple', 'Complex', 'Complicated', 'Intricate', 0, 'Simple means easy to understand; the others describe things with many confusing parts.'),
            ('Frequently', 'Regularly', 'Often', 'Rarely', 3, 'Rarely means almost never; the others mean happening a lot.'),
            ('Reject', 'Deny', 'Decline', 'Accept', 3, 'Accept means to say yes; the others mean to say no or refuse.'),
            ('Temporary', 'Permanent', 'Everlasting', 'Endless', 0, 'Temporary means lasting only a short time; the others mean lasting forever.'),
            ('Connect', 'Separate', 'Link', 'Join', 1, 'Separate means to pull apart; the others mean to put together.'),
            ('Clearly', 'Obscurely', 'Vaguely', 'Unclearly', 0, 'Clearly means easy to see or understand; the others mean the opposite.'),
            ('Stabilize', 'Fluctuate', 'Vary', 'Change', 0, 'Stabilize means to stay the same; the others mean to shift or alter.'),
            ('Sufficient', 'Adequate', 'Lacking', 'Enough', 2, 'Lacking means not having enough; the others mean having the required amount.'),
            ('Benefit', 'Profit', 'Gain', 'Lose', 3, 'Lose means to be deprived of something; the others mean to acquire an advantage.'),
            ('Modern', 'Traditional', 'Old', 'Ancient', 0, 'Modern means relating to the present; the others relate to the past.'),
            ('Deliberately', 'Accidentally', 'Unintentionally', 'Mistakenly', 0, 'Deliberately means on purpose; the others mean happening by chance.'),
            ('Promote', 'Encourage', 'Hinder', 'Support', 2, 'Hinder means to hold back; the others mean to help forward.'),
            ('Useless', 'Efficient', 'Effective', 'Productive', 0, 'Useless means having no practical value; the others describe successful performance.'),
            ('Conceal', 'Reveal', 'Hide', 'Cover', 1, 'Reveal means to show; the others mean to keep hidden.'),
            ('Strict', 'Lenient', 'Flexible', 'Relaxed', 0, 'Strict means firmly enforcing rules; the others mean allowing freedom.'),
            ('Maintain', 'Preserve', 'Keep', 'Abandon', 3, 'Abandon means to leave behind; the others mean to hold onto.'),
            ('Voluntary', 'Mandatory', 'Required', 'Compulsory', 0, 'Voluntary means by choice; the others mean forced by rule.'),
            ('Predict', 'Forecast', 'Prove', 'Guess', 2, 'Prove means to show the truth with evidence; the others mean estimating the future.'),
            ('Scarce', 'Abundant', 'Plentiful', 'Ample', 0, 'Scarce means very rare; the others mean existing in large quantities.'),
            ('Examine', 'Inspect', 'Ignore', 'Review', 2, 'Ignore means to overlook; the others mean to look at closely.'),
            ('Suddenly', 'Gradually', 'Steadily', 'Slowly', 0, 'Suddenly means happening without warning; the others describe slow progression.'),
            ('Construct', 'Build', 'Assemble', 'Destroy', 3, 'Destroy means to tear down; the others mean to put together.'),
            ('Identical', 'Similar', 'Alike', 'Different', 3, 'Different means not the same; the others highlight shared characteristics.'),
        ],
    },
    {
        'title': '한국어 – 쉬운 문제 (TOPIK I)',
        'description': '일상 대화에 자주 쓰이는 기초 동사, 형용사, 부사입니다.',
        'language': 'ko',
        'questions': [
            ('자다', '뛰다', '달리다', '걷다', 0, '자다는 움직임이 없는 행동입니다.'),
            ('예쁘다', '아름답다', '밉다', '귀엽다', 2, '밉다는 부정적인 느낌입니다.'),
            ('천천히', '빨리', '일찍', '신속히', 0, '천천히는 느린 속도를 의미합니다.'),
            ('넓다', '거대하다', '작다', '크다', 2, '작다는 크기가 반대되는 형용사입니다.'),
            ('먹다', '씹다', '보다', '마시다', 2, '보다는 눈으로 하는 행동이고 나머지는 입과 관련됩니다.'),
            ('뜨겁다', '따뜻하다', '차갑다', '덥다', 2, '차갑다는 온도가 낮음을 의미합니다.'),
            ('시끄럽게', '조용히', '가만히', '잠잠히', 0, '시끄럽게는 소음이 발생하는 상태입니다.'),
            ('보다', '바라보다', '듣다', '쳐다보다', 2, '듣다는 귀로 하는 행동입니다.'),
            ('부드럽다', '매끄럽다', '푹신하다', '딱딱하다', 3, '딱딱하다는 질감이 굳고 단단합니다.'),
            ('항상', '늘', '절대', '언제나', 2, '절대는 빈도가 전혀 없음을 의미합니다.'),
            ('당기다', '밀다', '누르다', '찌르다', 0, '당기다는 몸 쪽으로 끌어오는 동작입니다.'),
            ('슬프다', '기쁘다', '즐겁다', '신나다', 0, '슬프다는 부정적인 감정입니다.'),
            ('조금', '매우', '아주', '몹시', 0, '조금은 정도가 약함을 의미하는 부사입니다.'),
            ('속삭이다', '춤추다', '부르다', '외치다', 1, '춤추다는 몸을 쓰는 동작이고 나머지는 목소리를 냅니다.'),
            ('달다', '짜다', '시다', '시끄럽다', 3, '시끄럽다는 청각적 느낌이고 나머지는 미각입니다.'),
            ('웃다', '울다', '흐느끼다', '슬퍼하다', 0, '웃다는 기쁠 때 하는 행동입니다.'),
            ('안전하게', '위험하게', '조심스럽게', '신중하게', 1, '위험하게는 조심성이나 안전이 없는 상태입니다.'),
            ('낮다', '높다', '길다', '크다', 0, '낮다는 높이나 길이가 반대되는 개념입니다.'),
            ('어둡다', '밝다', '환하다', '눈부시다', 0, '어둡다는 빛이 없는 상태입니다.'),
            ('침묵하다', '말하다', '얘기하다', '떠들다', 0, '침묵하다는 소리를 내지 않는 행동입니다.'),
            ('열다', '닫다', '풀다', '벗다', 1, '닫다는 무언가를 막거나 가리는 행동입니다.'),
            ('뾰족하다', '둥글다', '동그랗다', '원만하다', 0, '뾰족하다는 끝이 날카로운 상태를 묘사합니다.'),
            ('얼다', '녹다', '풀리다', '흐르다', 0, '얼다는 액체가 굳어지는 현상입니다.'),
            ('마르다', '축축하다', '젖다', '습하다', 0, '마르다는 물기가 없는 상태입니다.'),
            ('씻다', '닦다', '청소하다', '더럽히다', 3, '더럽히다는 깨끗하지 않게 만드는 동작입니다.'),
            ('약하다', '강하다', '세다', '튼튼하다', 0, '약하다는 힘이나 내구성이 부족함을 의미합니다.'),
            ('일하다', '놀다', '쉬다', '즐기다', 0, '일하다는 노동을 의미하며 나머지는 휴식이나 오락입니다.'),
            ('가볍다', '무겁다', '경쾌하다', '홀가분하다', 1, '무겁다는 무게나 느낌이 크게 나가는 상태입니다.'),
            ('잡다', '쥐다', '움켜쥐다', '놓다', 3, '놓다는 손에서 벗어나게 하는 동작입니다.'),
            ('가져오다', '밀어내다', '쫓아내다', '버리다', 0, '가져오다는 자신에게로 향하는 동작입니다.'),
        ],
    },
    {
        'title': '한국어 – 어려운 문제 (TOPIK II)',
        'description': '시험에 자주 출제되는 중고급 동사, 형용사, 부사입니다.',
        'language': 'ko',
        'questions': [
            ('분석하다', '평가하다', '무시하다', '검토하다', 2, '무시하다는 신경 쓰지 않는다는 뜻이고, 나머지는 자세히 살펴보는 행동입니다.'),
            ('감소하다', '증가하다', '늘어나다', '확대되다', 0, '감소하다는 줄어듦을 의미하고 나머지는 커지거나 많아짐을 뜻합니다.'),
            ('정확히', '뚜렷하게', '명확히', '모호하게', 3, '모호하게는 흐릿하거나 확실하지 않음을 의미합니다.'),
            ('중요하다', '사소하다', '필수적이다', '중대하다', 1, '사소하다는 중요하지 않고 작음을 뜻합니다.'),
            ('창조하다', '파괴하다', '훼손하다', '망치다', 0, '창조하다는 새로 만든다는 뜻이고 나머지는 부수거나 상하게 하는 행동입니다.'),
            ('서서히', '신속히', '빠르게', '급격히', 0, '서서히는 속도가 느림을 뜻합니다.'),
            ('개선하다', '향상시키다', '악화시키다', '발전시키다', 2, '악화시키다는 더 나쁘게 만든다는 의미입니다.'),
            ('복잡하다', '단순하다', '까다롭다', '난해하다', 1, '단순하다는 얽히지 않고 쉬움을 의미합니다.'),
            ('빈번하게', '드물게', '자주', '종종', 1, '드물게는 어쩌다 한 번씩 일어난다는 의미입니다.'),
            ('수용하다', '거절하다', '거부하다', '반대하다', 0, '수용하다는 받아들인다는 뜻입니다.'),
            ('영구적이다', '일시적이다', '지속적이다', '끊임없다', 1, '일시적이다는 짧은 시간 동안만 유지됨을 의미합니다.'),
            ('분리하다', '연결하다', '이어지다', '결합하다', 0, '분리하다는 따로 떨어지게 만든다는 뜻입니다.'),
            ('명확하게', '뚜렷하게', '애매하게', '분명하게', 2, '애매하게는 뜻이나 경계가 확실하지 않음을 의미합니다.'),
            ('안정되다', '변동하다', '변화하다', '달라지다', 0, '안정되다는 바뀌지 않고 평안함을 유지하는 상태입니다.'),
            ('충분하다', '넉넉하다', '부족하다', '풍부하다', 2, '부족하다는 모자람을 의미합니다.'),
            ('얻다', '획득하다', '잃다', '취득하다', 2, '잃다는 가지고 있던 것을 없애게 됨을 뜻합니다.'),
            ('전통적이다', '현대적이다', '최신이다', '새롭다', 0, '전통적이다는 과거로부터 이어져 오는 것을 의미합니다.'),
            ('고의로', '의도적으로', '실수로', '일부러', 2, '실수로는 뜻하지 않게 잘못을 저질렀음을 뜻합니다.'),
            ('방해하다', '촉진하다', '장려하다', '지원하다', 0, '방해하다는 남의 일을 못하게 막는 행동입니다.'),
            ('효율적이다', '무의미하다', '효과적이다', '생산적이다', 1, '무의미하다는 아무런 가치나 뜻이 없음을 의미합니다.'),
            ('숨기다', '드러내다', '감추다', '덮다', 1, '드러내다는 보이지 않던 것을 보이게 만든다는 뜻입니다.'),
            ('엄격하다', '철저하다', '관대하다', '단호하다', 2, '관대하다는 마음이 넓고 이해심이 많음을 뜻합니다.'),
            ('포기하다', '유지하다', '보존하다', '지키다', 0, '포기하다는 하던 일을 중간에 그만둔다는 뜻입니다.'),
            ('의무적이다', '강제적이다', '자발적이다', '필수적이다', 2, '자발적이다는 스스로 원해서 한다는 의미입니다.'),
            ('증명하다', '예측하다', '전망하다', '예상하다', 0, '증명하다는 증거를 들어 밝히는 것이고 나머지는 앞날을 미리 추측하는 행동입니다.'),
            ('풍부하다', '희귀하다', '넉넉하다', '많다', 1, '희귀하다는 드물고 구하기 어려움을 의미합니다.'),
            ('조사하다', '방치하다', '검사하다', '관찰하다', 1, '방치하다는 내버려 둔다는 뜻이고 나머지는 주의 깊게 살펴보는 행동입니다.'),
            ('점진적으로', '서서히', '천천히', '갑자기', 3, '갑자기는 예상치 못한 순간에 빠르게 일어남을 뜻합니다.'),
            ('건설하다', '세우다', '만들다', '철거하다', 3, '철거하다는 세워진 것을 무너뜨려 없앤다는 의미입니다.'),
            ('동일하다', '비슷하다', '유사하다', '다르다', 3, '다르다는 서로 같지 않음을 뜻합니다.'),
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed Odd-One-Out packs with English (IELTS) and Korean (TOPIK) questions with randomized correct answers.'

    def handle(self, *args, **options):
        user = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not user:
            self.stderr.write('No users found. Create a superuser first.')
            return

        total_packs = total_qs = 0

        for pack_data in PACKS:
            pack, created = OddOneOutPack.objects.get_or_create(
                title=pack_data['title'],
                defaults={
                    'description': pack_data['description'],
                    'language':    pack_data['language'],
                    'created_by':  user,
                    'is_active':   True,
                },
            )
            if not created:
                self.stdout.write(f'  skip (exists): {pack.title}')
                continue

            total_packs += 1
            for order, q in enumerate(pack_data['questions']):
                w1, w2, w3, w4, odd_idx, expl = q
                OddOneOutQuestion.objects.create(
                    pack=pack,
                    word_1=w1, word_2=w2, word_3=w3, word_4=w4,
                    odd_index=odd_idx,
                    explanation=expl,
                    order=order,
                )
                total_qs += 1

            self.stdout.write(self.style.SUCCESS(
                f'  created: {pack.title} ({len(pack_data["questions"])} questions)'
            ))

        self.stdout.write(self.style.SUCCESS(
            f'Done — {total_packs} pack(s), {total_qs} question(s) created.'
        ))