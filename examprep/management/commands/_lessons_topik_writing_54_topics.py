# TOPIK II Yozish (쓰기) 54 — mavzu jumlalari (yodlash uchun). Manba: material_54.txt.
# Har mavzu uchun 3–4 tayyor koreyscha jumla + o'zbekcha tarjimasi. 5 mavzudan bir "qism".
# Tarjimalar TRANSLATIONS da (qo'lda). Faqat tarjima qilingan mavzular chiqadi.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_54_topics.py --author=prime
# (yangi mavzular tarjima qilingach --republish bilan qayta import qiling).

import os
import re
import html

_DIR = os.path.dirname(os.path.abspath(__file__))


def _parse_topics(path):
    topics, cur = [], None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            m = re.match(r"^(\d+)[.\t]\s*(.*)$", line)
            if m:
                if cur is not None:
                    cur["sents"].append(m.group(2).strip())
            else:
                cur = {"title": line, "sents": []}
                topics.append(cur)
    return topics


_TOPICS = _parse_topics(os.path.join(_DIR, "material_54.txt"))


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

# Koreyscha sarlavha -> {"uz": mavzu nomi, "s": [har bir jumla tarjimasi]}
TRANSLATIONS = {
    "스마트폰 중독": {
        "uz": "Smartfonga qaramlik",
        "s": [
            "Smartfon bo'lsa bas, istalgan vaqt va joyda telefon, internet va o'yindan foydalanish mumkin.",
            "Smartfon bilan ovora bo'lib, boshqa ishlarga yaxshi diqqat qila olmay qolamiz.",
            "Kerakli ma'lumotni ham smartfon qidiruviga tayanib qolganimiz sababli, xotira zaiflashmasligi mumkin emas.",
        ],
    },
    "글쓰기 능력": {
        "uz": "Yozish qobiliyati",
        "s": [
            "Do'stga xabar yuborish, rasmiy elektron xat yozish kabi biz turli shakldagi matnlar yozamiz,",
            "Yozish qobiliyatini oshirish uchun avvalo kitob o'qish odatini shakllantirish kerak.",
            "Ko'p yozgandagina malaka oshgani uchun, har kuni kundalik yuritish yoki shaxsiy blogga muntazam yozib borish ham yaxshi usul bo'lishi mumkin.",
        ],
    },
    "부탁 거절": {
        "uz": "Iltimosni rad etish",
        "s": [
            "Iltimosni rad etib, yaxshi bo'lgan munosabatlar buzilib ketadigan holatlar ham bo'ladi.",
            "Rad etayotganda, suhbatdoshning qiyin ahvoliga to'liq hamdard ekaningiz va uni tushunayotganingizni ko'rsatish kerak.",
            "Muammoni hal qilish uchun birga bosh qotirganingizni ko'rsata olganingiz sababli, suhbatdoshning ham ko'ngli kamroq og'riydi.",
        ],
    },
    "과소비의 문제점": {
        "uz": "Isrofgarchilikning muammolari",
        "s": [
            "To'satdan baxtsiz hodisaga uchrab yoki kasal bo'lib shifoxona xarajati chiqsa, qarzga botishdan boshqa iloj qolmaydi.",
            "Ko'ngli notinch yoki tushkun bo'lgani uchun beixtiyor isrof qiladiganlar ham, o'zini ko'rsatish yoki e'tibor tortish uchun isrof qiladiganlar ham bor.",
            "Isrofga olib keladigan sabablardan biri sifatida reklamaning ta'sirini keltirish mumkin.",
            "Inson o'zi nega isrof qilayotganining sababini aniq bilgandagina, xarajatni jilovlash yo'lini ham topa oladi.",
        ],
    },
    "바른말 & 의사소통": {
        "uz": "To'g'ri nutq va muloqot",
        "s": [
            "Qanday gapirishga qarab, o'sha odam haqidagi taassurot o'zgarishi mumkin.",
            "Ijtimoiy tarmoqda oson va qulay muloqotga o'rganib, qisqartma so'zlarni tez-tez ishlatgani uchun, qaysi biri to'g'ri so'z ekanini yaxshi bilmaydiganlar ko'paydi.",
            "Rasmiy joylarda moda so'zlar yoki qisqartmalardan qochgan ma'qul.",
        ],
    },
    "시간 관리": {
        "uz": "Vaqtni boshqarish",
        "s": [
            "Tobora tezlashayotgan o'zgarishlar va keskin raqobat ichida, vaqtdan qanday foydalanish inson hayotidagi muvaffaqiyat va muvaffaqiyatsizlikka katta ta'sir qilmoqda.",
            "Vaqtni yaxshi boshqara olmasangiz, keyin afsuslanadigan ishlar ko'payadi.",
            "Vaqtni samarali boshqarish uchun ishlarning ustuvorligini belgilash kerak.",
            "Ishga borib-kelishda yoki birovni kutganda kabi kundalik hayotda ozdan hosil bo'ladigan qisqa vaqtni behuda ketkazmay, o'sha vaqtda bajarsa bo'ladigan ishlarni tayyorlab qilgan yaxshi.",
        ],
    },
    "긍정적은 생각": {
        "uz": "Ijobiy fikrlash",
        "s": [
            "Aslida qiyin vaziyatga tushganda, odam o'zini va sharoitni ayblab, salbiy fikrga berilib ketishi oson.",
            "Ijobiy fikrlasangiz, muvaffaqiyatsiz tajribadan ham o'rganadigan narsa topa olasiz.",
            "Ijobiy fikrlash ruhiy va jismoniy sog'liqqa ham yaxshi ta'sir qiladi.",
            "Katta maqsaddan ko'ra kichik maqsadlarni birma-bir amalga oshirib borsangiz, yutuq hissi ham paydo bo'ladi, o'ziga ishonch ham ortadi.",
        ],
    },
    "좋은 습관": {
        "uz": "Yaxshi odatlar",
        "s": [
            "Yaxshi odat hayotimizga ijobiy ta'sir qiladi.",
            "Odatda odamlar yaxshi odat sifatida erta yotib erta turishni, muntazam sport bilan shug'ullanishni sanashadi.",
            "Avvalo o'z odatlaring orasidan yaxshi va yomon odatni ajratib tahlil qilish kerak.",
            "Yaxshi xatti-harakatni takrorlasang, yaxshi natijaga erishasan.",
        ],
    },
    "갈등": {
        "uz": "Ziddiyat (nizo)",
        "s": [
            "Odamlar iloji boricha ziddiyatdan qochishni istaydi.",
            "Faqat o'z fikrini o'tkazib, suhbatdoshni ayblash yoki umuman gaplashmaslik kabi munosabat ziddiyatni hal qilishga aslo yordam bermaydi.",
            "Suhbatdoshga e'tiborli bo'lib, o'z pozitsiyasidan yon bermaslik mumkin emas.",
        ],
    },
    "감시카메라 설치": {
        "uz": "Kuzatuv kamerasini o'rnatish",
        "s": [
            "Kuzatuv kamerasini o'rnatishdan maqsad jinoyatning oldini olishdir.",
            "Kuzatuv kamerasining muammolaridan biri — shaxsiy hayotga tajovuz qilinishi mumkinligidir.",
            "Bolalar, keksalar, ayollar kabi himoyaga muhtojlarga qarshi jinoyat ortayotgan bir paytda, kuzatuv kamerasi ularning xavotirini kamaytira olishi kabi afzalligi bor.",
        ],
    },
    "외모지상주의": {
        "uz": "Tashqi ko'rinish kultusi",
        "s": [
            "Masalan, suhbatda (intervyuda) qobiliyat emas, tashqi ko'rinish qabul qilinish-qilinmaslikka hal qiluvchi ta'sir ko'rsatishi mumkin.",
            "Boylik va muvaffaqiyatga intiladiganlar ko'paygani sari, faqat ko'zga ko'rinadigan narsani qadrlash tamoyili bu hodisani yanada kuchaytirmoqda.",
            "Ommaviy madaniyat ko'rsatadigan tashqi go'zallikni mezon qilib olsangiz, o'zingizdagi o'ziga xoslikni namoyon qila olmay qolasiz.",
        ],
    },
    "진정한 배움": {
        "uz": "Haqiqiy o'rganish",
        "s": [
            "Bilim qanchalik ko'p bo'lmasin, tez o'zgarayotgan dunyoga moslashish uchun yangidan o'rganish kerak bo'lgan narsa bo'ladi.",
            "O'rgangan sari o'rganish kerak bo'lgan narsa yanada ko'proq ko'rinadi.",
            "Ota-onaning xohishiga ko'ra chet tili o'rganish yoki bitirish uchun imtihonga tayyorlanish — haqiqiy o'rganish emas, balki ehtiyoj yuzasidan qilingan vositadan boshqa narsa emas.",
            "Muntazam biror narsa o'rgansangiz, o'z kamchiliklaringizni to'ldirib, yanada rivojlanib borishingiz mumkin.",
        ],
    },
    "진정한 친구": {
        "uz": "Haqiqiy do'st",
        "s": [
            "Hayotda yolg'iz qoladigan paytlar ham, qiyin paytlar ham ko'p bo'ladi, va har safar do'st yoningda turib madad bo'ladi.",
            "Tez-tez uchrashib, suhbatlashib, hamdardlik qobiliyatini oshirasan va g'amxo'rlik qilishni o'rganasan.",
            "Muloqot yaxshi bo'lmasa, dardni bo'lishish ham qiyin, suhbat zavqini his qilish ham qiyin bo'lib, munosabat chuqurlasha olmaydi.",
        ],
    },
    "기업의 역할": {
        "uz": "Korxonaning (biznesning) roli",
        "s": [
            "Korxonalar texnologiya rivoji orqali yangi mahsulot va xizmatlarni taqdim etadi.",
            "Ko'plab korxonalar shaxs o'zi yarata olmaydigan yoki juda zarur mahsulotlarni ishlab chiqarib taqdim etish orqali hayotni qulay qiladi.",
            "Kambag'al talabalarga stipendiya beradigan yoki turmushi og'ir qo'shnilarga xayriya qiladigan korxonalar ko'paymoqda, ba'zi korxonalar atrof-muhit harakatlarida ham ishtirok etadi.",
            "Korxona jamiyat taraqqiyoti uchun nima qilish kerakligini o'ylab, amalga oshirishi kerak.",
        ],
    },
    "인간관계": {
        "uz": "Insoniy munosabatlar",
        "s": [
            "Ish joyida hamkasblar bilan yaxshi munosabat o'rnata olmasangiz, stressga tushasiz va ishlash qiyinlashishi mumkin.",
            "Xarakter va qadriyatlardagi farq tufayli har bir insonning turmush tarzi har xil bo'ladi.",
            "Biror manfaat olish uchun munosabat o'rnatmoqchi bo'lsangiz yoki har uchrashganda o'zini o'ylab ish tutsangiz, suhbatdoshga zarar yetkazasiz yoki qalbini yaralaysiz.",
        ],
    },
    "건강 유지": {
        "uz": "Sog'liqni saqlash",
        "s": [
            "Ifloslangan muhit va kuchli stress ichida yashaganimiz sababli, sog'lom yashash yanada muhim bo'lib qoldi.",
            "Sog'lig'imizni yo'qotsak, iqtisodiy va ruhiy jihatdan qiyinchilikka duch kelamiz.",
            "Tungi ovqat va ortiqcha ovqatdan qochib, sabzavot va meva kabilarni tez-tez iste'mol qilish sog'liqni saqlashda yordam beradi.",
        ],
    },
    "협업 능력": {
        "uz": "Hamkorlik qobiliyati",
        "s": [
            "Har kimning qobiliyati har xil bo'lgani uchun, har kim o'zi uddalaydigan sohani olib, ishni bo'lib bajarish yanada samaraliroq.",
            "Samarali hamkorlik qilish aslo oson emas.",
            "Albatta, har kimning fikri har xil bo'lgani uchun, fikr farqi paydo bo'lmasligi mumkin emas.",
            "Ishni boshqaga ag'darish yoki muddatni bajarmaslik orqali butun jamoaga zarar yetkazmaslikka ehtiyot bo'lish kerak.",
        ],
    },
    "토론의 역할": {
        "uz": "Munozaraning roli",
        "s": [
            "Munozara orqali biz bir-birimizning fikrimizni eshitib, farqni aniqlash bilan yaxshiroq yo'l topa olamiz.",
            "Munozara orqali yetarlicha muloqot qilgandan so'ng, uning natijasini qabul qilgan ma'qul.",
            "Munozara paytida suhbatdoshning gapini diqqat bilan tinglash har narsadan muhim.",
        ],
    },
    "여행의 역할": {
        "uz": "Sayohatning roli",
        "s": [
            "Sayohat qilsangiz, stressni bartaraf etib, ko'ngil xotirjamligini topa olasiz.",
            "Sayohat qilganda xavfsizlik va sog'liqqa e'tibor berish kerak.",
            "Sayohatga qiziqish bo'lmasa, yangi tajriba va fikrga ega bo'lish imkoniyatini boy berishingiz mumkin.",
            "Mahalliy aholining turmush tarzi va madaniyatini bor holicha qabul qilish kayfiyati kerak.",
        ],
    },
    "창의적인 사고 능력": {
        "uz": "Ijodiy fikrlash qobiliyati",
        "s": [
            "Korxonalar ijodiy fikr orqali yangi mahsulot va xizmat taqdim eta olmasa, iste'molchilarni qoniqtira olmay, raqobatda orqada qolishi mumkin.",
            "Ijodiy fikrlash qobiliyati muammoni samarali hal qilishda ham yordam beradi.",
            "Ijodiy fikrlash uchun avvalo qotib qolgan qarashlarni (stereotiplarni) buzish muhim.",
        ],
    },
    "잘못 후 사과": {
        "uz": "Xatodan keyin uzr so'rash",
        "s": [
            "Xatosini tan olib uzr so'raydigan odam ham, mag'rurligi tufayli uzr so'ramaydigan odam ham bor.",
            "Uzr so'rash — bunday salbiy ehtimolni ijobiyga aylantira oladigan yaxshi imkoniyatdir.",
            "Uzr so'raganda, avvalo bahona qilmasdan, o'z xatosini tan olish munosabati muhim.",
        ],
    },
    "신조어의 장단점": {
        "uz": "Yangi so'zlar (neologizm)ning afzallik va kamchiliklari",
        "s": [
            "Yangi so'zlardan foydalansangiz, oson va tez muloqot qila olasiz.",
            "Jamiyatda yangi so'z ishlatish odatiy holga aylangani sari, vaqti va joyiga mos kelmagan holda yangi so'z ishlatadiganlarning ko'payishi ham muammo.",
            "Biz yangi so'zlarni o'ylamasdan (nazoratsiz) ishlatmaslikka harakat qilishimiz kerak.",
            "Odob talab qilinadigan joylarda yangi so'z ishlatishdan qochish kerak.",
        ],
    },
    "조기 외국어 교육": {
        "uz": "Erta chet tili ta'limi",
        "s": [
            "Ota-onalar chet tili ta'limini erta boshlasa, bola tilni yanada ravon gapira oladigan bo'ladi deb o'ylaydi.",
            "Erta chet tili ta'limi aksincha bolaning til qobiliyatini pasaytirishi mumkin.",
            "Muhimi vaqt emas, harakat, shuning uchun rag'bat paydo bo'lganda bola o'zi mustaqil o'qisa ham, aslo kech emas.",
        ],
    },
    "대중문화의 발달": {
        "uz": "Ommaviy madaniyatning rivoji",
        "s": [
            "Smartfon bo'lsa bas, internet orqali istalgan vaqt va joyda kino ko'rish, musiqa tinglash, hatto kontent yaratishda bevosita ishtirok etish ham mumkin.",
            "Ommaviy madaniyatda zo'ravonlik va shahvoniy mazmun ko'p bo'lishi mumkin, bu esa o'sib kelayotgan bolalarga ayniqsa yomon ta'sir qiladi.",
            "Ommaviy madaniyatning afzalligini saqlab, kamchiligini kamaytirmoqchi bo'lsangiz, uni tanqidiy qabul qila bilish kerak.",
        ],
    },
    "관광 산업의 장단점": {
        "uz": "Turizm sanoatining afzallik va kamchiliklari",
        "s": [
            "Sayyohlar ko'paysa, tegishli ish o'rinlari ortadi va mahalliy aholi daromadi ham oshadi.",
            "Shovqin yoki chiqindi muammosi — turizm sanoatining eng tipik muammosi.",
            "Turizm sanoatining salbiy oqibatlarini oldini olish uchun avvalo mahalliy aholi bilan yetarli muloqot bo'lishi kerak.",
        ],
    },
    "성형수술": {
        "uz": "Plastik jarrohlik",
        "s": [
            "Plastik jarrohlik bilan har kim xohlaganidek tashqi ko'rinishini o'zgartira oladigan bo'ldi.",
            "Plastik jarrohlik qoniqish va o'ziga ishonch olishda yordam beradi.",
            "Plastik jarrohlik qildiradiganlar ko'paysa, jamiyatda tashqi ko'rinishni qadrlash kayfiyati keng tarqalishi mumkin.",
            "Tashqi ko'rinishi tufayli o'ziga ishonchi yo'q yoki ijtimoiy hayotda tez-tez ziyon ko'radigan odam uchun plastik jarrohlik shu muammoni hal qila oladigan yo'l bo'lishi mumkin.",
        ],
    },
    "경쟁의 치열": {
        "uz": "Raqobatning keskinligi",
        "s": [
            "Globallashuv ta'sirida raqobat maydoni yanada kengaymoqda.",
            "Shaxsmi yoki korxonami, jahon bozorida faoliyat yuritishi kerak bo'lgani uchun, taqqoslanadigan raqiblar ko'payib, raqobat yanada keskinlashdi.",
            "Suhbatdoshni hamkorlik obyekti emas, faqat raqobat obyekti sifatida ko'rib, unga ishona olmay qolishadi.",
            "Jarayondan ko'ra faqat natijani qadrlaydigan jamiyatga aylanishi mumkinligi muammo.",
        ],
    },
    "지구 온난화": {
        "uz": "Global isish",
        "s": [
            "Global isish butun dunyo bo'ylab noodatiy iqlim hodisalarini keltirib chiqarmoqda.",
            "Noodatiy iqlim hodisalari davom etsa, yangi kasalliklar paydo bo'libgina qolmay, kelajakda yo'q bo'lib ketadigan hayvonlar ham ko'payadi.",
            "Global isishning oldini olish uchun kundalik hayotda amalga oshirsa bo'ladigan yo'l — energiyani tejash va resurslarni isrof qilmaslik.",
            "Hukumat esa ekologik toza energiya ishlab chiqishga sarmoya kiritishi kerak.",
        ],
    },
    "황금만능주의": {
        "uz": "Pulparastlik (pulni hamma narsadan ustun qo'yish)",
        "s": [
            "Pulparastlikka berilgan odamlar pulni turmush qulayligi uchun vosita emas, maqsad deb biladi.",
            "Eng avvalo ma'naviy qadriyatlarning muhimligini anglab, ichki go'zallikni ko'ra bilishga harakat qilish kerak.",
            "Ommaviy axborot vositalari rivoji tufayli odamlar kuniga son-sanoqsiz reklamaga duch keladi va istalgan vaqtda osongina serial ko'ra oladigan bo'ldi; bunday reklama va seriallar turli yangi mahsulotlarni ko'rsatib, e'tibor tortadi.",
        ],
    },
    "세대 갈등": {
        "uz": "Avlodlar ziddiyati",
        "s": [
            "Yosh avlod keksalarni hurmat qilmaydi, keksalar esa yosh avlodni hurmat qilmaydi.",
            "Siyosiy vaziyat o'zgarib, madaniy did o'zgargani sari, fikrlarda katta farq paydo bo'lmoqda.",
            "Avlodlar ziddiyatini hal qilish uchun bir-birini hurmat qilish kayfiyati bilan muloqot qilishga harakat kerak.",
        ],
    },
    "차별": {
        "uz": "Kamsitish (diskriminatsiya)",
        "s": [
            "Kamsitish qandaydir noto'g'ri qarash (xurofot) bilan odamni baholaganda osongina yuzaga kelishi mumkin.",
            "Asosan jins, ma'lumot kabi jihatlardan biroz ustunroq odam boshqalarni kamsitgani sari, noqulay ahvoldagi odamning ahvoli yanada og'irlashadi.",
            "Kamsitish muammosini yengish uchun xurofotni tashlab, boshqacha bo'lishni (farqni) hurmat qila bilish kerak.",
            "Kamsitishni taqiqlaydigan qonun chiqarish ham yaxshi.",
        ],
    },
    "바람직한 소비": {
        "uz": "Ma'qul (to'g'ri) iste'mol",
        "s": [
            "Ma'qul iste'mol deganda shunchaki narxni emas, balki o'z iste'moli jamiyatga qanday ta'sir qilishini ham hisobga olishni tushunish mumkin.",
            "Oqilona iste'mol qilsangiz, tabiiy ravishda ijtimoiy faoliyatda ham qatnasha olasiz.",
            "Ma'qul iste'mol qilish uchun o'zingiz nimani eng qadrli deb bilishingizni anglashingiz kerak.",
        ],
    },
    "직업 선택": {
        "uz": "Kasb tanlash",
        "s": [
            "Kasb bo'lsagina pul topib, tirikchilikni ta'minlash mumkin.",
            "Kasbni yaxshi tanlash uchun, birinchidan, moyillikni (qobiliyatni) o'ylash kerak.",
            "O'zi xohlagan kasb talab qiladigan qobiliyat nimaligini aniqlab, oldindan tayyorgarlik ko'rish kerak.",
        ],
    },
    "신문의 역할": {
        "uz": "Gazetaning roli",
        "s": [
            "Gazeta odamlarning fikrini to'plash va yo'naltirish rolini bajaradi.",
            "Gazeta xato ishlarni topib, xabar berish va tanqid qilish rolini ham bajaradi.",
            "Biz gazeta to'g'ri ishlashi uchun uni nazorat qilish rolini bajarishimiz kerak.",
            "Agar gazeta biror masala haqida so'zsiz maqtasa yoki faqat yomon qilib xabar bersa, odamlarning ishonchini yo'qotadi.",
        ],
    },
    "노후 생활": {
        "uz": "Keksalikdagi (nafaqadagi) hayot",
        "s": [
            "Zamonaviy jamiyatda tibbiyot rivoji tufayli o'rtacha umr uzaygani sari, ilgariga nisbatan qarilik davri uzaydi.",
            "Baxtli keksalik hayoti uchun oldindan tayyorgarlik ko'rish zarur.",
            "Sog'liqni yo'qotish — hamma narsani yo'qotish bilan barobar.",
            "Iqtisodiy farovonlik uchun ko'proq jamg'arma qilish kerak.",
        ],
    },
    "교육자의 역할": {
        "uz": "O'qituvchining (tarbiyachining) roli",
        "s": [
            "O'qituvchi bilim va ijtimoiy me'yorlarni yetkazish rolini bajaradi.",
            "O'qituvchi o'quvchilarning qadriyatlari shakllanishiga ta'sir qilgani uchun, to'g'ri so'z va xatti-harakat bilan namuna bo'lishi kerak.",
            "Inson bir kunda o'zgarmaydi, shuning uchun ularga yordam bera olish uchun sabr-toqat shart.",
        ],
    },
    "영화의 장단점": {
        "uz": "Kinoning afzallik va kamchiliklari",
        "s": [
            "Odamlar zerikkanda, stress to'planganda, uchrashuvga chiqqanda ko'rgisi kelgan kinoni ko'radi.",
            "Qiziqarli, lekin ta'sirli bo'lmagan kinolar ham ko'p, va bunday kinoni ko'rgach, vaqtga achinadigan paytlar ham bo'ladi.",
            "Biz ishga kirgach, deyarli doim o'xshash muhitda yashaganimiz uchun tajriba cheklanib qolishi oson, kino esa buni to'ldirib beradi.",
        ],
    },
    "CCTV 설치": {
        "uz": "CCTV (kuzatuv kamerasi) o'rnatish",
        "s": [
            "CCTV o'rnatilishidan o'zini xavfsiz his qiladigan odam ham, shaxsiy hayotga tajovuz qiladi degan sabab bilan qarshi chiqadigan odam ham bor.",
            "Faqat xavfsizlik uchun degan sabab bilan shaxsiy hayot qurbon bo'lmasligi kerak.",
            "Albatta, CCTV kamerasi tufayli jinoyat hal bo'ladigan holatlar bor, lekin umumiy nisbatda olsak, ko'p emas.",
        ],
    },
    "자국어의 중요함": {
        "uz": "Ona tilining muhimligi",
        "s": [
            "Til o'sha mamlakat madaniyati, tarixi, xalqning hissiyoti kabilarning barchasini o'z ichiga oladi.",
            "Ona tili shunchaki muloqot vositasi emas, o'sha mamlakat odamlariga muhim ta'sir ko'rsatadi.",
            "Biz ona tili orqali o'sha xalq vakili sifatida o'zligimiz (identiteti) va millat ruhini o'rgana olamiz.",
        ],
    },
}

