# TOPIK II Reading — 42–43-savollar: Adabiy matn (소설·심정), lessons 1–2 (orders 140–141).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_novel_1_2.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "42–43-savollar: Adabiy matn (소설·심정)",
    "summary": "Hikoya-qissa parchasida qahramon his-tuyg'usini va voqea tafsilotlarini o'qish.",
    "icon":    "bi-book-half",
    "order":   16,
}

LESSONS = [
    # ── Lesson 1 (order 140) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 소설 1: 42–43-savollar bilan tanishuv — adabiy his-tuyg'ular",
        "summary": "Adabiy parcha 23–24-savollardan nimasi bilan farq qiladi va nozik his-tuyg'u lug'ati.",
        "order":   140,
        "blocks": [
            {"rich_text": """
<h2>📖 42–43-savollar: badiiy parcha</h2>
<p>Bu blokda roman, qissa yoki esse'dan <strong>badiiy parcha</strong> beriladi. Savollar
23–24-savollardagidek: <strong>42</strong> — chizilgan qismdagi qahramon his-tuyg'usi,
<strong>43</strong> — mazmunga mos gap. Farqi — matnning "adabiyligi"da:</p>
<ul>
  <li><strong>Dialog va xatti-harakat ko'p:</strong> his-tuyg'u "aytilmaydi" — yuz ifodasi,
  sukut, mayda ish-harakatlar orqali <em>chiziladi</em>.</li>
  <li><strong>Xotira (회상):</strong> hikoya o'tmishga sakrashi mumkin — "어릴 때..." (bolaligimda).</li>
  <li><strong>His-tuyg'u nozikroq:</strong> shunchaki "xafa" emas — "ich-ichidan achinish",
  "gina", "huvillash"... Variantlar ham shunga mos, boyroq lug'atdan keladi.</li>
</ul>
<h3>Yangi daraja his-tuyg'u lug'ati</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>뭉클하다</strong> — yuragi jiz etmoq (iliq ta'sirlanish) · <strong>먹먹하다</strong> — ko'ksi to'lib, gap chiqmay qolmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>허전하다</strong> — huvillagan his (nimadir yetishmayapti) · <strong>후련하다</strong> — ichi bo'shab, yengil tortmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>안쓰럽다</strong> — rahmi kelmoq (mehr bilan achinish) · <strong>원망스럽다</strong> — gina-alam his qilmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>조마조마하다</strong> — yuragi po'killab turmoq · <strong>얼떨떨하다</strong> — garang, o'ziga kelolmay</p>
  <p style="font-size:1.05em;margin:0;"><strong>멋쩍다</strong> — noqulay, o'ng'aysiz sezmoq · <strong>못마땅하다</strong> — ko'ngliga yoqmay, norozi</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul o'sha-o'sha (23–24-darslardan):</strong> chizilgan joygacha nima bo'ldi? →
  musbat yoki manfiy? → aniq tus. Faqat endi "voqea"ni dialog va mayda harakatlardan
  yig'asiz: "아무 말씀도 하지 않으셨다" (indamadi) ham voqea!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Vaziyatga mos his-tuyg'uni tanlang.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0;line-height:1.8;"><strong>이십 년 만에 초등학교 동창을
  길에서 우연히 만났다. 이름을 부르며 손을 잡는데 나도 모르게 가슴이 뭉클했다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Yigirma yildan keyin boshlang'ich sinfdoshimni
  ko'chada tasodifan uchratdim. Ismini aytib qo'lини ushlaganimda, bilmagan holda yuragim jiz etdi.</em></p>
</div>
<p>가슴이 뭉클했다 — bu qanday his?</p>
""",
             "choices": [
                 {"text": "반갑고 감동적인 마음 (quvonchli, iliq ta'sirlangan his)", "is_correct": True},
                 {"text": "화가 나는 마음 (jahli chiqqan his)", "is_correct": False},
                 {"text": "무섭고 불안한 마음 (qo'rquv va bezovtalik)", "is_correct": False},
                 {"text": "지루하고 심심한 마음 (zerikkan his)", "is_correct": False},
             ],
             "explanation": """
<p><strong>뭉클하다</strong> = biror narsa yurakni "iliq siqib" yuborishi — sog'inch, mehr,
ta'sirlanish aralash ijobiy his ✅. 20 yillik ayriliq + kutilmagan uchrashuv = aynan shu.
Adabiy matnda 가슴이/코끝이 (yurak/burun uchi) bilan boshlangan iboralar deyarli doim
<strong>ta'sirlanish</strong> oilasidan: 가슴이 뭉클하다, 가슴이 먹먹하다, 코끝이 찡하다.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Vaziyatga mos his-tuyg'uni tanlang.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0;line-height:1.8;"><strong>자식들이 모두 도시로 떠난 뒤,
  어머니는 빈방마다 불을 켜 보았다가 다시 끄곤 하셨다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Farzandlari hammasi shaharga ketganidan keyin, ona
  bo'sh xonalarning chirog'ini yoqib ko'rib, yana o'chirib yurar edi.</em></p>
</div>
<p>어머니의 심정은?</p>
""",
             "choices": [
                 {"text": "허전하다 (huvillagan, ko'ngli bo'shab qolgan)", "is_correct": True},
                 {"text": "후련하다 (yengil tortgan)", "is_correct": False},
                 {"text": "못마땅하다 (norozi)", "is_correct": False},
                 {"text": "조마조마하다 (yuragi po'killagan)", "is_correct": False},
             ],
             "explanation": """
<p>Harakatni o'qiymiz: bo'sh xonalar chirog'ini <strong>yoqib-o'chirib yurish</strong> —
maqsadsiz, odatdan chiqolmagan harakat: bolalar yo'q, lekin qo'l hamon ularni "izlaydi" →
<mark style="background:#dcfce7;">허전하다</mark> ✅ (huvillash — nimadir/kimdir yetishmasligi).
② 후련하다 teskari (yuk tushib yengillashish); "bolalar ketdi — yengil tortdi" bu matnning
ohangiga zid: 곤 하셨다 (takror odat — his uzoq davom etyapti).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">뭉클하다</div><div class="pp-card-back">yuragi jiz etmoq (+)</div></div>
  <div class="pp-card"><div class="pp-card-front">먹먹하다</div><div class="pp-card-back">ko'ksi to'lib qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">허전하다</div><div class="pp-card-back">huvillagan his</div></div>
  <div class="pp-card"><div class="pp-card-front">후련하다</div><div class="pp-card-back">ichi bo'shab yengil tortmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">안쓰럽다</div><div class="pp-card-back">rahmi kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">원망스럽다</div><div class="pp-card-back">gina qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">조마조마하다</div><div class="pp-card-back">yuragi po'killamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">멋쩍다</div><div class="pp-card-back">o'ng'aysiz sezmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">못마땅하다</div><div class="pp-card-back">norozi, yoqtirmay</div></div>
  <div class="pp-card"><div class="pp-card-front">얼떨떨하다</div><div class="pp-card-back">garang bo'lib qolmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>42–43 = 23–24ning adabiy darajasi: his dialog, sukut va mayda harakatlardan o'qiladi.</li>
  <li>가슴이/코끝이 iboralari — ta'sirlanish; maqsadsiz takror harakat — huvillash/sog'inch.</li>
  <li>Yangi lug'atni obraz bilan yodlang: 허전 (bo'sh xona), 조마조마 (po'killagan yurak).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 141) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 소설 2: To'liq amaliyot — badiiy parcha + ikki savol",
        "summary": "Imtihon formatidagi ikkita badiiy parcha: his-tuyg'u (42-tur) va mazmun (43-tur) savollari.",
        "order":   141,
        "blocks": [
            {"rich_text": """
<h2>🏁 Badiiy parcha — imtihon rejimi</h2>
<p>Ish tartibi: parchani <strong>voqealar zanjiri</strong> sifatida o'qing (kim nima qildi),
chizilgan joyda to'xtab "hozir unga qanday?" deb so'rang, keyin 43ni 소거법 bilan yeching.
Dialogdagi gaplar ham fakt — 43-savol ularni ham tekshiradi!</p>
"""},
            {"rich_text": """
<h3>1-parcha</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">어릴 때 나는 시골 할머니 댁에서 자랐다.
  부모님이 도시에서 일하셨기 때문이다. 할머니는 매일 새벽마다 시장에 나가 나물을 파셨다.
  나는 그런 할머니가 창피해서 친구들에게 할머니 이야기를 하지 않았다. 어느 날 학교 앞에서
  나물 바구니를 든 할머니와 마주쳤을 때도 나는 모른 척 지나가 버렸다. 그런데 그날 밤
  할머니는 아무 말씀도 없이 내가 좋아하는 반찬만 밥상에 올려 주셨다. <u>나는 이불 속에서
  소리를 죽여 울었다.</u></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Bolaligimda men qishloqda buvimning uyida o'sganman.
  Ota-onam shaharda ishlagani uchun. Buvim har kuni saharda bozorga chiqib ko'kat sotardi. Men bunday
  buvimdan uyalib, do'stlarimga u haqda gapirmasdim. Bir kuni maktab oldida ko'kat savati ko'targan
  buvimga duch kelganimda ham o'zimni tanimaganlikka solib o'tib ketdim. Lekin o'sha kecha buvim hech
  narsa demay, dasturxonga men yaxshi ko'radigan taomlarnigina tortdi. <u>Men ko'rpa ichida ovozimni
  chiqarmay yig'ladim.</u></em></p>
</div>
<p><strong>Amaliyot 1 (42-tur).</strong> 밑줄 친 부분에 나타난 '나'의 심정으로 가장 알맞은 것을 고르십시오.</p>
""",
             "choices": [
                 {"text": "죄송하고 후회스럽다 (aybdorlik va pushaymonlik)", "is_correct": True},
                 {"text": "자랑스럽고 뿌듯하다 (g'urur va faxr)", "is_correct": False},
                 {"text": "후련하고 홀가분하다 (yengil tortgan)", "is_correct": False},
                 {"text": "무섭고 두렵다 (qo'rquv)", "is_correct": False},
             ],
             "explanation": """
<p>Voqealar zanjiri: buvidan uyaldim → tanimaganlikka soldim → buvi <strong>indamay</strong>,
sevimli taomimni qo'ydi (so'zsiz mehr!) → ko'rpada yashirin yig'i. Kimdir sizga yomonlik
o'rniga mehr ko'rsatsa-yu, siz unga nohaqlik qilgan bo'lsangiz — bu
<mark style="background:#dcfce7;">aybdorlik va pushaymonlik</mark> yig'isi ✅.
"소리를 죽여" (ovozini o'chirib) — yashirin, ichki azob belgisi. Buvining sukuti bu yerda
eng kuchli "gap"!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (43-tur).</strong> 윗글의 내용과 같은 것을 고르십시오. (parcha yuqorida)</p>
""",
             "choices": [
                 {"text": "할머니는 시장에서 나물을 파셨다. (Buvim bozorda ko'kat sotardi.)", "is_correct": True},
                 {"text": "나는 도시에서 부모님과 함께 자랐다. (Men shaharda ota-onam bilan o'sganman.)", "is_correct": False},
                 {"text": "할머니는 그날 밤 나를 크게 혼내셨다. (Buvim o'sha kecha meni qattiq urishdi.)", "is_correct": False},
                 {"text": "나는 친구들에게 할머니 이야기를 자주 했다. (Men do'stlarimga buvim haqida tez-tez gapirardim.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari — qishloqda <strong>buvim bilan</strong> o'sganman (ota-onam shaharda
ishlagan). ③ teskari — 아무 말씀도 <strong>없이</strong> (hech narsa demay). ④ teskari —
이야기를 하지 <strong>않았다</strong>. To'g'risi ①: "시장에 나가 나물을 파셨다"ning o'zi ✅.
Badiiy matnda ham tuzoqlar o'sha-o'sha — faqat faktlar hikoya ichiga singdirilgan.</p>
"""},
            {"rich_text": """
<h3>2-parcha</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">아버지는 삼십 년 동안 택시를 모셨다.
  지난달 아버지가 마지막 운행을 마치신 날, 가족들은 작은 잔치를 열어 그동안의 수고를
  축하해 드렸다. 아버지는 웃으시며 "이제 좀 쉬어야지" 하셨다. 그런데 다음 날 새벽, 아버지는
  여느 때처럼 일찍 일어나 외출복으로 갈아입으셨다. <u>그러고는 현관 앞에서 한참을 그냥
  서 계셨다.</u> 그 뒷모습을 보며 나는 아무 말도 할 수 없었다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Otam o'ttiz yil taksi haydadi. O'tgan oy otam so'nggi
  qatnovини tugatgan kuni, oilamiz kichik ziyofat qilib, shuncha yillik mehnatini tabrikladik. Otam
  kulib "endi biroz dam olay" dedi. Lekin ertasi kuni saharda otam odatdagidek erta turib, ko'cha
  kiyimini kiyib oldi. <u>So'ng eshik oldida ancha vaqt shunchaki turib qoldi.</u> O'sha qaddi-qomatga
  orqadan qarab, men hech narsa deyolmadim.</em></p>
</div>
<p><strong>Amaliyot 3 (42-tur).</strong> 밑줄 친 부분에 나타난 아버지의 심정으로 가장 알맞은 것을 고르십시오.</p>
""",
             "choices": [
                 {"text": "허전하다 (huvillagan, bo'shliq his qilgan)", "is_correct": True},
                 {"text": "신이 나다 (ko'tarinki, xursand)", "is_correct": False},
                 {"text": "무섭다 (qo'rqqan)", "is_correct": False},
                 {"text": "부럽다 (havas qilgan)", "is_correct": False},
             ],
             "explanation": """
<p>Harakatni o'qiymiz: 30 yillik odat — saharda turish, kiyinish... lekin endi
<strong>boradigan joy yo'q</strong>. Eshik oldida "shunchaki turib qolish" — hayotining katta
qismi tugaganini his qilish → <mark style="background:#dcfce7;">허전하다</mark> ✅
(1-darsdagi bo'sh xonalar obrazi bilan bir oila!). Og'zida "dam olay" degan, tanasi esa
hali ham ishga otlanadi — adabiy matn ana shu <strong>so'z va harakat zidligi</strong>
orqali gapiradi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 4 (43-tur).</strong> 윗글의 내용과 같은 것을 고르십시오. (parcha yuqorida)</p>
""",
             "choices": [
                 {"text": "가족들은 아버지의 은퇴를 축하해 드렸다. (Oila otamning nafaqaga chiqishini tabrikladi.)", "is_correct": True},
                 {"text": "아버지는 아직도 택시를 몰고 계신다. (Otam hali ham taksi haydaydi.)", "is_correct": False},
                 {"text": "아버지는 다음 날 늦잠을 주무셨다. (Otam ertasi kuni uxlab qoldi.)", "is_correct": False},
                 {"text": "나는 아버지에게 화를 냈다. (Men otamga jahl qildim.)", "is_correct": False},
             ],
             "explanation": """
<p>② "마지막 운행을 <strong>마치신</strong>" — tugatgan (hali haydamaydi). ③ teskari:
여느 때처럼 <strong>일찍 일어나</strong> (odatdagidek erta turdi). ④ matnda yo'q — men
"hech narsa deyolmadim" (his-tuyg'udan, jahldan emas). To'g'risi ①: "잔치를 열어 ...
축하해 드렸다" = nafaqani (은퇴) tabriklash ✅. Tabriklaymiz — adabiy matnlar ham
qo'lingizda! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">마주치다</div><div class="pp-card-back">duch kelmoq, to'qnash kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">모른 척하다</div><div class="pp-card-back">tanimaganlikka solmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">소리를 죽이다</div><div class="pp-card-back">ovozini o'chirmoq (yashirincha)</div></div>
  <div class="pp-card"><div class="pp-card-front">은퇴</div><div class="pp-card-back">nafaqaga chiqish</div></div>
  <div class="pp-card"><div class="pp-card-front">여느 때처럼</div><div class="pp-card-back">odatdagidek</div></div>
  <div class="pp-card"><div class="pp-card-front">뒷모습</div><div class="pp-card-back">orqa ko'rinish, qaddi-qomat</div></div>
  <div class="pp-card"><div class="pp-card-front">수고</div><div class="pp-card-back">mehnat, zahmat</div></div>
  <div class="pp-card"><div class="pp-card-front">잔치</div><div class="pp-card-back">ziyofat, bayram</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Badiiy matnda his-tuyg'u <strong>sukut, takror odat va so'z-harakat zidligi</strong>dan o'qiladi.</li>
  <li>Chizilgan joygacha voqealar zanjirini yig'ing — his o'sha zanjirning natijasi.</li>
  <li>43-savol uchun dialog ichidagi gaplar ham fakt; tuzoqlar o'sha 4 tur.</li>
</ul>
"""},
        ],
    },
]
