from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice


QUESTIONS = [
{
'text': 'Mantiqiy masala (EKUB):Sinf rahbari 48 ta shokolad va 72 ta konfetdan oʻquvchilar uchun bir xil sovgʻalar tayyorlamoqchi. Har bir sovgʻada shokolad va konfetlar soni mos ravishda teng boʻlishi kerak. Eng koʻpi bilan nechta bir xil sovgʻa tayyorlash mumkin?',
'explanation': '24 toʻgʻri javob. Sovgʻalar soni eng koʻp boʻlishi uchun 48 va 72 sonlarining eng katta umumiy boʻluvchisini (EKUB) topishimiz kerak. 48 va 72 ning EKUBi 24 ga teng. Demak, 24 ta sovgʻa tayyorlash mumkin (har birida 2 ta shokolad va 3 ta konfet).',
'correct': '24',
'choices': ['12', '24', '48', '6']
},
{
'text': 'Mantiqiy masala (EKUK):Ikki avtobus yoʻnalish boshidan bir vaqtda yoʻlga chiqdi. Birinchi avtobus har 12 minutda, ikkinchisi esa har 18 minutda shu bekatga qaytib keladi. Ular yoʻlga chiqqandan keyin eng kamida necha minutdan soʻng yana ushbu bekatda uchrashadilar?',
'explanation': '36 toʻgʻri javob. Avtobuslarning bekatda qayta uchrashish vaqti 12 va 18 sonlarining eng kichik umumiy karralisi (EKUK) boʻladi. EKUK(12, 18) = 36. Demak, ular 36 minutdan keyin yana uchrashadilar.',
'correct': '36',
'choices': ['24', '36', '48', '72']
},
{
'text': 'Mantiqiy masala (EKUB):Duradgorda uzunligi 90 sm va 120 sm boʻlgan ikkita taxta bor. U taxtalarni hech qanday ortiqchasiz, eng katta va teng uzunlikdagi boʻlaklarga kesmoqchi. Har bir boʻlakning uzunligi necha sm boʻladi?',
'explanation': '30 toʻgʻri javob. Har bir boʻlakning uzunligi maksimal boʻlishi uchun 90 va 120 sonlarining EKUBini topamiz. 90 = 30 * 3 va 120 = 30 * 4. EKUB(90, 120) = 30 sm.',
'correct': '30',
'choices': ['15', '20', '30', '10']
},
{
'text': 'Mantiqiy masala (EKUK):Maydondagi ikkita chiroqdan biri har 8 sekundda, ikkinchisi esa har 14 sekundda yonib-oʻchadi. Ular bir vaqtda yongandan keyin, eng kamida necha sekunddan soʻng yana bir vaqtda yonadi?',
'explanation': '56 toʻgʻri javob. Chiroqlarning bir vaqtda yonish vaqti 8 va 14 sonlarining EKUKiga teng. 8 = 2^3 va 14 = 2 * 7. EKUK(8, 14) = 2^3 * 7 = 8 * 7 = 56 sekund.',
'correct': '56',
'choices': ['28', '42', '56', '112']
},
{
'text': 'Mantiqiy masala (EKUK):Kutubxonadagi kitoblarni 6 tadan qilib ham, 8 tadan qilib ham taxlaganda hech qaysi guruhda kitob ortib qolmadi. Kutubxonada eng kamida nechta kitob boʻlishi mumkin?',
'explanation': '24 toʻgʻri javob. Kitoblar soni 6 ga ham, 8 ga ham qoldiqsiz boʻlinishi kerak. Buning uchun ularning EKUKini topamiz: EKUK(6, 8) = 24.',
'correct': '24',
'choices': ['14', '24', '48', '16']
},
{
'text': 'Mantiqiy masala (EKUB):Doʻkonga 60 litr olma sharbati va 84 litr gilos sharbati olib kelindi. Ularni aralashtirmasdan, bir xil sigʻimdagi eng katta idishlarga toʻldirib chiqish uchun idishning sigʻimi necha litr boʻlishi kerak?',
'explanation': '12 toʻgʻri javob. Idish sigʻimi maksimal boʻlishi uchun 60 va 84 ning EKUBini topamiz. 60 = 12 * 5 va 84 = 12 * 7. EKUB(60, 84) = 12 litr.',
'correct': '12',
'choices': ['6', '12', '4', '24']
},
{
'text': 'Natural boʻluvchilar soni:120 sonining nechta natural boʻluvchisi bor?',
'explanation': '16 toʻgʻri javob. 120 sonini tub koʻpaytuvchilarga ajratamiz: 120 = 2^3 * 3^1 * 5^1. Natural boʻluvchilar sonini topish uchun daraja koʻrsatkichlariga 1 qoʻshib koʻpaytiramiz: (3+1) * (1+1) * (1+1) = 4 * 2 * 2 = 16.',
'correct': '16',
'choices': ['12', '14', '16', '20']
},
{
'text': 'Natural boʻluvchilar soni:100 sonining nechta natural boʻluvchisi bor?',
'explanation': '9 toʻgʻri javob. 100 sonini tub koʻpaytuvchilarga ajratamiz: 100 = 2^2 * 5^2. Boʻluvchilar soni formulasi boʻyicha: (2+1) * (2+1) = 3 * 3 = 9.',
'correct': '9',
'choices': ['6', '8', '9', '10']
},
{
'text': 'Boʻlinish alomatlari:Besh xonali 432X0 soni 9 ga qoldiqsiz boʻlinishi uchun X raqamining oʻrniga qaysi raqam qoʻyilishi kerak?',
'explanation': '9 toʻgʻri javob. Son 9 ga boʻlinishi uchun uning raqamlari yigʻindisi 9 ga boʻlinishi shart. Raqamlar yigʻindisi: 4+3+2+X+0 = 9 + X. Bu yigʻindi 9 ga boʻlinishi uchun X raqami 0 yoki 9 boʻlishi mumkin. Variantlar ichida 9 bor.',
'correct': '9',
'choices': ['3', '6', '8', '9']
},
{
'text': 'Tub sonlar va koʻpaytuvchilar:210 sonining nechta turli tub koʻpaytuvchisi bor?',
'explanation': '4 toʻgʻri javob. 210 sonini tub koʻpaytuvchilarga ajratamiz: 210 = 2 * 3 * 5 * 7. Demak, uning 4 ta turli tub koʻpaytuvchisi bor: 2, 3, 5 va 7.',
'correct': '4',
'choices': ['3', '4', '5', '6']
},
{
'text': 'Boʻlinish alomatlari:Toʻrt xonali 57X4 soni 4 ga qoldiqsiz boʻlinadi. X raqami qabul qilishi mumkin boʻlgan barcha raqamlarning yigʻindisini toping.',
'explanation': '20 toʻgʻri javob. Son 4 ga boʻlinishi uchun uning oxirgi ikkita raqamidan tuzilgan son 4 ga boʻlinishi kerak. X4 koʻrinishidagi sonlar: 04, 24, 44, 64, 84. Demak, X oʻrniga 0, 2, 4, 6, 8 qoʻyish mumkin. Ularning yigʻindisi: 0+2+4+6+8 = 20.',
'correct': '20',
'choices': ['15', '18', '20', '24']
},
{
'text': 'Mantiqiy boʻluvchilar:Faqatgina 3 ta natural boʻluvchiga ega boʻlgan sonlar qanday sonlar hisoblanadi?',
'explanation': 'Tub sonlarning kvadratlari toʻgʻri javob. Masalan, 4 sonining boʻluvchilari (1, 2, 4) - 3 ta; 9 sonining boʻluvchilari (1, 3, 9) - 3 ta; 25 sonining boʻluvchilari (1, 5, 25) - 3 ta. Bular tub sonlarning kvadratlaridir.',
'correct': 'Tub sonlarning kvadratlari',
'choices': ['Barcha tub sonlar', 'Juft sonlar', 'Tub sonlarning kvadratlari', 'Toq sonlar']
},
{
'text': 'Natural boʻluvchilar soni:60 sonining nechta natural boʻluvchisi bor?',
'explanation': '12 toʻgʻri javob. 60 = 2^2 * 3^1 * 5^1. Formula yordamida: (2+1) * (1+1) * (1+1) = 3 * 2 * 2 = 12 ta boʻluvchisi bor.',
'correct': '12',
'choices': ['8', '10', '12', '16']
},
{
'text': 'Qoldiqli boʻlish mantigʻi:Nomaʼlum sonni 7 ga boʻlganda qoldiq 4 ga teng chiqdi. Shu nomaʼlum sonni 2 barobar oshirib, keyin 7 ga boʻlinsa, qoldiq nechaga teng boʻladi?',
'explanation': '1 toʻgʻri javob. Sonni 2 barobar oshirganda, uning qoldigʻi ham 2 barobar oshadi: 4 * 2 = 8. Qoldiq boʻluvchidan (7 dan) katta boʻlishi mumkin emas, shuning uchun 8 ni 7 ga boʻlamiz va yakuniy qoldiq 1 ekanini topamiz.',
'correct': '1',
'choices': ['1', '2', '4', '0']
},
{
'text': 'Harakatga doir masala (Qarama-qarshi harakat):A va B shaharlar orasidagi masofa 450 km. Bir vaqtning oʻzida ikki avtomobil bir-biriga qarab yoʻlga chiqdi. Birinchisining tezligi 70 km/sh, ikkinchisining tezligi 80 km/sh. Ular necha soatdan keyin uchrashadilar?',
'explanation': '3 toʻgʻri javob. Avtomobillar bir-biriga qarab harakatlanayotganligi sababli yaqinlashish tezligi topiladi: 70 + 80 = 150 km/sh. Uchrashish vaqti: t = S / v = 450 / 150 = 3 soat.',
'correct': '3',
'choices': ['2', '3', '4', '5']
},
{
'text': 'Harakatga doir masala (Uzoqlashish):Ikki velosipedchi bir nuqtadan qarama-qarshi yoʻnalishda harakatni boshladi. Birinchisining tezligi 12 km/sh, ikkinchisining tezligi 15 km/sh. 4 soatdan keyin ular orasidagi masofa necha km boʻladi?',
'explanation': '108 toʻgʻri javob. Qarama-qarshi yoʻnalishda uzoqlashish tezligi: 12 + 15 = 27 km/sh. 4 soatdagi masofa: 27 * 4 = 108 km.',
'correct': '108',
'choices': ['96', '100', '108', '120']
},
{
'text': 'Harakatga doir masala (Oqim boʻylab):Katerning turgʻun suvdagi tezligi 18 km/sh, daryo oqimining tezligi esa 3 km/sh. Kater daryo oqimi boʻylab 3 soatda qancha masofani (km) bosib oʻtadi?',
'explanation': '63 toʻgʻri javob. Oqim boʻylab harakatlanganda kater tezligiga oqim tezligi qoʻshiladi: 18 + 3 = 21 km/sh. 3 soatda bosib oʻtilgan masofa: 21 * 3 = 63 km.',
'correct': '63',
'choices': ['45', '54', '60', '63']
},
{
'text': 'Harakatga doir masala (Oqimga qarshi):Kema daryo oqimiga qarshi suzmoqda. Kemaning xususiy tezligi 20 km/sh, daryo oqimining tezligi esa 4 km/sh. Kema daryo oqimiga qarshi 48 km masofani necha soatda bosib oʻtadi?',
'explanation': '3 toʻgʻri javob. Oqimga qarshi harakat tezligi: 20 - 4 = 16 km/sh. Vaqtni topish formulasi: t = S / v = 48 / 16 = 3 soat.',
'correct': '3',
'choices': ['2', '3', '4', '6']
},
{
'text': 'Harakatga doir masala (Quvib yetish):Tezligi 5 km/sh boʻlgan piyoda yoʻlga chiqqanidan soʻng, xuddi shu nuqtadan va shu yoʻnalishda tezligi 15 km/sh boʻlgan velosipedchi harakatni boshladi. Agar piyoda velosipedchidan 20 km oldinda boʻlsa, velosipedchi piyodani necha soatda quvib yetadi?',
'explanation': '2 toʻgʻri javob. Quvib yetish tezligi (tezliklar ayirmasi): 15 - 5 = 10 km/sh. Quvib yetish vaqti: t = S / v = 20 / 10 = 2 soat.',
'correct': '2',
'choices': ['1.5', '2', '3', '4']
},
{
'text': 'Harakatga doir masala (Oʻrtacha tezlik):Avtomobil yoʻlning birinchi 2 soatida 60 km/sh tezlik bilan, keyingi 3 soatida esa 80 km/sh tezlik bilan yurdi. Avtomobilning butun yoʻldagi oʻrtacha tezligini (km/sh) toping.',
'explanation': '72 toʻgʻri javob. Umumiy masofa: (2 * 60) + (3 * 80) = 120 + 240 = 360 km. Umumiy vaqt: 2 + 3 = 5 soat. Oʻrtacha tezlik: V_oʻrta = 360 / 5 = 72 km/sh.',
'correct': '72',
'choices': ['70', '72', '74', '75']
},
{
'text': 'Harakatga doir masala:Poyezd reja boʻyicha maʼlum masofani 60 km/sh tezlik bilan 4 soatda bosib oʻtishi kerak edi. Agar u shu masofani 3 soatda bosib oʻtishi kerak boʻlsa, tezligini necha km/sh ga oshirishi kerak?',
'explanation': '20 toʻgʻri javob. Jami masofa: 60 * 4 = 240 km. Masofani 3 soatda oʻtish uchun kerakli tezlik: 240 / 3 = 80 km/sh. Tezlikni oshirish miqdori: 80 - 60 = 20 km/sh.',
'correct': '20',
'choices': ['15', '20', '25', '80']
},
{
'text': 'Tezlik birliklari:Yuguruvchi 200 metr masofani 25 sekundda bosib oʻtdi. Uning tezligini m/s da aniqlang.',
'explanation': '8 toʻgʻri javob. Tezlikni topish uchun masofa vaqtga boʻlinadi: v = 200 / 25 = 8 m/s.',
'correct': '8',
'choices': ['6', '8', '10', '12']
},
{
'text': 'Kasrlar (Notoʻgʻri kasrni aralash songa aylantirish):37/5 notoʻgʻri kasrni aralash son koʻrinishida ifodalang.',
'explanation': '7 butun 2/5 toʻgʻri javob. 37 sonini 5 ga boʻlamiz: toʻliqsiz boʻlinma 7 (butun qism) va qoldiq 2 (surat) boʻladi. Maxraj oʻzgarmaydi. Natija: 7 butun 2/5.',
'correct': '7 butun 2/5',
'choices': ['6 butun 2/5', '7 butun 2/5', '7 butun 1/5', '5 butun 7/5']
},
{
'text': 'Kasrlar (Aralash sonni notoʻgʻri kasrga aylantirish):5 butun 4/7 aralash sonini notoʻgʻri kasr koʻrinishida yozing.',
'explanation': '39/7 toʻgʻri javob. Aralash sonni notoʻgʻri kasrga aylantirish uchun butun qism maxrajga koʻpaytirilib, surat qoʻshiladi: 5 * 7 + 4 = 35 + 4 = 39. Bu surat boʻladi, maxraj esa oʻzgarishsiz qoladi: 39/7.',
'correct': '39/7',
'choices': ['35/7', '39/7', '43/7', '29/7']
},
{
'text': 'Kasrlar mantigʻi:Bir kasrning surati maxrajidan 5 ga kam. Agar surat va maxrajning yigʻindisi 23 ga teng boʻlsa, ushbu kasrni toping.',
'explanation': '9/14 toʻgʻri javob. Maxrajni X deb olsak, surat X - 5 boʻladi. Ularning yigʻindisi: X + X - 5 = 23 -> 2X = 28 -> X = 14 (maxraj). Surat: 14 - 5 = 9. Kasr 9/14 ga teng.',
'correct': '9/14',
'choices': ['7/16', '9/14', '8/15', '10/13']
},
{
'text': 'Kasrlarni taqqoslash:Quyidagi kasrlardan qaysi biri eng katta?',
'explanation': '3/4 toʻgʻri javob. Kasrlarni taqqoslash uchun umumiy maxrajga keltiramiz yoki oʻzaro solishtiramiz. 3/4 = 0.75; 5/7 ≈ 0.714; 1/2 = 0.5; 5/8 = 0.625. Koʻrinib turibdiki, 3/4 eng kattasi.',
'correct': '3/4',
'choices': ['1/2', '5/7', '3/4', '5/8']
},
{
'text': 'Kasrlar ustida amallar:Hisoblang: 11/15 - 4/15 + 2/15 ifodaning qiymatini toping.',
'explanation': '3/5 toʻgʻri javob. Maxrajlar bir xil boʻlgani uchun suratlar ustida amallar bajariladi: (11 - 4 + 2) / 15 = 9/15. Bu kasrni 3 ga qisqartirsak, 3/5 hosil boʻladi.',
'correct': '3/5',
'choices': ['9/15', '3/5', '7/15', '1/3']
},
{
'text': 'Aralash sonlarni qoʻshish:Amalni bajaring: 3 butun 2/9 + 4 butun 5/9',
'explanation': '7 butun 7/9 toʻgʻri javob. Aralash sonlarni qoʻshishda butun qismlar alohida, kasr qismlar alohida qoʻshiladi: (3 + 4) + (2/9 + 5/9) = 7 + 7/9 = 7 butun 7/9.',
'correct': '7 butun 7/9',
'choices': ['7 butun 7/9', '8 butun 7/9', '7 butun 2/9', '12 butun 7/9']
},
{
'text': 'Aralash sonlarni ayirish (qarz olish):Amalni bajaring: 5 butun 1/6 - 2 butun 5/6',
'explanation': '2 butun 2/6 toʻgʻri javob. 1/6 dan 5/6 ni ayirib boʻlmagani uchun butun qismdan 1 qarz olamiz: 5 butun 1/6 = 4 butun 7/6. Endi ayiramiz: 4 butun 7/6 - 2 butun 5/6 = 2 butun 2/6 (yoki qisqartirilganda 2 butun 1/3).',
'correct': '2 butun 2/6',
'choices': ['3 butun 4/6', '2 butun 2/6', '2 butun 4/6', '3 butun 2/6']
},
{
'text': 'Sonning kasrini topish:Sinfdagi 42 ta oʻquvchining 3/7 qismi matematika toʻgaragiga qatnashadi. Nechta oʻquvchi matematika toʻgaragiga qatnashadi?',
'explanation': '18 toʻgʻri javob. Sonning kasrini topish uchun sonni kasrning maxrajiga boʻlib, suratiga koʻpaytiramiz: 42 / 7 * 3 = 6 * 3 = 18.',
'correct': '18',
'choices': ['12', '16', '18', '24']
},
{
'text': 'Kasriga koʻra sonni topish:Kitobning 4/9 qismi oʻqilganda 36 sahifa boʻldi. Kitob jami necha sahifadan iborat?',
'explanation': '81 toʻgʻri javob. Kasriga koʻra sonni topish uchun berilgan qiymatni suratga boʻlib, maxrajga koʻpaytiramiz: 36 / 4 * 9 = 9 * 9 = 81 sahifa.',
'correct': '81',
'choices': ['72', '81', '90', '64']
},
{
'text': 'Kasrlar bilan bogʻliq mantiqiy masala:Hovuzning 3/8 qismi suv bilan toʻldirilgan. Agar hovuzga yana 15 litr suv quyilsa, hovuz toʻladi. Hovuzning jami sigʻimi necha litr?',
'explanation': '24 toʻgʻri javob. Hovuzning boʻsh qismi kasr koʻrinishida: 1 - 3/8 = 5/8 qism. Demak, hovuzning 5/8 qismi 15 litrga teng. Jami sigʻimni topish uchun: 15 / 5 * 8 = 3 * 8 = 24 litr.',
'correct': '24',
'choices': ['24', '32', '40', '48']
},
{
'text': 'Geometrik mantiqiy masala:Toʻgʻri toʻrtburchakning perimetri 30 sm ga teng. Agar uning boʻyi 9 sm boʻlsa, ushbu toʻgʻri toʻrtburchakning yuzini (sm²) toping.',
'explanation': '54 toʻgʻri javob. Perimetr formulasi: P = 2 * (a + b). 30 = 2 * (9 + b) -> 9 + b = 15 -> b = 6 sm (eni). Yuzi: S = a * b = 9 * 6 = 54 sm².',
'correct': '54',
'choices': ['45', '54', '60', '63']
},
{
'text': 'Yoshga doir mantiqiy masala:Ota 36 yoshda, oʻgʻil esa 8 yoshda. Necha yildan keyin ota oʻgʻlidan 3 barobar katta boʻladi?',
'explanation': '6 toʻgʻri javob. X yildan keyin otaning yoshi 36 + X, oʻgʻilning yoshi 8 + X boʻladi. Tenglama tuzamiz: 36 + X = 3 * (8 + X) -> 36 + X = 24 + 3X -> 2X = 12 -> X = 6 yil.',
'correct': '6',
'choices': ['4', '5', '6', '7']
},
{
'text': 'Mantiqiy masala (Yigʻindi va ayirma):Ikki sonning yigʻindisi 84 ga, ularning ayirmasi esa 16 ga teng. Shu sonlardan kattasini toping.',
'explanation': '50 toʻgʻri javob. Katta sonni topish uchun yigʻindi va ayirma qoʻshilib 2 ga boʻlinadi: (84 + 16) / 2 = 100 / 2 = 50. (Kichik son 34 boʻladi).',
'correct': '50',
'choices': ['45', '48', '50', '52']
},
{
'text': 'Tenglama yechish:Tenglamani yeching: 5x - 12 = 38',
'explanation': '10 toʻgʻri javob. 5x = 38 + 12 -> 5x = 50 -> x = 50 / 5 -> x = 10.',
'correct': '10',
'choices': ['8', '9', '10', '12']
},
{
'text': 'Mantiqiy masala (Teskari proporsiya):3 ta ishchi maʼlum bir ishni 6 kunda bajarib tugatadi. Agar ishchilar soni 9 ta boʻlsa, shu ishni necha kunda bajarishadi?',
'explanation': '2 toʻgʻri javob. Ishchilar soni koʻpaysa, ishga ketadigan vaqt kamayadi (teskari proporsiya). Jami ish hajmi: 3 * 6 = 18 odam-kun. 9 ta ishchi uchun: 18 / 9 = 2 kun kerak boʻladi.',
'correct': '2',
'choices': ['2', '3', '4', '18']
},
{
'text': 'Mantiqiy ketma-ketlik:Quyidagi qonuniyatga qarab boʻsh oʻringa mos sonni toping: 2, 5, 11, 23, ...',
'explanation': '47 toʻgʻri javob. Ketma-ketlikdagi har bir son oʻzidan oldingi sonni 2 ga koʻpaytirib, 1 qoʻshish orqali hosil boʻlyapti: 2*2+1=5; 5*2+1=11; 11*2+1=23. Keyingi son: 23*2+1 = 47.',
'correct': '47',
'choices': ['35', '45', '46', '47']
},
{
'text': 'Dirixle prinsipi / Mantiqiy masala:Qutida 6 ta qizil va 8 ta koʻk shar bor. Qutiga qaramasdan, eng kamida nechta shar olganda ularning ichida albatta kamida bitta qizil shar boʻlishi kafolatlanadi?',
'explanation': '9 toʻgʻri javob. Eng yomon holatni tasavvur qilamiz: ketma-ket olgan dastlabki 8 ta sharimizning barchasi koʻk boʻlib chiqdi. Shundan keyin olinadigan 9-shar albatta qizil boʻladi. Demak, 9 ta shar olish kerak.',
'correct': '9',
'choices': ['7', '8', '9', '14']
},
{
'text': 'Toʻplamlar mantiqi:25 ta oʻquvchisi bor sinfda 15 ta oʻquvchi matematika toʻgaragiga, 12 tasi esa ingliz tili toʻgaragiga qatnashadi. 5 ta oʻquvchi har ikkala toʻgarakka qatnashsa, sinfda nechta oʻquvchi umuman toʻgaraklarga qatnashmaydi?',
'explanation': '3 toʻgʻri javob. Kamida bitta toʻgarakka qatnashadigan oʻquvchilar sonini topamiz: 15 + 12 - 5 = 22 ta oʻquvchi. Toʻgaraklarga qatnashmaydiganlar oʻquvchilar: 25 - 22 = 3 ta.',
'correct': '3',
'choices': ['2', '3', '5', '8']
}
]


class Command(BaseCommand):
    help = 'Create a math practice test'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign this practice to')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options['master'])
        except User.DoesNotExist:
            raise CommandError(f"User '{options['master']}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{options['master']}'.")

        subject, _ = Subject.objects.get_or_create(
            name='math',  # --- IGNORE ---
            defaults={'description': 'Math practice problems'},
        )

        practice, created = Practice.objects.get_or_create(
            title='math 5th grade all',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Let\'s practice some math problems to improve your skills.',  # --- IGNORE ---
                'subject': subject,
                'level': 'medium',
                'is_free': True,
                'is_published': True,
                'is_available_for_all': True,
                'pass_score': 70,
                'max_attempts': 0,
                'show_answers_after': True,
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
            ))
            return

        for i, q in enumerate(QUESTIONS, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q['text'],
                explanation=q['explanation'],
                order=i,
                points=1,
            )
            for choice_text in q['choices']:
                PracticeChoice.objects.create(
                    question=question,
                    text=choice_text,
                    is_correct=(choice_text == q['correct']),
                )

        self.stdout.write(self.style.SUCCESS(
            f"Created practice '{practice.title}' with {len(QUESTIONS)} questions (id={practice.pk})."
        ))
