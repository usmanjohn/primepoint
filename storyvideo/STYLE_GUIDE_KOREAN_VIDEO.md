# Koreys videolar — qanday yasaladi

`storyvideo/` orqali koreys tili haqidagi 1080x1920 videolarni yasash qoʻllanmasi.
Birinchi uchtasi 2026-08-30 da yasaldi: **ko01** (출 ildiz oilasi), **ko02** (alifbo),
**ko03** (soʻz tartibi). 2026-09-11 da «Tutilgan xato» seriyasi qoʻshildi:
**ko04** (nutq darajalari), **ko05** (에/에서), **ko06** (ikkita sanoq tizimi) —
muqova, fan urgʻusi va burchak chipi bilan; `README.md` ning oxirgi boʻlimiga qarang. Ingliz tili uchun ham xuddi shu mashina ishlaydi — farqi
faqat `korean.py` oʻrniga qoʻlda yozilgan talaffuz.

Umumiy renderer, `seek(t)` shartnomasi va matematika videolarining qoidalari
`README.md` da. Bu fayl faqat **til videolariga** tegishli qismni yozadi.

---

## 1. Asosiy gʻoya: rasm emas, MEXANIZM

Matematika videolari yaxshi chiqadi, chunki **rasm dalil keltiradi** — sanagich
haqiqiy nuqtalarni sanaydi, ustun oʻsadi, notoʻgʻri javob chizib tashlanadi.
Internetdan olingan surat hech qanday dalil keltirmaydi: uni `lint` tekshira olmaydi,
`seek(t)` ga boʻysunmaydi va sayt ranglariga qarshi turadi.

**Shuning uchun bu videolarga surat kerak emas va qidirilmaydi.** Tilning oʻzida
sanaladigan tuzilma bor, va u allaqachon bazada:

| Matematikada | Tilda | Qaysi beat |
|---|---|---|
| 37 ta stul | 출(出) → **9 ta soʻz** | `word_family` + sanagich |
| 608 − 550 = 58 | `per- + spect + -ive` | `pairs`, `solve` |
| ikkita narx | 감사합니다 va 고마워 | `versus`, `order` |
| notoʻgʻri javob | notoʻgʻri nutq darajasi | `claim → consequence → correct` |
| diagramma | ogʻiz kesimi, nutq darajalari | `shape`, `bars` |
| Ulugʻbek, 1424 | Sejong, **1443** | `era` · `portrait` · `fact` |

Manba: `examprep.VocabRoot` — TOPIK uchun **51 ta ildiz / 202 ta soʻz**,
IELTS uchun **31 ta ildiz / 167 ta soʻz**. Bitta ildiz = bitta video.

---

## 2. Toʻliq sikl

```bash
cd storyvideo                      # HAR DOIM shu papkadan; `python -m storyvideo` ISHLAMAYDI

python3 korean.py                  # 0. talaffuz qoidalari hali ham toʻgʻrimi (36/36)
python3 cli.py lint    ko04        # 1. toʻrtta darvoza, render yoʻq
python3 cli.py sheet   ko04        # 2. HAR BIR kadrni koʻring (pastga qarang)
python3 cli.py script  ko04 --one --ssml    # 3. tts_scripts/ko04_tts_one.txt
python3 cli.py kowords ko04        # 4. koreyscha ovozlar (yagona internet talab qiladigan qadam)
#   → 5. matnni saytga qoʻying, mp3 ni tts_audios/ ga saqlang
python3 cli.py check   ko04 --audio tts_audios/ko_04.mp3     # 6. BIR SONIYA
python3 cli.py voice   ko04 --audio tts_audios/ko_04.mp3 \
                            --script tts_scripts/ko04_tts_one.txt --workers 3
#   → videos/ko04_voiced.mp4  (~6 daqiqa)
```

**6-qadamni hech qachon oʻtkazib yubormang.** U bir soniya turadi, `voice` esa olti
daqiqa. 2026-08-30 da u ikki marta buzuq yozuvni render qilinishidan oldin ushladi.

---

## 3. Spetsifikatsiya yozish

Fayl: `stories/ko04.py` — `Video(slug=…, scenes=[…])` + oxirida `narrate(VIDEO, [...])`.
Har bir sahnaga bitta ovoz satri, jim sahnaga `None`.

### Til beatlari (`scenes.py`, KOREYS boʻlimi)

