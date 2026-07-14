# TOPIK Lesson Writing Guide (for Claude)

This guide tells Claude HOW to write **examprep** TOPIK lessons. It is the same for every
skill (Reading 읽기, Writing 쓰기, Listening 듣기). Each skill has its own table-of-contents
file (e.g. `toc_topik_writing.txt`) listing the lessons in order. **Always follow that order.**

> ⚠️ **This guide is written in English for Claude, but the LESSONS YOU PRODUCE MUST BE IN
> UZBEK + KOREAN — never English.** The audience is young Uzbek students learning Korean.
> English in the lesson body is wrong. Goal: *yoshlar uchun oʻrganishni oson qilamiz!*

The data model: a lesson is a list of **blocks**. The player renders each block in order:
**image (+caption) → rich text → MCQ choices → explanation (after submit)**. Compose a
lesson from several blocks rather than one giant field.

**Topics (question-type cards).** Lessons are grouped by a `topic` — a question type inside
the skill (e.g. Reading → "Reklama va e'lonlar (광고·안내문)"). The skill page shows one card
per topic, and the lesson player's playlist is scoped to the topic. Every lesson in a data
file should carry a shared `TOPIC = {"title", "summary", "icon", "order"}` dict passed as
`"topic": TOPIC`. Topic titles are Uzbek + Korean in parentheses; the toc file's
`## TOPIC:` headers say which lessons belong to which topic. Give each topic its own
lesson-`order` decade (10–19, 20–29, …) so groups never collide.

---

## 1. Til siyosati — Language policy (MOST IMPORTANT)

- **Asosiy til = Oʻzbekcha.** All explanation, instructions, headings, and the `summary`
  field are in **Uzbek**.
- **Korean (한글) is used for the actual exam material** — example sentences, vocabulary,
  grammar patterns, question prompts — always with an Uzbek translation right under it.
- **Do NOT use English** in the lesson body (the only allowed exceptions are unavoidable
  proper nouns like "TOPIK"). No English explanations, no English glossary.
- Korean is written as Hangul (한글), not romanized (unless teaching pronunciation).

## 2. Lesson structure (the `blocks` list)

Build each lesson from blocks, in this order (all text in Uzbek, examples in Korean):

1. **Kirish bloki** (`rich_text`) — `<h2>` sarlavha + 1–2 jumlalik Uzbek tavsif: bu dars
   nimani oʻrgatadi va nega TOPIK uchun muhim.
2. **Tushuntirish bloklari** (`rich_text`) — strategiya/qoidani bosqichma-bosqich, oson →
   qiyin. Bir nechta kichik blok ishlating (tushuncha → usul → namunalar → tez-tez
   uchraydigan xatolar), shunda player chiroyli sahifalaydi. **Koʻp namuna bering.**
3. **Amaliyot (savol) bloklari** — `rich_text` da savol (oʻzbekcha/koreyscha) + `choices`
   (variantlar, faqat bittasi `is_correct: True`) + `explanation` (javobdan keyin koʻrinadi,
   toʻliq tushuntirish bilan).
4. **Yakuniy blok** (`rich_text`) — "Kalit soʻzlar" lugʻati (3-bandga qarang), keyin
   `<h3>Xulosa</h3>` va asosiy fikrlar roʻyxati.

### Chuqurlik (minimal talab — yupqa dars yozmang)

Har bir dars **batafsil** boʻlishi shart. Bloklar boʻylab jami:
- kamida ~500–800 soʻz haqiqiy tushuntirish (oʻzbekcha);
- **koʻplab koreyscha namunalar** (jumlalar, iboralar) — har biri oʻzbekcha tarjimasi bilan;
- kamida **2 ta amaliyot savoli** (`choices` + `explanation`);
- "Kalit soʻzlar" lugʻati.

## 3. Styling palette — use these freely (copy-paste these HTML snippets)

The site is light-mode only, so these inline-styled boxes are safe. **Mix them** — make the
page colorful and easy to scan.

**Highlights (`<mark>`):**
```
<mark>muhim</mark>
<mark style="background:#dbeafe;">grammatika</mark>          (koʻk)
<mark style="background:#dcfce7;">toʻgʻri</mark>             (yashil)
<mark style="background:#fee2e2;">xato</mark>               (qizil)
```

**Rangli callout qutilari (quotes with background):**
```
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> ...
</div>                                                        (yashil — maslahat)

<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> ...
</div>                                                        (sariq — ogohlantirish)

<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> ...
</div>                                                        (koʻk — ma'lumot)

<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 Namuna:</strong> ...
</div>                                                        (binafsha — namuna)
```

**Koreyscha jumla kartasi (Korean sentence card — Korean big, Uzbek under):**
```
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>현대 사회에서 ~은/는 중요한 문제이다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Zamonaviy jamiyatda ~ muhim masala hisoblanadi.</em></p>
</div>
```

**Ochiladigan menyu (dropdown — `<details>`):**
```
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 서론 (kirish) jumlalari — bosing</summary>
  <div style="margin-top:10px;"> ...kartalar... </div>
</details>
```

