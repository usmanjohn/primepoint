from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from games.models import WordOrderChallenge


SENTENCES = [
    # ── English – Easy ──────────────────────────────────────────────────────
    {
        'title': 'EN-Easy-01',
        'sentence': 'The young student reads interesting books every day.',
        'hint': 'Subject + verb + object + time expression',
    },
    {
        'title': 'EN-Easy-02',
        'sentence': 'She quickly finished her delicious breakfast this morning.',
        'hint': 'Adverb modifies the verb; possessive + adjective before noun',
    },
    {
        'title': 'EN-Easy-03',
        'sentence': 'The tall teacher explains difficult concepts very clearly.',
        'hint': 'Adjective before noun; adverb phrase at the end',
    },
    {
        'title': 'EN-Easy-04',
        'sentence': 'We always eat healthy food at home.',
        'hint': 'Frequency adverb goes between subject and main verb',
    },
    {
        'title': 'EN-Easy-05',
        'sentence': 'The small cat sleeps quietly on the warm blanket.',
        'hint': 'Adjective + noun, manner adverb, prepositional phrase',
    },
    {
        'title': 'EN-Easy-06',
        'sentence': 'He carefully writes important notes in his notebook.',
        'hint': 'Manner adverb before verb; adjective + noun',
    },
    {
        'title': 'EN-Easy-07',
        'sentence': 'The beautiful flowers grow naturally in the garden.',
        'hint': 'Adjective before noun; adverb after verb',
    },
    {
        'title': 'EN-Easy-08',
        'sentence': 'They often visit their elderly parents on weekends.',
        'hint': 'Frequency adverb before main verb; adjective before noun',
    },
    {
        'title': 'EN-Easy-09',
        'sentence': 'The busy city streets are always very noisy.',
        'hint': 'Multiple adjectives; intensifier + adjective at the end',
    },
    {
        'title': 'EN-Easy-10',
        'sentence': 'She speaks English fluently and confidently.',
        'hint': 'Two coordinated manner adverbs at the end',
    },
    {
        'title': 'EN-Easy-11',
        'sentence': 'The friendly old man walks slowly along the quiet road.',
        'hint': 'Two adjectives before noun; manner adverb + prepositional phrase',
    },
    {
        'title': 'EN-Easy-12',
        'sentence': 'My younger sister studies very hard every evening.',
        'hint': 'Possessive + comparative adjective; intensifier + adverb + time',
    },
    # ── English – Medium ─────────────────────────────────────────────────────
    {
        'title': 'EN-Med-01',
        'sentence': 'The diligent students consistently achieve excellent academic results.',
        'hint': 'Adjective before noun; frequency adverb before verb; two-word noun phrase',
    },
    {
        'title': 'EN-Med-02',
        'sentence': 'Modern technology has significantly changed our daily communication habits.',
        'hint': 'Adjective + noun as subject; adverb in present-perfect clause',
    },
    {
        'title': 'EN-Med-03',
        'sentence': 'The experienced professor carefully analyzes each complex problem thoroughly.',
        'hint': 'Two adverbs frame the verb; adjective before noun in object',
    },
    {
        'title': 'EN-Med-04',
        'sentence': 'Regular exercise is extremely beneficial for both physical and mental health.',
        'hint': 'Intensifier + adjective; coordinated adjectives before noun',
    },
    {
        'title': 'EN-Med-05',
        'sentence': 'She politely but firmly declined the unexpected job offer yesterday.',
        'hint': 'Coordinated adverbs before verb; adjective before compound noun',
    },
    {
        'title': 'EN-Med-06',
        'sentence': 'The ancient historical monument was carefully restored by skilled craftsmen.',
        'hint': 'Two adjectives before noun; passive voice with manner adverb',
    },
    {
        'title': 'EN-Med-07',
        'sentence': 'Many international students successfully adapt to a completely different academic environment.',
        'hint': 'Adjective before noun; adverb before verb; intensifier + adjective',
    },
    {
        'title': 'EN-Med-08',
        'sentence': 'A well-balanced diet greatly contributes to long-term overall health improvement.',
        'hint': 'Compound adjective before noun; adverb before verb; hyphenated adjective',
    },
    {
        'title': 'EN-Med-09',
        'sentence': 'The innovative company recently developed a highly efficient production method.',
        'hint': 'Adjective + noun; time adverb; intensifier + adjective + compound noun',
    },
    {
        'title': 'EN-Med-10',
        'sentence': 'The passionate researcher persistently conducted numerous experiments before reaching a conclusion.',
        'hint': 'Adjective + noun; adverb before verb; adjective + noun; gerund clause',
    },
    {
        'title': 'EN-Med-11',
        'sentence': 'Surprisingly few students correctly answered the unexpectedly difficult exam question.',
        'hint': 'Intensifier + adjective; adverb before verb; adverb + adjective before noun',
    },
    {
        'title': 'EN-Med-12',
        'sentence': 'The newly appointed director immediately introduced several important policy changes.',
        'hint': 'Participial adjective; time adverb; numeral adjective; two adjectives before noun',
    },
    # ── English – Hard / Academic ────────────────────────────────────────────
    {
        'title': 'EN-Hard-01',
        'sentence': 'The researchers systematically analyzed the previously collected empirical data.',
        'hint': 'Adverb before verb; adverb + participial adjective before noun',
    },
    {
        'title': 'EN-Hard-02',
        'sentence': 'Extensive globalization has significantly influenced contemporary cultural identities worldwide.',
        'hint': 'Adjective + noun subject; adverb in present perfect; two adjectives before noun; place adverb',
    },
    {
        'title': 'EN-Hard-03',
        'sentence': 'Socioeconomic inequality inevitably affects educational opportunities across diverse communities.',
        'hint': 'Compound adjective; frequency adverb; adjective before noun; preposition + adjective + noun',
    },
    {
        'title': 'EN-Hard-04',
        'sentence': 'Continuous technological advancement has fundamentally altered traditional manufacturing processes globally.',
        'hint': 'Two adjectives before noun; adverb in present perfect; adjective + compound noun; adverb at end',
    },
    {
        'title': 'EN-Hard-05',
        'sentence': 'The critically acclaimed documentary thoroughly examines widespread environmental degradation issues.',
        'hint': 'Adverb + participial adjective; adverb before verb; adjective + compound noun phrase',
    },
    {
        'title': 'EN-Hard-06',
        'sentence': 'Comprehensive policy reforms are urgently needed to effectively address systemic inequality.',
        'hint': 'Adjective + compound noun; adverb before adjective; infinitive with adverb; adjective + noun',
    },
    {
        'title': 'EN-Hard-07',
        'sentence': 'The rapidly evolving digital landscape poses significant challenges to established media organizations.',
        'hint': 'Adverb + gerund + adjective; adjective + noun; adjective + compound noun',
    },
    {
        'title': 'EN-Hard-08',
        'sentence': 'Sustained academic achievement requires disciplined study habits and intrinsic motivation.',
        'hint': 'Participial adjective; two coordinated noun phrases each with an adjective',
    },
    {
        'title': 'EN-Hard-09',
        'sentence': 'The gradually increasing frequency of extreme weather events strongly suggests climate change.',
        'hint': 'Adverb + gerund before noun; adjective + noun + noun; adverb before verb',
    },
    {
        'title': 'EN-Hard-10',
        'sentence': 'Academically rigorous peer review processes ensure the scientific integrity of published research.',
        'hint': 'Adverb + adjective; compound noun; adjective + noun; participial adjective',
    },
    {
        'title': 'EN-Hard-11',
        'sentence': 'The profoundly influential philosopher eloquently articulated complex existential questions throughout his career.',
        'hint': 'Adverb + adjective; manner adverb before verb; two adjectives before noun; prepositional phrase',
    },
    {
        'title': 'EN-Hard-12',
        'sentence': 'Remarkably innovative solutions are constantly emerging from dynamic collaborative research environments.',
        'hint': 'Adverb + adjective; adverb in present progressive; two adjectives before noun',
    },
    {
        'title': 'EN-Hard-13',
        'sentence': 'The deliberately ambiguous political statement carefully avoided addressing the genuinely controversial issue.',
        'hint': 'Adverb + adjective; adjective + noun; adverb before verb; adverb + adjective before noun',
    },

    # ── Korean – Easy ────────────────────────────────────────────────────────
    {
        'title': 'KO-Easy-01',
        'sentence': '학생들은 매일 도서관에서 열심히 공부합니다.',
        'hint': '주어 + 시간 부사 + 장소 + 방법 부사 + 동사',
    },
    {
        'title': 'KO-Easy-02',
        'sentence': '그녀는 아침마다 건강한 음식을 빠르게 먹습니다.',
        'hint': '시간 표현 + 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-03',
        'sentence': '키가 큰 선생님은 어려운 내용을 천천히 설명합니다.',
        'hint': '관형절 + 주어 + 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-04',
        'sentence': '우리는 주말에 자주 공원에서 즐겁게 산책합니다.',
        'hint': '시간 + 빈도 부사 + 장소 + 방법 부사 + 동사',
    },
    {
        'title': 'KO-Easy-05',
        'sentence': '작은 고양이가 따뜻한 담요 위에서 조용히 잡니다.',
        'hint': '형용사 + 주어 + 형용사 + 장소 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-06',
        'sentence': '그는 중요한 내용을 노트에 꼼꼼히 적습니다.',
        'hint': '형용사 + 목적어 + 장소 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-07',
        'sentence': '예쁜 꽃들이 정원에서 자연스럽게 자랍니다.',
        'hint': '형용사 + 주어 + 장소 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-08',
        'sentence': '그들은 주말마다 연로한 부모님을 자주 방문합니다.',
        'hint': '시간 표현 + 형용사 + 목적어 + 빈도 부사 + 동사',
    },
    {
        'title': 'KO-Easy-09',
        'sentence': '도심의 거리는 항상 매우 시끄럽습니다.',
        'hint': '주어 + 빈도 부사 + 강조 부사 + 형용사',
    },
    {
        'title': 'KO-Easy-10',
        'sentence': '그녀는 영어를 매우 유창하고 자신감 있게 말합니다.',
        'hint': '목적어 + 강조 부사 + 두 개의 부사 + 동사',
    },
    {
        'title': 'KO-Easy-11',
        'sentence': '친절한 할아버지는 조용한 길을 따라 천천히 걷습니다.',
        'hint': '형용사 + 주어 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Easy-12',
        'sentence': '내 여동생은 매우 열심히 매일 저녁 공부합니다.',
        'hint': '소유 + 주어 + 강조 부사 + 부사 + 시간 표현 + 동사',
    },
    # ── Korean – Medium ──────────────────────────────────────────────────────
    {
        'title': 'KO-Med-01',
        'sentence': '성실한 학생들은 꾸준히 뛰어난 학업 성과를 거둡니다.',
        'hint': '형용사 + 주어 + 부사 + 형용사 + 명사 + 동사',
    },
    {
        'title': 'KO-Med-02',
        'sentence': '현대 기술은 우리의 일상적인 소통 방식을 크게 바꾸었습니다.',
        'hint': '형용사 + 주어 + 소유 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-03',
        'sentence': '경험 많은 교수는 각각의 복잡한 문제를 꼼꼼히 분석합니다.',
        'hint': '관형어 + 주어 + 각각의 + 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-04',
        'sentence': '규칙적인 운동은 신체적, 정신적 건강에 매우 유익합니다.',
        'hint': '형용사 + 주어 + 두 개의 형용사 + 명사 + 강조 부사 + 형용사',
    },
    {
        'title': 'KO-Med-05',
        'sentence': '그녀는 어제 예상치 못한 취업 제안을 정중하지만 단호하게 거절했습니다.',
        'hint': '시간 부사 + 형용사 + 명사 + 두 개의 부사 + 동사',
    },
    {
        'title': 'KO-Med-06',
        'sentence': '오래된 역사적 기념물이 숙련된 장인들에 의해 세심하게 복원되었습니다.',
        'hint': '두 형용사 + 주어 + 형용사 + 행위자 + 부사 + 피동 동사',
    },
    {
        'title': 'KO-Med-07',
        'sentence': '많은 유학생들이 완전히 다른 학업 환경에 성공적으로 적응합니다.',
        'hint': '형용사 + 주어 + 강조 부사 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-08',
        'sentence': '균형 잡힌 식단은 장기적인 전반적 건강 개선에 크게 기여합니다.',
        'hint': '복합 형용사 + 주어 + 두 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-09',
        'sentence': '그 혁신적인 회사는 최근 매우 효율적인 생산 방법을 개발했습니다.',
        'hint': '형용사 + 주어 + 시간 부사 + 강조 부사 + 형용사 + 명사 + 동사',
    },
    {
        'title': 'KO-Med-10',
        'sentence': '열정적인 연구자는 결론에 도달하기 전에 수많은 실험을 끈질기게 수행했습니다.',
        'hint': '형용사 + 주어 + 명사절 + 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-11',
        'sentence': '놀랍도록 적은 학생들이 예상보다 어려운 시험 문제에 정확하게 답했습니다.',
        'hint': '강조 부사 + 형용사 + 주어 + 비교 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Med-12',
        'sentence': '새로 임명된 원장님은 즉시 몇 가지 중요한 정책 변경을 도입했습니다.',
        'hint': '부사 + 형용사 + 주어 + 시간 부사 + 형용사 + 명사 + 동사',
    },
    # ── Korean – Hard / Academic ─────────────────────────────────────────────
    {
        'title': 'KO-Hard-01',
        'sentence': '연구자들은 이전에 수집된 경험적 데이터를 체계적으로 분석했습니다.',
        'hint': '주어 + 부사 + 형용사 + 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-02',
        'sentence': '광범위한 세계화는 전 세계 현대 문화 정체성에 크게 영향을 미쳤습니다.',
        'hint': '형용사 + 주어 + 장소 부사 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-03',
        'sentence': '사회경제적 불평등은 다양한 공동체의 교육 기회에 필연적으로 영향을 미칩니다.',
        'hint': '복합 형용사 + 주어 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-04',
        'sentence': '지속적인 기술 발전이 전 세계 전통적인 제조 공정을 근본적으로 변화시켰습니다.',
        'hint': '형용사 + 주어 + 장소 부사 + 형용사 + 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-05',
        'sentence': '비평가들에게 극찬 받은 다큐멘터리는 광범위한 환경 훼손 문제를 철저히 검토합니다.',
        'hint': '관형절 + 주어 + 형용사 + 복합 명사 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-06',
        'sentence': '체계적인 불평등을 효과적으로 해결하기 위해서는 포괄적인 정책 개혁이 시급히 필요합니다.',
        'hint': '형용사 + 목적어 + 부사 + 동사 + 조건절 + 형용사 + 명사 + 부사 + 형용사',
    },
    {
        'title': 'KO-Hard-07',
        'sentence': '빠르게 진화하는 디지털 환경은 기존 미디어 조직에 중요한 도전을 제기합니다.',
        'hint': '부사 + 동명사 + 형용사 + 주어 + 형용사 + 명사 + 형용사 + 목적어 + 동사',
    },
    {
        'title': 'KO-Hard-08',
        'sentence': '지속적인 학업 성취는 규율적인 학습 습관과 내재적 동기를 필요로 합니다.',
        'hint': '형용사 + 주어 + 두 개의 형용사 + 명사 + 동사',
    },
    {
        'title': 'KO-Hard-09',
        'sentence': '극단적인 기상 이변의 점진적으로 증가하는 빈도는 기후 변화를 강하게 시사합니다.',
        'hint': '형용사 + 명사 + 부사 + 형용사 + 주어 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-10',
        'sentence': '학문적으로 엄격한 동료 심사 과정은 발표된 연구의 과학적 무결성을 보장합니다.',
        'hint': '부사 + 형용사 + 복합 명사 + 주어 + 형용사 + 명사 + 동사',
    },
    {
        'title': 'KO-Hard-11',
        'sentence': '깊이 영향력 있는 철학자는 경력 전반에 걸쳐 복잡한 실존적 질문을 명쾌하게 표현했습니다.',
        'hint': '부사 + 형용사 + 주어 + 시간 표현 + 두 형용사 + 목적어 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-12',
        'sentence': '역동적인 협력적 연구 환경에서 놀랍도록 혁신적인 해결책이 끊임없이 등장합니다.',
        'hint': '두 형용사 + 장소 + 강조 부사 + 형용사 + 주어 + 부사 + 동사',
    },
    {
        'title': 'KO-Hard-13',
        'sentence': '의도적으로 모호한 정치적 발언은 진정으로 논란이 있는 문제를 신중하게 피했습니다.',
        'hint': '부사 + 형용사 + 형용사 + 주어 + 부사 + 형용사 + 목적어 + 부사 + 동사',
    },
]


class Command(BaseCommand):
    help = 'Seed WordOrderChallenge with English and Korean sentences (mixed difficulty).'

    def handle(self, *args, **options):
        user = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not user:
            self.stderr.write('No users found. Create a superuser first.')
            return

        created_count = skipped_count = 0

        for data in SENTENCES:
            _, created = WordOrderChallenge.objects.get_or_create(
                title=data['title'],
                defaults={
                    'sentence':    data['sentence'],
                    'hint':        data['hint'],
                    'created_by':  user,
                    'is_active':   True,
                },
            )
            if created:
                created_count += 1
            else:
                skipped_count += 1
                self.stdout.write(f'  skip (exists): {data["title"]}')

        self.stdout.write(self.style.SUCCESS(
            f'Done — {created_count} sentence(s) created, {skipped_count} skipped.'
        ))