| beat | nima qiladi | qachon |
|---|---|---|
| `word` | bitta soʻz: 한글 + talaffuz + maʼno | tanishtirish |
| `word_family` | ildiz + u ochadigan soʻzlar, **sanaladi** | videoning yuragi |
| `spell` | ㅎ + ㅏ + ㄴ → 한 | alifbo, boʻgʻin bloki |
| `shape` | ogʻiz kesimi, bitta artikulyator oltin | harf shakli |
| `order` | bir gap uch tilda, **ustunlarda** | grammatika, tartib |
| `pairs` | 조사 ↔ oʻzbekcha qoʻshimcha jadvali | qoʻshimchalar |
| `echo` | **jim sahna** — koreyscha ovoz aytadi | takrorlash |
| `practice` | Powertyga yoʻllovchi karta | oxiridan oldin |

Matematika kiti (`hook` `count_in` `says` `beat` `claim` `consequence` `correct`
`check` `versus` `fill` `walk`) va tarix kiti (`era` `portrait` `fact`) ham
ishlaydi — `rule` va `ask` esa har doim ishlatiladi.

### Tuzilish

    era/word/fact  →  mexanizm (family/spell/shape/order)  →  echo
                   →  rule  →  ask  →  practice  →  outro

`ask` — **oxirgi fikr**: javobi hech qayerda yoʻq boʻlgan koʻchirma savol.
`practice` undan keyin turadi va bu qoidani buzmaydi: koʻrsatkich javob emas.

**`practice` manzili haqiqiy boʻlsin.** Baza soʻrab tekshiring:
ko01 → `/examprep/topik/vocab/roots/`, ko03 → PK-17 (을/를 va 의).

---

## 4. ⚠️ Ovoz matni — uchta qatʼiy qoida

### 4.1 Hangulni hech qachon dvigatelga bermang

Oʻzbek ovozi 한글 ni sukut deb oʻqiydi. Bu **raqam qoidasining aynan oʻzi**:
spetsifikatsiyada haqiqiy soʻzni yozasiz, `speech.py` uni `korean.romanise_all`
orqali oʻtkazadi, ekranda esa 한글 qoladi. `cli.py script` qolib ketganini topsa
xato beradi.

    "Koreyadagi har bir binoda: *출구*."   →   "…: chulgu."

### 4.2 Hanja va yakka harf — RAD ETILADI, oʻgirilmaydi

出 ning bir nechta koreyscha oʻqilishi bor; ㄱ — unlisiz undosh. Hisoblab
chiqaradigan narsa yoʻq. **Ekranda ular maqsad, ovozda esa oʻzbekcha ayting:**

    ekranda:  ㄱ harfi 出 dan                ovozda:  "k tovushi"

(Yakka harflar 가-힣 dan boshqa Unicode blokida — birinchi darvoza ularni
umuman koʻrmagan edi.)

### 4.3 Raqamlar va tartib sonlar

`speech.py` hammasini soʻzga aylantiradi: `1443-yil` → «ming toʻrt yuz qirq uchinchi
yil». Tartib son unlidan keyin `-nchi`, undoshdan keyin `-inchi` oladi
(`17-dars` → «oʻn yettinchi dars»). Digit qolib ketsa `script` xato beradi.

### Talaffuz qayerdan keladi

`korean.py` — jamo boʻlish arifmetika, ish esa beshta tovush qoidasida
(연음 · 비음화 · 유음화 · 격음화 · jaranglilik). **Etalon holat — 감사합니다 →
`kamsahamnida`**: u ikki qoidani birdan mixlaydi. `python3 korean.py` 36 ta holatni
tekshiradi; qoidaga tegsangiz, avval shuni ishlating.

### ⚠️ Koreyscha soʻz kadrda hech qachon boʻlinmasin

Hangulda soʻz ichida boʻsh joy yoʻq, shuning uchun brauzer 먹어요 ni
**먹 / 어요** qilib ikkiga boʻlib tashlaydi — yaʼni mavjud boʻlmagan ikkita
soʻzga. Ikki marta ushlandi: 감사합니다 ko04 ning `pairs` jadvalida, 먹어요 esa
ko08 ning `ask` sahnasida. Yechim `stage.css` da: `.pair b` ga `nowrap`,
qolgan matn klasslariga (`hero big expr ttl ask lbl cap cmp__* pron__k pron__g`)
**`word-break: keep-all`** — lotin matniga taʼsiri yoʻq.