**Badge / yorliq:**
```
<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">TOPIK 54</span>
```

Also use: `<ul>/<ol>`, `<strong>/<em>/<u>`, and group long lists of sentences inside
dropdowns so the page stays tidy.

## 4. Choices (amaliyot savollari)

Use MCQ blocks generously for practice. Prompt in `rich_text` (oʻzbekcha, kerak boʻlsa
koreyscha matn bilan), options in `choices`, full reasoning in `explanation` (oʻzbekcha).
Aim for at least 2 per lesson; varied — vocabulary, grammar, "find the 결론 sentence", etc.

## 5. Kalit soʻzlar (glossary) & summary

- Yakunda **"Kalit soʻzlar"** bloki: kamida 6–8 ta muhim **koreyscha** soʻz/ibora, har biri
  oʻzbekcha tarjimasi bilan (English yoʻq).
- `summary` maydoni (≤300 belgi): bitta aniq **oʻzbekcha** jumla — dars nimani oʻrgatadi.

---

## 5b. Interaktiv komponentlar — Interactive components (kit)

Darslar endi **interaktiv**. Bir statik CSS/JS to'plami (`examprep-kit.css` / `examprep-kit.js`)
har bir dars sahifasida ishlaydi. Komponentlar **progressive enhancement** — JavaScript
o'chiq bo'lsa ham sahifa to'liq o'qiladi. Ularni HTML ichida **class + `data-` atribut**
orqali chaqirasiz. **Har darsda hammasini ishlatmang** — faqat pedagogik jihatdan foydali
joyda. Ko'p `<div style="...">` qutilar o'rniga shu komponentlarni ishlating.

