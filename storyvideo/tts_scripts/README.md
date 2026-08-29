# tts_scripts/ — TTS matnlari

`python3 cli.py script <slug> --one --ssml` shu yerga yozadi.

- **`<slug>_tts_one.txt`** — joriy matn. Saytga shuni qoʻying.
  Sozlamalar: **Speed +26%, Pitch +10%**. Chegara: 2000 belgi (SSML teglari ham sanaladi).
- **`<slug>_tts_recorded.txt`** — oʻsha video AYNAN qaysi matndan yozib olingani.
  `voice` buyrugʻiga `--script` sifatida **shuni** berish kerak: tanaffus qiymatlari
  audiodagi haqiqiy pauzalarga mos keladi, va split shu asosda kesadi.

Nega ikkitasi bor: 2026-08-29 da sahna tanaffusi 1,5s dan 2,5s ga kengaytirildi.
pm04·pm08·pm12·pm25·pm67·pm92 undan OLDIN yozib olingan, shuning uchun ularning
`_recorded` nusxasi eski qiymatlarni saqlaydi. Yangi yozuvlar uchun ikkalasi bir xil.

## pm04 da nega `_recorded` yoʻq

pm04 ning audiosi 01:26 da yozib olingan, undan keyin matn ikki marta oʻzgargan
(«dedi u» olib tashlandi, tanaffuslar kengaytirildi) — va yozuvdan oldingi
aynan qaysi matn ishlatilgani saqlanmagan. Taxminiy nusxani «recorded» deb
atash xato boʻlardi, shuning uchun yaratilmadi. pm04 allaqachon render
qilingan; qayta kerak boʻlsa `pm04_tts_one.txt` bilan ham split ishlaydi,
faqat tanaffus qiymatlari biroz farq qiladi.

## Nega `scripts/` emas, `tts_scripts/`

Repodagi venv gitignore blokida yalangʻoch `[Ss]cripts` qoidasi bor (Windows
virtualenv papkasi uchun), shuning uchun `scripts/` degan papka git uchun
koʻrinmas boʻlib qolardi. `tts_scripts/` esa `tts_audios/` bilan juft boʻladi:
biri matn, ikkinchisi ovoz.