### ⚠️ `versus` kartasini boʻsh joysiz uzun soʻz kengaytirib yuboradi

`.cmp__side` — flex element, va u oʻz min-content kengligidan pastga
siqilmaydi. Shuning uchun **boʻsh joysiz bitta uzun soʻz** (teg satrida
`bora olmayman` emas, `boraolmayman`) butun kartani kadrdan chiqarib yuboradi.

Tuzatishning **notoʻgʻri** yoʻli — `.cmp__side { min-width: 0 }`: u ko08 ni
tuzatdi va **mo01 ni buzdi** (karta endi mazmunidan kichrayib, chap chetdan
chiqib ketdi, x = −25). Umumiy kitga tegishdan oldin butun katalogni linting
qiling. Toʻgʻri yoʻli oddiy: **tegda boʻsh joy boʻlsin** — `ketayotgan odamga`,
`ketayotganga` emas. Bu, qolaversa, oʻzbek imlosiga ham mos.

### ⚠️ 구개음화 — ㅅ/ㅆ + ㅣ yoki y-unli = **sh**, hech qachon **s** emas

2026-09-13 da foydalanuvchining qulogʻi ushladi, `selftest` esa **oʻn besh
holatda ham sezmagan**: 감사합니다 da 사, 안녕하세요 da 세, 수출 da 수 — birortasida
ham **시** yoʻq edi. Natijada ko06 (soat va sonlar filmi) boshdan-oxir
«sam si samsip pun» deb oʻqilgan.

    시 → shi      십 → ship      이십 → iship      삼십 → samship
    사 → sa       세 → se        셋 → set         수 → su      (oʻzgarmaydi)

**y-unli sh ichiga singib ketadi**, shuning uchun unlidan y tushadi:
셔 → `sho`, `shyo` EMAS. Bu — yapon romanizatoridagi yoon tuzogʻining aynan
oʻzi, va shu sababli `PALATAL` alohida jadval, flag emas.

Endi 36 ta holat tekshiriladi va ular orasida 시, 십, 이십, 삼십, 시간, 소식,
샤워 bor — hamda oʻzgarmasligi kerak boʻlganlar: 사, 수, 셋, 서울.
Bu rule 신라 ning eski kutilgan javobini ham tuzatdi: `silla` emas, **`shilla`**.

### ⚠️ 자음군 단순화 — ikki undoshli 받침 dan FAQAT BITTASI eshitiladi

2026-09-16 da topildi, ko14 ga 시간이 없다 kerak boʻlganda. Kod har doim
klasterning **oxirgisini** olardi — bu ㄺ ㄻ ㄿ uchun toʻgʻri, qolgan yettitasi
uchun notoʻgʻri:

    없다 → «opta»,  «otta» emas        값 → «kap»       앉다 → «anta»
    여덟 → «yodol»                      핥다 → «halta»
    닭 → «tak»     삶 → «sam»          읽다 → «ikta»    (bular oʻzgarmadi)

Va ㄺ **ㄱ dan oldin** ㄹ ini saqlaydi: 읽기 [일끼] → **`ilki`**. Bu qoida
koreys tilidan tashqarida ham muhim edi: ilgari 읽기 «ikki» boʻlib chiqardi —
yaʼni oʻzbekcha **«ikki»** soni, sonlarga toʻla ovoz matnining oʻrtasida.

Jarangsizlantirish (경음화) tushib qolgan undosh tufayli qoladi, lekin
qoʻshaloq harf bilan emas — PALATAL bilan bir xil tanlov: **`anta`**, `anda`
ham emas, `antta` ham emas.

**Yana bir marta oʻsha saboq:** avval yiqiladigan holatni yozdim (36 tadan
7 tasi qizil chiqdi), keyin qoidani. Yashil selftest qoidaning borligini
isbotlamaydi.

**Saboq: yangi tovush qoidasi qoʻshsangiz, avval uni USHLAYDIGAN holat yozing.**
Oʻn besh holat yashil boʻlgani qoidaning borligini isbotlamaydi.

Oʻzbek tilining ikkita omadi: **ㅗ→`oʻ` / ㅓ→`o`** — ingliz transliteratsiyasi
yoʻqotadigan farq. ㅡ esa `u` deb yoziladi va ㅜ bilan ataylab toʻqnashadi
(lotin oʻzbekchada ы yoʻq) — ekranda 한글 turadi va koreyscha ovoz aytadi, shuning
uchun transliteratsiya koʻprik, hakam emas.