PER_PART = 5
_BADGE = ('<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;'
          'font-size:0.85em;">쓰기 54</span>')


def _topic_card(topic):
    tr = _TR[_norm(topic["title"])]
    ko_title = html.escape(topic["title"])
    uz_title = html.escape(tr["uz"])
    items = ""
    for ko, uz in zip(topic["sents"], tr["s"]):
        items += (f'<li style="margin-bottom:8px;"><strong>{html.escape(ko)}</strong><br>'
                  f'<span style="color:#475569;"><em>{html.escape(uz)}</em></span></li>')
    return f"""
<div style="background:#ffffff;border-left:4px solid #a855f7;box-shadow:0 1px 2px rgba(0,0,0,.06);padding:12px 16px;border-radius:8px;margin:16px 0;">
  <p style="margin:0 0 8px;"><strong style="font-size:1.08em;">📌 {ko_title}</strong>
     &nbsp;—&nbsp;<span style="color:#7c3aed;">{uz_title}</span></p>
  <ol style="margin:0;line-height:1.6;">{items}</ol>
</div>
"""


def _intro(part_no, first, last):
    if part_no == 1:
        return f"""
<h2>TOPIK Writing 54: Mavzu jumlalari ({part_no}-qism)</h2>
<p>{_BADGE} &nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">yodlash uchun</span></p>
<p>쓰기 54 inshosi uchun <strong>maxsus mavzular bo'yicha tayyor jumlalar</strong>. Har
mavzuda 3–4 ta jumla — koreyschasini yodlang, o'zbekcha tarjimasi tushunish uchun.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Qanday yodlash:</strong> har jumlani <strong>kuniga 3 marta, 3 kun</strong>
  yozing (kuniga 3 ta jumla). Metod haqida <em>“Jumla yodlash metodi”</em> darsiga qarang.
</div>
"""
    return f"""
<h2>TOPIK Writing 54: Mavzu jumlalari ({part_no}-qism)</h2>
<p>Yana bir necha mavzu bo'yicha tayyor jumlalar — koreyschasini yodlang.</p>
"""


