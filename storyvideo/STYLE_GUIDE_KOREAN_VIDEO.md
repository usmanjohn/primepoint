# Koreys videolar — qanday yasaladi

`storyvideo/` orqali koreys tili haqidagi 1080x1920 videolarni yasash qoʻllanmasi.
Birinchi uchtasi 2026-08-30 da yasaldi: **ko01** (출 ildiz oilasi), **ko02** (alifbo),
**ko03** (soʻz tartibi). Ingliz tili uchun ham xuddi shu mashina ishlaydi — farqi
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

python3 korean.py                  # 0. talaffuz qoidalari hali ham toʻgʻrimi (15/15)
python3 cli.py lint    ko04        # 1. uchta darvoza, render yoʻq
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
`kamsahamnida`**: u ikki qoidani birdan mixlaydi. `python3 korean.py` 15 ta holatni
tekshiradi; qoidaga tegsangiz, avval shuni ishlating.

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

- [ ] `python3 korean.py` → 15/15
- [ ] `cli.py lint` → PASS (uchta darvoza)
- [ ] `cli.py sheet` → **har bir kadrga** qaradim
- [ ] `cli.py script --one --ssml` → raqam yoʻq, hangul yoʻq, hanja yoʻq, <2000 belgi
- [ ] `practice` kartasidagi manzil bazada haqiqatan bor
- [ ] sanalar va sonlar tekshirilgan (tarixiy film boʻlsa — ikki marta)
- [ ] `cli.py kowords` → koreyscha klip bor
- [ ] **`cli.py check --audio`** → «split ishonchli»
- [ ] `cli.py voice` → PASS, keyin tayyor mp4 dan bir necha kadr olib koʻrdim