---

## 5. Koreyscha ovoz — faqat jim sahnada

Oʻzbek ovozi oʻz sahnasining deyarli har soniyasini toʻldiradi, shuning uchun
uning ostiga qoʻyilgan koreyscha soʻz — loyqa. Soʻz darajasida moslashtirish yoʻq.

**`scenes.echo` — `say=None` boʻlgan sahna.** `retime` unga oʻz vaqtini beradi,
`mix` unga ovoz qoʻymaydi, `koaudio` esa oʻsha teshikka soʻzni **ikki marta**
joylaydi. `voice.split` ga tegilmadi — gap shunda edi.

Bu, qolaversa, toʻgʻri pedagogik beat: matematika videolari bitta jim sahnani
tomoshabin hisoblasin deb himoya qiladi, til videosi esa **ovoz chiqarib
takrorlasin** deb.

    python3 cli.py kowords ko04          # assets/ko_words/ ga yuklab oladi (git da saqlanadi)
    python3 cli.py voice … --ko-gain 0.95   # baland tuyulsa 0.75

Ovoz: `ko-KR-SunHiNeural`, tezlik −10%. Klip ~1 soniya; ikkita talaffuz orasi
2.0 s, sahna esa ~4.2 s — uzun ibora sigʻmay qolishi mumkin, tekshiring.

---

## 6. `check` — ikkita butunlay boshqa nosozlik

```
python3 cli.py check ko04 --audio tts_audios/ko_04.mp3
```

Har bir segmentni **yozuvning oʻz tezligiga** solishtiradi (20% tez oʻqilgan
yozuv aks holda hammasini belgilab tashlaydi) va nosozlikni nomlaydi:

**`SHUBHALI CHEGARA`** — solver chegarani notoʻgʻri qoʻygan. **Vaqt saqlanadi**:
siqilgan segment doim choʻzilganining yonida turadi. Qayta yozish shart emas.

**`OVOZDA MATN YOQ`** — dvigatel matnning bir qismini umuman aytmagan. Yoʻqolgan
vaqtni hech kim yutmaydi: qisqa segmentning **ikkala qoʻshnisi ham joyida**.
Hech qanday qayta yechish buni tuzatmaydi.

> ⚠️ **Nosozlikni solverning oʻz splitidan aniqlamang.** Matn yoʻqolganda solver
> chegaralarni baribir bir joyga qoʻyishga majbur va zararni yoyib yuboradi:
> ko02 da u 4-blokni ayblagan, aybdor esa 9-blok edi. `check` sodda gipotezani
> (eng uzun n−1 sukut) ham baholaydi va chetlashishi kamrog'ini koʻrsatadi.

### Dvigatel ayni bitta gapni TAKROR tashlab ketishi mumkin

ko02 ikkita alohida yozuvda bir xil gapni yoʻqotdi. Belgi muammosi emas edi,
kesish ham emas (keyingi blok normal aytilgan). Yoʻqolgani — blokning ichki
`<break time='0.45s'/>` idan **oldingi** hamma narsa.

**Yechim: shu blokning ichki tanaffusini olib tashlang va gapni qisqartiring.**
Keyingi dubl toza chiqdi (0.24x → 1.04x). **Oʻzgartirmasdan uchinchi marta
yozdirmang.** `||` beatini faqat ikkala tomonida haqiqiy matn bor blokda qoldiring.

---

## 7. Dvigatel shartnomasi

- **Speed +26%, Pitch +10%** — har doim, ovozlar bir xil boʻlishi uchun.
- **Bitta qoʻyishda 2000 belgi**, SSML teglari ham sanaladi. Maqsad 1300–1800.
  `script` 95% dan oshsa ogohlantiradi, 100% dan oshsa xato beradi.
- Faqat `break` va `emphasis`. `prosody` yoʻq, `<speak>` oʻrami yoʻq.
- Tanaffuslar `speech.py` da: **SCENE 2.5s · INNER 0.45s · SHORT 0.3s**.
- Belgilar: `*taʼkid*` · `|` qisqa nafas · `||` beat.
- **Ergashuvchi gap teglari yoʻq** — «dedi», «dedi u» yozilmaydi.

---

