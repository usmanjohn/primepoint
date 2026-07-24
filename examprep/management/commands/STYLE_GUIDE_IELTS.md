# IELTS Lesson Writing Guide (for Claude)

This guide tells Claude HOW to write **examprep** IELTS lessons. It is the same for every
skill (Listening, Reading, Writing, Speaking). Each skill has its own table-of-contents
file (e.g. `toc_ielts_reading.txt`) listing the lessons in order. **Always follow that order.**

> ⚠️ **This guide is written in English for Claude, but the EXPLANATIONS YOU PRODUCE MUST BE
> IN UZBEK — never Russian.** The audience is young Uzbek students preparing for IELTS.
> The exam material itself (passages, questions, sample answers) stays in **English** — that's
> what students are being tested on — but every instruction, strategy note, and piece of
> feedback around it is Uzbek. Goal: *yoshlar uchun oʻrganishni oson qilamiz!*

The data model: a lesson is a list of **blocks**. The player renders each block in order:
**image (+caption) → rich text → MCQ choices → explanation (after submit)**. Compose a
lesson from several blocks rather than one giant field.

**Topics (question-type cards).** Lessons are grouped by a `topic` — a question type or
sub-skill inside the skill (e.g. Reading → "Haqiqat / Yolg'on / Berilmagan (True/False/Not
Given)"). The skill page shows one card per topic, and the lesson player's playlist is
scoped to the topic. Every lesson in a data file should carry a shared
`TOPIC = {"title", "summary", "icon", "order"}` dict passed as `"topic": TOPIC`. Topic
titles are Uzbek with the English exam term in parentheses; the toc file's `## TOPIC:`
headers say which lessons belong to which topic. Give each topic its own lesson-`order`
decade (10–19, 20–29, …) so groups never collide.

---

## 1. Til siyosati — Language policy (MOST IMPORTANT)

- **Asosiy til = Oʻzbekcha.** All explanation, instructions, headings, and the `summary`
  field are in **Uzbek**.
- **English is used for the actual exam material** — passage excerpts, question prompts,
  sample sentences, model answers, band-boosting vocabulary — always with an Uzbek
  translation or gloss right under/next to it, exactly like TOPIK does with Korean.
- **Do NOT write the strategy/explanation prose in English.** The only allowed
  English is exam material itself and unavoidable proper nouns/terms ("IELTS", "Task 2",
  "Band 7"). No English-only explanation blocks.
- Keep English at natural exam register (Academic or General Training as relevant) — don't
  simplify it to "learner English"; the point is to train students on real exam language.

## 2. Lesson structure (the `blocks` list)

Build each lesson from blocks, in this order (all explanation in Uzbek, examples in English):

1. **Kirish bloki** (`rich_text`) — `<h2>` sarlavha + 1–2 jumlalik Uzbek tavsif: bu dars
   nimani oʻrgatadi va nega IELTS uchun muhim (qaysi band ballga taʼsir qiladi).
2. **Tushuntirish bloklari** (`rich_text`) — strategiya/qoidani bosqichma-bosqich, oson →
   qiyin. Bir nechta kichik blok ishlating (tushuncha → usul → namunalar → tez-tez
   uchraydigan xatolar), shunda player chiroyli sahifalaydi. **Koʻp namuna bering.**
3. **Amaliyot (savol) bloklari** — `rich_text` da savol/parcha (inglizcha, kerak boʻlsa
   oʻzbekcha izoh bilan) + `choices` (variantlar, faqat bittasi `is_correct: True`) +
   `explanation` (javobdan keyin koʻrinadi, toʻliq oʻzbekcha tushuntirish bilan).
4. **Yakuniy blok** (`rich_text`) — "Kalit soʻzlar" lugʻati (3-bandga qarang), keyin
   `<h3>Xulosa</h3>` va asosiy fikrlar roʻyxati.

### Chuqurlik (minimal talab — yupqa dars yozmang)

Har bir dars **batafsil** boʻlishi shart. Bloklar boʻylab jami:
- kamida ~500–800 soʻz haqiqiy tushuntirish (oʻzbekcha);
- **koʻplab inglizcha namunalar** (jumlalar, parcha qismlari, ibora roʻyxatlari) — har biri
  kerak boʻlsa oʻzbekcha tarjima/izoh bilan;
