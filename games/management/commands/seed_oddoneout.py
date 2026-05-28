from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from games.models import OddOneOutPack, OddOneOutQuestion


PACKS = [
    {
        'title': 'English – Easy',
        'description': 'Basic vocabulary: spot the word that does not belong.',
        'language': 'en',
        'questions': [
            ('Apple', 'Banana', 'Orange', 'Chair',    3, 'Chair is furniture, not a fruit.'),
            ('Red',   'Blue',   'Table',  'Yellow',   2, 'Table is furniture, not a colour.'),
            ('Dog',   'Cat',    'Book',   'Horse',    2, 'Book is not an animal.'),
            ('Spring','Summer', 'Monday', 'Winter',   2, 'Monday is a weekday, not a season.'),
            ('Monday','Tuesday','January','Thursday', 2, 'January is a month, not a weekday.'),
            ('Car',   'Bus',    'Train',  'Chair',    3, 'Chair is not a means of transport.'),
            ('Hand',  'Foot',   'Eye',    'Apple',    3, 'Apple is not a body part.'),
            ('Carrot','Potato', 'Lion',   'Tomato',   2, 'Lion is an animal, not a vegetable.'),
            ('One',   'Two',    'Three',  'Blue',     3, 'Blue is a colour, not a number.'),
            ('Pencil','Book',   'Eraser', 'Banana',   3, 'Banana is not school stationery.'),
            ('Shirt', 'Pants',  'Shoes',  'Table',    3, 'Table is not clothing.'),
            ('Rain',  'Snow',   'Sun',    'Dog',      3, 'Dog is not a weather condition.'),
            ('Mother','Father', 'Sister', 'Pencil',   3, 'Pencil is not a family member.'),
            ('France','Japan',  'Brazil', 'Carrot',   3, 'Carrot is not a country.'),
            ('Mars',  'Venus',  'Earth',  'River',    3, 'River is not a planet.'),
            ('Tiger', 'Lion',   'Leopard','Shark',    3, 'Shark lives in water; others are land big cats.'),
            ('Doctor','Teacher','Pilot',  'Hospital', 3, 'Hospital is a place, not a profession.'),
            ('Rose',  'Tulip',  'Daisy',  'Oak',      3, 'Oak is a tree, not a flower.'),
            ('Piano', 'Guitar', 'Violin', 'Hammer',   3, 'Hammer is a tool, not a musical instrument.'),
            ('Kitchen','Bedroom','Bathroom','Garden', 3, 'Garden is outside, not a room inside a house.'),
        ],
    },
    {
        'title': 'English – Hard',
        'description': 'Tricky categories: grammar, science, culture, and more.',
        'language': 'en',
        'questions': [
            ('Run',       'Jump',     'Swim',      'Beautiful',  3, 'Beautiful is an adjective; the others are verbs.'),
            ('Shakespeare','Dickens', 'Newton',    'Hemingway',  2, 'Newton was a scientist; the others are novelists.'),
            ('Piano',     'Guitar',   'Violin',    'Drum',       3, 'Drum is a percussion instrument; the others have strings.'),
            ('Mercury',   'Venus',    'Earth',     'Moon',       3, "Moon is Earth's satellite, not a planet."),
            ('Lion',      'Tiger',    'Leopard',   'Wolf',       3, 'Wolf is a canine; the others are big cats.'),
            ('Paris',     'Rome',     'London',    'Alps',       3, 'Alps is a mountain range, not a capital city.'),
            ('Copper',    'Gold',     'Silver',    'Diamond',    3, 'Diamond is a mineral; the others are metals.'),
            ('Quickly',   'Softly',   'Angry',     'Quietly',    2, 'Angry is an adjective; the others are adverbs.'),
            ('Amazon',    'Nile',     'Sahara',    'Mississippi',2, 'Sahara is a desert, not a river.'),
            ('Beethoven', 'Mozart',   'Picasso',   'Bach',       2, 'Picasso was a painter; the others were composers.'),
            ('Hydrogen',  'Oxygen',   'Nitrogen',  'Gold',       3, 'Gold is a metal; the others are gases at room temperature.'),
            ('Triangle',  'Circle',   'Square',    'Cube',       3, 'Cube is 3-dimensional; the others are 2D shapes.'),
            ('Comedy',    'Tragedy',  'Biography', 'Drama',      2, 'Biography is non-fiction; the others are dramatic genres.'),
            ('Knee',      'Elbow',    'Wrist',     'Chin',       3, 'Chin is not a joint.'),
            ('Maple',     'Oak',      'Pine',      'Rose',       3, 'Rose is a flower; the others are trees.'),
            ('Omnivore',  'Herbivore','Carnivore', 'Predator',   3, 'Predator describes a hunting role, not a diet category.'),
            ('Simile',    'Metaphor', 'Alliteration','Noun',     3, 'Noun is a word class; the others are literary devices.'),
            ('Mitosis',   'Meiosis',  'Osmosis',   'Photosynthesis',3,'Photosynthesis is a plant process; the others involve cell division or water movement.'),
            ('Renaissance','Baroque', 'Jazz',      'Romanticism',2, 'Jazz is a music genre; the others are art/cultural movements.'),
            ('Equator',   'Tropic',   'Meridian',  'Archipelago',3, 'Archipelago is a geographic landform; the others are imaginary lines on maps.'),
        ],
    },
    {
        'title': '한국어 – 쉬운 문제',
        'description': '기본 어휘: 나머지 셋과 다른 단어를 고르세요.',
        'language': 'ko',
        'questions': [
            ('사과',   '바나나',  '포도',    '의자',    3, '의자는 가구이고, 나머지는 과일입니다.'),
            ('빨간색', '파란색',  '책상',    '노란색',  2, '책상은 가구이고, 나머지는 색깔입니다.'),
            ('개',     '고양이',  '책',      '말',      2, '책은 사물이고, 나머지는 동물입니다.'),
            ('봄',     '여름',    '월요일',  '겨울',    2, '월요일은 요일이고, 나머지는 계절입니다.'),
            ('월요일', '화요일',  '1월',     '목요일',  2, '1월은 달 이름이고, 나머지는 요일입니다.'),
            ('자동차', '버스',    '기차',    '의자',    3, '의자는 교통수단이 아닙니다.'),
            ('손',     '발',      '눈',      '사과',    3, '사과는 신체 부위가 아닙니다.'),
            ('당근',   '감자',    '사자',    '토마토',  2, '사자는 동물이고, 나머지는 채소입니다.'),
            ('하나',   '둘',      '셋',      '파랑',    3, '파랑은 색깔이고, 나머지는 숫자입니다.'),
            ('연필',   '책',      '지우개',  '바나나',  3, '바나나는 학용품이 아닙니다.'),
            ('셔츠',   '바지',    '신발',    '책상',    3, '책상은 의류가 아닙니다.'),
            ('비',     '눈',      '햇빛',    '개',      3, '개는 날씨 현상이 아닙니다.'),
            ('어머니', '아버지',  '언니',    '연필',    3, '연필은 가족 구성원이 아닙니다.'),
            ('프랑스', '일본',    '브라질',  '당근',    3, '당근은 나라가 아닙니다.'),
            ('화성',   '금성',    '지구',    '강',      3, '강은 행성이 아닙니다.'),
            ('호랑이', '사자',    '표범',    '상어',    3, '상어는 수중 생물이고, 나머지는 육상 맹수입니다.'),
            ('의사',   '선생님',  '조종사',  '병원',    3, '병원은 장소이고, 나머지는 직업입니다.'),
            ('장미',   '튤립',    '데이지',  '참나무',  3, '참나무는 나무이고, 나머지는 꽃입니다.'),
            ('피아노', '기타',    '바이올린','망치',    3, '망치는 악기가 아닌 도구입니다.'),
            ('부엌',   '침실',    '욕실',    '정원',    3, '정원은 실내 공간이 아닙니다.'),
        ],
    },
    {
        'title': '한국어 – 어려운 문제',
        'description': '문법, 과학, 문화 등 심화 어휘로 도전하세요.',
        'language': 'ko',
        'questions': [
            ('달리다',   '뛰다',    '수영하다',  '아름답다',  3, '아름답다는 형용사이고, 나머지는 동사입니다.'),
            ('세종대왕', '이순신',  '뉴턴',      '유관순',    2, '뉴턴은 외국 과학자이고, 나머지는 한국 역사 인물입니다.'),
            ('피아노',   '기타',    '바이올린',  '북',        3, '북은 타악기이고, 나머지는 현악기입니다.'),
            ('수성',     '금성',    '지구',      '달',        3, '달은 위성이고, 나머지는 행성입니다.'),
            ('사자',     '호랑이',  '표범',      '늑대',      3, '늑대는 개과이고, 나머지는 고양이과입니다.'),
            ('서울',     '도쿄',    '베이징',    '알프스',    3, '알프스는 산맥이고, 나머지는 도시입니다.'),
            ('구리',     '금',      '은',        '다이아몬드',3, '다이아몬드는 광물이고, 나머지는 금속입니다.'),
            ('빠르게',   '조용히',  '화나다',    '조심스럽게',2, '화나다는 동사이고, 나머지는 부사입니다.'),
            ('아마존',   '나일강',  '사하라',    '한강',      2, '사하라는 사막이고, 나머지는 강입니다.'),
            ('베토벤',   '모차르트','피카소',    '바흐',      2, '피카소는 화가이고, 나머지는 작곡가입니다.'),
            ('수소',     '산소',    '질소',      '금',        3, '금은 금속이고, 나머지는 상온 기체입니다.'),
            ('삼각형',   '원',      '사각형',    '정육면체',  3, '정육면체는 3차원 도형이고, 나머지는 2차원입니다.'),
            ('코미디',   '비극',    '전기문',    '드라마',    2, '전기문은 논픽션이고, 나머지는 허구 장르입니다.'),
            ('무릎',     '팔꿈치',  '손목',      '턱',        3, '턱은 관절 부위가 아닙니다.'),
            ('단풍나무', '참나무',  '소나무',    '장미',      3, '장미는 꽃이고, 나머지는 나무입니다.'),
            ('직유법',   '은유법',  '두운법',    '명사',      3, '명사는 품사이고, 나머지는 수사법입니다.'),
            ('세포분열', '감수분열','삼투현상',  '광합성',    3, '광합성은 식물 과정이고, 나머지는 세포/물 관련 과정입니다.'),
            ('르네상스', '바로크',  '재즈',      '낭만주의',  2, '재즈는 음악 장르이고, 나머지는 예술·문화 사조입니다.'),
            ('적도',     '북회귀선','본초자오선','군도',      3, '군도는 지리적 지형이고, 나머지는 지도 위의 가상선입니다.'),
            ('민주주의', '공화제',  '군주제',    '자본주의',  3, '자본주의는 경제 체제이고, 나머지는 정치 체제입니다.'),
        ],
    },
]


class Command(BaseCommand):
    help = 'Seed Odd-One-Out packs with English and Korean questions (easy + hard).'

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