## 8. Chizmadagi tuzoqlar (toʻlangan)

**Ogʻiz kesimi uch marta qayta chizildi.** Beshta nuqtasi belgilangan «quvur»
divanga oʻxshab qoldi. Chizmani ogʻiz qiladigan narsa — **siluet (burun va iyak)
va YOPIQ bosh konturi**; ochiq qoldirilsa chiziqlar havoda uzilib, tugallanmagan
koʻrinadi. Oʻrgatadigan narsa esa — **tilning zonalar orasida harakatlanishi**
(har bir artikulyatsiya joyi uchun alohida yoʻl), qimirlamas rasm ustidagi
koʻchuvchi belgi emas.

**Ustun tekisligi `order` ning butun ayyorligi.** Uch gapni erkin oqimda qoʻysangiz
oʻquvchi ularni oʻqib solishtirishi kerak; qatʼiy uch ustunli setkada esa inglizcha
qatorning ranglari shunchaki mos tushmaydi — dalil bir soʻz aytilmasdan keltiriladi.

**Ajratgichini oʻzi chizadigan builder maʼlumot bilan takrorlanadi.**
`= = oʻzbekcha -ni` tayyor videoga chiqib ketdi: `pair_rows` `=` ni oʻzi chizadi,
spetsifikatsiyada esa yana bittasi yozilgan edi. `lint` buni koʻra olmaydi.

> **Kontakt varagʻining HAMMASINI koʻring, bitta kadrini emas.** Yuqoridagi xato
> aynan men qaramagan kadrda edi.

Yana: SVG `<text>` ni viewBox chetiga yaqin qoʻymang (iyak ustiga bosib chiqdi);
`.pron__k` oʻzi kichraymaydi — uzun ibora uchun `size=` bering.

**`.pron__k` ham `word-break: keep-all` roʻyxatiga qoʻshildi (2026-09-16).**
ko16 ning `echo` kartasi 호랑이도 온다 ni «호랑이도 온 / 다» qilib boʻlib
tashladi — ko04 dagi 감사합니다 bilan aynan bir xil nosozlik, faqat asl
tuzatish oʻtkazib yuborgan klassda. Undan oldingi har bir `echo` yo yetarlicha
qisqa edi, yo `size=` bilan yozilgan edi. Ikkalasini ham qiling: klass
tuzatildi, uzun iboraga esa baribir `size=` bering.

---

## 9. Manba javoni: «Koreya olami»

`corner` toʻplami (Korean, order 5) —
`corner/management/commands/toc_koreya_olami.txt` da butun siyosat.
36 ta matn toʻrt oilaga boʻlingan, 3 tasi yozilgan.

Boshqa har qanday koreys toʻplamidan farqi: **nasr oʻzbekcha, koreys tili esa
material** — har bir soʻz `cn-word` spani. Talaffuz qavs ichida `korean.py`
qanday yozsa shunday yoziladi, shunda javon, video va ovoz bir-biriga zid boʻlmaydi.
⛔ Bu javonda audio yoʻq.

```
railway run python manage.py import_corner \
    corner/management/commands/_stories_koreya_olami_<range>.py --author=powerty
```

---

## 10. Chiqarishdan oldingi roʻyxat

- [ ] `python3 korean.py` → 36/36
- [ ] `cli.py lint` → PASS (**toʻrtta** darvoza — muqova ham)
- [ ] `Video(subject=...)` qoʻyilgan (aks holda urgʻu ham, chip ham yoʻq)
- [ ] muqovaning 0-kadri toʻliq chizilgan, qizil chiziq FAQAT xato boʻlakdan oʻtadi
- [ ] muqova vaʼdasi toʻrt soʻzdan koʻp emas va mavzu nomi EMAS
- [ ] `cli.py sheet` → **har bir kadrga** qaradim
- [ ] `cli.py script --one --ssml` → raqam yoʻq, hangul yoʻq, hanja yoʻq, <2000 belgi
- [ ] `practice` kartasidagi manzil bazada haqiqatan bor
- [ ] sanalar va sonlar tekshirilgan (tarixiy film boʻlsa — ikki marta)
- [ ] `cli.py kowords` → koreyscha klip bor
- [ ] **`cli.py check --audio`** → «split ishonchli»
- [ ] `cli.py voice` → PASS, keyin tayyor mp4 dan bir necha kadr olib koʻrdim