- kamida **2 ta amaliyot savoli** (`choices` + `explanation`);
- "Kalit soʻzlar" lugʻati.

## 3. Styling palette — use these freely (copy-paste these HTML snippets)

The site is light-mode only, so these inline-styled boxes are safe. **Mix them** — make the
page colorful and easy to scan. (Identical kit to TOPIK — reuse verbatim.)

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

**Inglizcha jumla/ibora kartasi (English sentence card — English big, Uzbek under):**
```
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>The graph illustrates a marked increase in ~ over the given period.</strong></p>
  <p style="color:#475569;margin:0;"><em>Grafik berilgan davrda ~ ning sezilarli oʻsishini koʻrsatadi.</em></p>
</div>
```

**Ochiladigan menyu (dropdown — `<details>`):**
```
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 Foydali iboralar — bosing</summary>
  <div style="margin-top:10px;"> ...kartalar... </div>
</details>
```

**Badge / yorliq:**
```
<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Band 7+</span>
```

Also use: `<ul>/<ol>`, `<strong>/<em>/<u>`, and group long lists of phrases/vocabulary inside
dropdowns so the page stays tidy.

## 4. Choices (amaliyot savollari)

Use MCQ blocks generously for practice. Prompt/passage in `rich_text` (inglizcha matn +
kerak boʻlsa oʻzbekcha izoh), options in `choices`, full reasoning in `explanation`
(oʻzbekcha). Aim for at least 2 per lesson; varied — the real IELTS question types apply
here: True/False/Not Given, Yes/No/Not Given, matching headings, sentence/summary
completion, multiple choice, short answer, etc. (see toc topics per skill).

## 5. Kalit soʻzlar (glossary) & summary

- Yakunda **"Kalit soʻzlar"** bloki: kamida 6–8 ta muhim **inglizcha** soʻz/ibora
  (band-boosting collocations, linking words, or topic vocabulary), har biri oʻzbekcha
  tarjimasi bilan.
- `summary` maydoni (≤300 belgi): bitta aniq **oʻzbekcha** jumla — dars nimani oʻrgatadi.

---

## 5b. Interaktiv komponentlar — Interactive components (kit)

Darslar **interaktiv**. Bir statik CSS/JS to'plami (`examprep-kit.css` / `examprep-kit.js`)
har bir dars sahifasida ishlaydi — TOPIK bilan bir xil kit, xuddi shu tarzda ishlatiladi.
Progressive enhancement — JavaScript o'chiq bo'lsa ham sahifa to'liq o'qiladi. **Har darsda
hammasini ishlatmang** — faqat pedagogik jihatdan foydali joyda.