_CLOSING = """
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> hamma mavzuni emas — imtihonda chiqishi mumkin bo'lgan bir
  nechta mavzuni tanlab, ularning jumlalarini mukammal yodlang. (전략 darsiga qarang.)
</div>
"""

# Faqat tarjima qilingan mavzular, fayldagi tartibda.
_TR = {_norm(k): v for k, v in TRANSLATIONS.items()}
_ready = [t for t in _TOPICS if _norm(t["title"]) in _TR]

LESSONS = []
for _pi, _start in enumerate(range(0, len(_ready), PER_PART), start=1):
    _chunk = _ready[_start:_start + PER_PART]
    _blocks = [{"rich_text": _intro(_pi, _start + 1, _start + len(_chunk))}]
    for _t in _chunk:
        _blocks.append({"rich_text": _topic_card(_t)})
    _blocks.append({"rich_text": _CLOSING})
    LESSONS.append({
        "skill":   "writing",
        "title":   f"TOPIK Writing 54: Mavzu jumlalari ({_pi}-qism)",
        "summary": f"쓰기 54 — {_start + 1}–{_start + len(_chunk)}-mavzular bo'yicha yodlash "
                   f"uchun tayyor jumlalar (koreyscha + o'zbekcha).",
        "order":   30 + _pi,   # 31, 32, ... (Q54 diapazoni)
        "blocks":  _blocks,
    })