### (a) MCQ — hech qanday markup shart emas
Oddiy `choices` bloki (4-bo'lim) endi **avtomatik** interaktiv: talaba variantni bosishi
bilan darhol yashil/qizil bo'ladi va `explanation` ochiladi (sahifa qayta yuklanmaydi).
Hech narsa o'zgartirmang — shunchaki `choices` + `explanation` yozing.

### (b) Flashcards (so'z kartalari) — `data-pp-flashcards`
"Kalit so'zlar" glossariysi (`<ul>`) o'rniga **ayni shu ma'lumotni** kartaga aylantiring —
old tomon koreyscha, orqa tomon o'zbekcha. Bosib ag'dariladi, ←/→ bilan aylantiriladi.
```html
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">읽기</div><div class="pp-card-back">o'qish</div></div>
  <div class="pp-card"><div class="pp-card-front">지문</div><div class="pp-card-back">matn / parcha</div></div>
  <!-- kamida 6–8 ta -->
</div>
```

### (c) Step reveal (qadam-baqadam) — `data-pp-steps`
Uzun tushuntirish yoki ishlangan misolni **bo'lib** bering — talaba "Keyingi qadam" tugmasi
bilan birma-bir ochadi (birdan skanerlamaydi). Har bosqich — bitta `.pp-step`.
```html
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p>Birinchi qadam...</p></div>
  <div class="pp-step"><p>Ikkinchi qadam...</p></div>
</div>
```

### Qaysi ko'nikma uchun nima (controlled variety)
- **읽기 Reading:** step-reveal (strategiya/misol) + inline MCQ + flashcards (glossary).
- **쓰기 Writing (51–54):** step-reveal (namuna javobni bo'lib ko'rsatish) + flashcards (naqsh/ibora).
- **듣기 Listening:** rasm/audio bloki + MCQ.
- **전략 Strategy:** step-reveal + MCQ.

> ⚠️ MCQ **amaliyot** uchun (baholanmaydigan). To'g'ri javob HTML manbada ko'rinadi — bu normal.
> Baholanadigan, xronometrajli test — alohida `exam` ilovasi.

---

## 6. Foydalanuvchining TOPIK maslahatlari (user's own tips)

Foydalanuvchi TOPIK'ga oʻzi tayyorlangan va metodlarini ulashmoqda. Bu maslahatlar umumiy
tavsiyalardan **ustun turadi** — uning soʻzlari, urgʻusi va usullariga moslang.

### 쓰기 54 (Writing, 54-savol) — Jumla yodlash metodi
- **Yakka soʻzni** toʻgʻri ishlatish qiyin. **Butun namunaviy javobni** yodlash ham qiyin
  (eslab qolish qiyin). Oʻrtasini tanlang: **maxsus mavzular boʻyicha jumlalarni yodlang.**
- Darslarda shunday **koʻplab tayyor jumlalar** beriladi — talaba ularni oʻz javobida
  ishlatishi mumkin.
- **Metod:** har bir jumlani **kuniga 3 marta, 3 kun davomida** yozing — shunda jumla
  tabiiy ravishda eslab qolinadi. **Kuniga 3 ta jumla** oʻrganish kifoya.
- **Nega? (3 ta foyda):**
  1. Tayyor jumlada **grammatik yoki mantiqiy xato boʻlmaydi.**
  2. Jumlani eslab qolish **soʻzga qaraganda oson** — chunki butun jumla yaxlit ma'noga ega.
  3. Imtihonda **1–2 ta tayyor fikr** boʻladi; ularning atrofini boshqa fikrlar bilan
     toʻldirib, **vaqtida tugatish** mumkin. Aks holda har bir qism uchun fikr oʻylash
     koʻp vaqt oladi.
- **Muhim:** bu jumlalarni **kitob oʻqib** oʻrganish eng yaxshisi — eski javoblardan
  shunchaki koʻchirib emas. Kitobdan olingan jumlalar tabiiy va xilma-xil boʻladi.

### 읽기 (Reading) — "Koʻp oʻqing, kam tarjima qiling" (soʻz oʻrganish metodi)
- **Koʻp oʻqing, kam tarjima qiling.** Soʻzni **koʻrganda tushunish** uni yozib yodlashdan
  muhimroq — *koʻzni mashq qildiring, qoʻlni emas* (imtihonda soʻzni koʻrib tushunish kerak).
- **Tarjima qilsangiz ham**, soʻzning oʻzini qogʻozga koʻchirib yodlamang. Buning oʻrniga
  **bir-ikki kundan keyin butun matnni qayta oʻqing** — oʻrgangan soʻzlar matn ichida qayta
  uchragani sayin xotirada mustahkamlanadi (soʻz roʻyxati tez unutiladi).
- **Qaysi soʻzlar:** otdan (명사) koʻra **sifat (형용사), ravish (부사), feʼl (동사)** ni
  koʻproq oʻrganing — javoblarni asosan shular hal qiladi.
- **읽기 → 쓰기 koʻprigi:** oʻqiyotganda **ajoyib jumla** (soʻz yoki paragraf emas — aynan
  jumla) uchratsangiz, uni yozib qoʻying va keyin Yozish (쓰기) inshosida tayanch fikr qiling.
  Namuna: <em>합리적 소비를 하면 자연스럽게 사회 활동에도 동참할 수 있다.</em> Darslarda
  **koʻplab eslab qolish oson, koʻp mavzuga mos jumlalar** bering.

### 듣기 (Listening) — Podkast metodi
- **Eng yaxshi tinglash mashqi — podkast.** Musiqa/drama emas (koʻp vaqt oladi, TOPIK dialog
  turiga mos kelmaydi). Tavsiya seriyasi: **빅데이터로 보는 세상** — mavzulari imtihonga mos
  (뉴스 va murakkabroq savollar) hamda 쓰기 uchun ham foydali.
- **Foyda:** bir vaqtda tinglash + mantiq + koreyscha tafakkur + Yozish uchun gʻoyalar.
- **Qoidalar:** skript yozmang (받아쓰기 yoʻq), tarjima qilmang; boʻsh vaqtni atayin sarflamang —
  **yurganda/ovqat pishirganda/ishlaganda** tinglang; tartib muhim emas; tushunmasangiz ham
  tinglayvering; eshitgan gʻoyalarni 쓰기 (54) uchun eslab qoling.
- **Mashq nisbati:** 60% podkast, 30% kitob, 10% mock (모의고사).
- Darslarda podkastga **havola tugmasi** boʻladi (foydalanuvchi URL beradi; data faylda
  `__PODCAST_URL__` placeholderini almashtiring).

### 전략 (Strategy) — "Bittani mukammal oʻrganing" + vaqt rejasi
- Darslarda **200+ shablon** bor, lekin hammasini oʻrganmang. Har bir qism uchun **faqat
  bitta shablonni** tanlab **mukammal** egallang — bitta ishonchli shablon imtihonda
  avtomatik, xatosiz va tez ishlaydi (hammasini yuzaki bilish = chalkashlik).
- Bitta shablon [주제] ni almashtirib har mavzuga yetadi (namuna:
  <em>현대 사회에서 [주제]은/는 점점 더 중요한 문제가 되고 있다</em> → 환경/교육/과학...).
- **Vaqt rejasi:** imtihongacha faqat **oʻqing va oʻrganing (input)**; imtihondan
  **~1 oy oldin** 1–2 savolga **yozib javob bering (output)**. Yozishni erta boshlash shart emas.

_(Foydalanuvchi keyin boshqa maslahatlarini ham qoʻshadi — shu yerga yoz.)_

---

## How to ask (foydalanuvchi nima yozadi)

Masalan:
- **"Make the next 5 TOPIK writing lessons"** — Claude qaysi yozma darslar borligini
  tekshiradi, tartibda davom etadi, partiyani yozadi va import qiladi.
- **"Make TOPIK writing 1 to 6"** — aniq shu oraliqni.
- **"Redo TOPIK Writing 7"** — uni qayta yozadi (`--republish` bilan).

Claude qiladi: bu guide'ni oʻqiydi → kerakli `toc_topik_<skill>.txt` ni oʻqiydi → bazadan
shu track+skill dagi eng katta `order` ni topadi → keyingi partiyani
`_lessons_topik_<skill>_<range>.py` ga yozadi (Uzbek + Korean, rangli styling bilan) →
`python manage.py import_examprep <file> --author=<username>` ni ishga tushiradi.