### (a) MCQ — hech qanday markup shart emas
Oddiy `choices` bloki (4-bo'lim) endi **avtomatik** interaktiv: talaba variantni bosishi
bilan darhol yashil/qizil bo'ladi va `explanation` ochiladi. Hech narsa o'zgartirmang —
shunchaki `choices` + `explanation` yozing.

### (b) Flashcards (so'z kartalari) — `data-pp-flashcards`
"Kalit so'zlar" glossariysi (`<ul>`) o'rniga **ayni shu ma'lumotni** kartaga aylantiring —
old tomon inglizcha, orqa tomon o'zbekcha. Bosib ag'dariladi, ←/→ bilan aylantiriladi.
```html
<h3>Kalit so'zlar — Key vocabulary</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">a marked increase</div><div class="pp-card-back">sezilarli o'sish</div></div>
  <div class="pp-card"><div class="pp-card-front">to fluctuate</div><div class="pp-card-back">tebranib turmoq</div></div>
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
- **Reading:** step-reveal (strategiya/misol) + inline MCQ + flashcards (glossary).
- **Writing (Task 1/2):** step-reveal (namuna javobni bo'lib ko'rsatish) + flashcards
  (linking words/collocations).
- **Listening:** audio blok + MCQ + skript dropdown (5c-bo'limga qarang) + flashcards.
- **Speaking:** audio blok (savol + namunaviy javob) + step-reveal (javob formulasi) +
  flashcards (foydali iboralar).

---

## 5c. Listening darslari — audio bloklar

Listening darslari **haqiqiy audio** bilan keladi. Audio biz o'zimiz yozgan original
IELTS-uslub skriptlardan lokal ravishda sintez qilinadi (edge-tts) — rasmiy imtihon
audiosi ishlatilmaydi (mualliflik huquqi; rasmiy mock audio `exam` simulyatoriga tegishli).

**Speaker labels → voices** (see `gen_examprep_audio.py` VOICES dict):
`Woman` → en-GB-SoniaNeural, `Man` → en-GB-RyanNeural, `Woman2` → en-AU-NatashaNeural,
`Man2` → en-US-GuyNeural. Use exactly these labels in `audio_script` (case-sensitive) —
anything else silently falls back to the wrong (Korean) default voice.

> ⚠️ **Never put the speaker's name inside the spoken line.** The label (tuple's 1st
> element) only *chooses the voice*; it is not read aloud. Write `("Woman", "Hello,
> how can I help?")` — **NOT** `("Woman", "Sarah: Hello, how can I help?")`. Otherwise
> the narrator literally says "Sarah: hello". (The generator now strips a leading
> `Name:` as a safety net, but keep the text clean anyway.) Give characters names in
> the *rich_text* around the audio (form labels, the transcript dropdown), not in the
> `audio_script` text itself. The same rule applies to Corner dialogue narration.

**Which labels per Listening section (real IELTS structure — 4 sections, difficulty rises):**
- **Section 1** — everyday conversation, 2 speakers (e.g. booking/enquiry): `Woman` + `Man`.
- **Section 2** — monologue, everyday context (e.g. facilities talk): one voice, either
  `Man` or `Woman` (vary across lessons).
- **Section 3** — conversation, up to 4 speakers, educational context (e.g. students +
  tutor discussing an assignment): mix of all four (`Woman`, `Man`, `Woman2`, `Man2`).
- **Section 4** — academic monologue/lecture: one voice, usually `Man` or `Woman` (vary),
  longer and denser than Section 2.

**Audio blok formati** (data faylda):
```python
{
    "audio":        "ielts_l_010_1.mp3",   # fayl nomi: ielts_l_<lesson order 3 xonali>_<blok n>.mp3
    "audio_script": [                        # faqat authoring uchun — gen_examprep_audio o'qiydi
        ("Woman", "Good morning, City Library, how can I help you?"),
        ("Man",   "Hi, I'd like to renew my membership, please."),
    ],
    "rich_text":    "<p><strong>Amaliyot 1.</strong> Complete the form below. Write NO MORE THAN TWO WORDS for each answer.</p>",
    "choices":      [...],
    "explanation":  "... + skript dropdown (pastga qarang)",
}
```

**Skript (transkript) qoidasi — "avval eshiting":**
- MCQ (amaliyot) blokida to'liq skript + o'zbekcha tarjima **`explanation` ichida**
  `<details>` dropdown bo'lib turadi — talaba javob berganidan KEYIN ochiladi:
```html
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>Woman:</strong> Good morning, City Library, how can I help you?<br>
    <em style="color:#475569;">Xayrli tong, Siti kutubxonasi, sizga qanday yordam bera olaman?</em></p>
    ...
  </div>
</details>
```
- Tushuntirish (o'rgatish) blokidagi namuna-audio uchun skript dropdown `rich_text`ning
  o'zida, audio ostida turadi ("⚠️ Avval eshiting, keyin skriptni oching!" eslatmasi bilan).
- `explanation`da javobni beruvchi **skript qatorini** iqtibos qilib ko'rsating.

**Ishlab chiqarish tartibi (har partiya):**
1. `_lessons_ielts_listening_<topic>_<range>.py` yozish (audio_script bilan).
2. `python manage.py gen_examprep_audio <fayl> --out examprep/management/commands/audio/<topic>/`
3. mp3lar repoga commit qilinadi (production import ham o'sha papkadan oladi).
4. `python manage.py import_examprep <fayl> --author=<user> --audio-dir=<o'sha papka>`

**Skript yozish maslahatlari:** haqiqiy IELTS 듣기 kabi emas — inglizcha, tabiiy tezlikda,
qisqa aniq jumlalar; raqamlar, sana, ism-familiya va joy nomlarini aniq talaffuz uchun
to'liq yozing (masalan "double-o-seven" spelling out a reference number, "the third of
March" not "3/3"). Section 1–2 oson (2–4 replika/blok), Section 3 o'rta (4–6 replika,
fikr almashinuvi bilan), Section 4 qiyin (uzunroq monolog, akademik lug'at).

---

## 5d. Speaking darslari — savol + namunaviy javob audiolari

IELTS Speaking: 3 qism, ~11–14 daqiqa, band 0–9 (Fluency & Coherence, Lexical Resource,
Grammatical Range & Accuracy, Pronunciation — teng vaznda baholanadi). Har savol turi/qism
— alohida topic (`toc_ielts_speaking.txt`).

**Uch qism:**
1. **Part 1 — Introduction & Interview** (4–5 daqiqa): tanish mavzular (uy, ish/oʻqish,
   hobbi, oila) — qisqa savol-javob.
2. **Part 2 — Long Turn / Cue Card** (3–4 daqiqa): kartochka + 1 daqiqa tayyorgarlik + 2
   daqiqa toʻxtovsiz gapirish, keyin 1–2 follow-up savol.
3. **Part 3 — Discussion** (4–5 daqiqa): Part 2 mavzusi bilan bogʻliq abstrakt/tahliliy
   savollar, chuqurroq fikr talab qiladi.

**Audio bloklar ikki xil:**
1. **Savol audiosi** — imtihon nazoratchisi ovozi kabi: `("Woman", "So, let's move on to
   the topic of hobbies. What do you like to do in your free time?")`. `Woman` = examiner
   (savol), izchillik uchun har doim shu label.
2. **Namunaviy javob audiosi** — talaba SOYA QILIB (shadowing) takrorlaydi:
   `("Man", "Well, in my free time, I mostly...")`. `Man` = model candidate answer, har
   doim shu label. Javob transkripti + o'zbekcha tarjima `<details>` dropdownda ("Avval
   o'zingiz aytib ko'ring, keyin oching!").

**Dars tuzilishi:** kirish (topshiriq formati) → javob formulasi (step-reveal) → savol
audiosi + tayyorgarlik maslahatlari → namunaviy javob audiosi + skript → shadowing
ko'rsatmasi (3 kun × 3 marta — TOPIK'dagi kabi foydali metod) → MCQ (qaysi javob toʻgʻri
tuzilgan? qaysi ibora mos? qaysi javobda "band killer" xato bor?) → flashcards (foydali
iboralar/linking phrases).

Audio nomlash: `ielts_s_<order 3 xonali>_<blok n>.mp3`; papka:
`examprep/management/commands/audio/speaking_<topic>/`.

> ⚠️ MCQ **amaliyot** uchun (baholanmaydigan). To'g'ri javob HTML manbada ko'rinadi — bu
> normal. Baholanadigan, xronometrajli test — alohida `exam` ilovasi.

---

## 6. Foydalanuvchining IELTS maslahatlari (user's own tips)

_(Foydalanuvchi keyin oʻz IELTS maslahatlarini shu yerga qoʻshadi — ular umumiy
tavsiyalardan **ustun turadi**, uning soʻzlari va usullariga moslang.)_

---

## How to ask (foydalanuvchi nima yozadi)

Masalan:
- **"Make the next 5 IELTS reading lessons"** — Claude qaysi darslar borligini tekshiradi,
  tartibda davom etadi, partiyani yozadi va import qiladi.
- **"Make IELTS writing 1 to 6"** — aniq shu oraliqni.
- **"Redo IELTS Speaking 7"** — uni qayta yozadi (`--republish` bilan).

Claude qiladi: bu guide'ni oʻqiydi → kerakli `toc_ielts_<skill>.txt` ni oʻqiydi → bazadan
shu track+skill dagi eng katta `order` ni topadi → keyingi partiyani
`_lessons_ielts_<skill>_<range>.py` ga yozadi (Uzbek + English, rangli styling bilan) →
`python manage.py import_examprep <file> --author=<username>` ni ishga tushiradi (listening/
speaking uchun avval `gen_examprep_audio` + `--audio-dir`).
