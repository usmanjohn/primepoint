"""BPMN «As Is» of the Управление отчётности и мониторинга данных.

    python3 kapital/bpmn/build_bpmn.py

writes kapital/bpmn/out/:
    BPMN_Upravlenie_otchetnosti.vsdx   — open in Visio, one tab per process
    BPMN_Upravlenie_otchetnosti.pdf    — the same pictures for reading
    BPMN_Reestr_shagov.xlsx            — every step: № · step · role · system · note

Everything marked [уточнить] is a guess to confirm with the team.
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bpmnkit import (Diagram, Shape, C, TH, rect_geom, line, text, svg_page,  # noqa: E402
                     write_vsdx)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
DATE = '13.11.2026'
UNIT = 'Управление отчётности и мониторинга данных'
DEPT = 'Департамент [уточнить]'
OWNER = 'Начальник управления отчётности и мониторинга данных – Обидов Б.'
DEV = 'Абдураимов У. – ведущий специалист управления отчётности и мониторинга данных'

TERMS_ALL = {
    'АБС Б2': 'автоматизированная банковская система B2NG, первоисточник данных по сделкам и обеспечению',
    'DWH': 'хранилище данных банка; выгрузка SQL-скриптами',
    'Power BI': 'каталог отчётов bi.kapitalbank.uz (веб-дашборды для скачивания данных)',
    'SQL/Python': 'скрипты выгрузки и автоматизации расчётов',
    'NPL': 'проблемные кредиты (просрочка свыше 90 дней) [уточнить критерий]',
    'PAR': 'портфель под риском (доля кредитов с просрочкой)',
    'Резерв': 'резерв на возможные убытки по кредитам',
    'АКР': '[уточнить полное наименование отчёта]',
    'Сальдо 945%%': 'остатки на внебалансовых счетах учёта обеспечения',
    'Декада': 'период в 10 дней; рассылка по итогам каждой декады',
    'Реестр ошибок': 'общий файл управления с выявленными расхождениями и статусом исправления',
    'Реестр запросов': 'учёт поступивших запросов: заказчик, срок, исполнитель, статус',
}


def terms(*keys):
    return [(k, TERMS_ALL[k]) for k in keys]


def passport(no, name):
    return [('Название БП', f'{no}. {name}'), ('Модель', 'As Is'),
            ('Номенклатурный номер', f'{no} [уточнить номер департамента]'),
            ('Статус', f'в разработке с {DATE} г.'), ('Владелец', OWNER), ('Разработчик', DEV)]


R_HEAD = ('Начальник управления', 'Обидов Б.: распределяет задачи, ежемесячная отчётность, АКР, презентации, контроль качества')
R_TOIROV = ('Главный специалист (обеспечение)', 'Тоиров Ж.: данные по обеспечению, сверка DWH ↔ АБС Б2')
R_MUKH = ('Главный специалист (портфель)', 'Мухаммадиев А.: ежедневный портфель, доля NPL, сверка с балансом и резервами')
R_AUTO = ('Ведущий специалист (автоматизация)', 'Абдураимов У.: автоматизация отчётов и проверок (Python, SQL, Excel)')
R_DIR = ('Директор департамента', 'получатель отчётов, заказчик срочных запросов, уровень эскалации')
R_RESP = ('Ответственные подразделения', 'филиалы и подразделения, которые вводят данные в АБС Б2 и исправляют ошибки')
R_CUST = ('Заказчик', 'директор департамента или другое подразделение, направившее запрос')
R_IT = ('ИТ / администраторы DWH', 'выдают доступы к данным и сопровождают DWH')


# ======================================================================= 1.1
def p_daily():
    d = Diagram('1.1 Ежедневный портфель',
                passport('1.1', 'Подготовка ежедневного отчёта по кредитному портфелю'),
                [R_MUKH, R_HEAD, R_RESP, R_DIR],
                terms('DWH', 'Power BI', 'АБС Б2', 'NPL', 'PAR', 'Резерв', 'Реестр ошибок'),
                UNIT, ['Директор департамента', ('Главный специалист\n(Мухаммадиев А.)', 66),
                       'Ответственные подразделения', 'Начальник управления'], ncols=13)
    M, R, H, D = 1, 2, 3, 0
    d.event('s', M, 0, 'timer_start', 'Каждый рабочий день, утро [уточнить время]')
    d.task('t1', M, 1, '1.1.1. Выгрузить кредитный портфель на отчётную дату', 'DWH · SQL-скрипт',
           note='Остатки ОД, просрочка,\nдни просрочки, резерв,\nкласс качества, филиал')
    d.task('t2', M, 2, '1.1.2. Скачать отчёты по портфелю и просрочке', 'Power BI')
    d.task('t3', M, 3, '1.1.3. Рассчитать показатели: портфель, NPL, доля NPL, PAR, резервы, покрытие',
           'Excel / Python')
    d.task('t4', M, 4, '1.1.4. Сверить портфель и резервы с балансом (остатки по балансовым счетам)',
           'DWH · Excel', note='Портфель отчёта = сальдо\nссудных счетов; резерв\n= сальдо счетов резерва')
    d.gate('g1', M, 5, 'Есть расхождения?')
    d.task('t5', M, 6, '1.1.5. Определить причину и ответственного, внести в реестр ошибок', 'Excel · реестр ошибок',
           dy=18)
    d.task('t6', M, 7, '1.1.6. Сообщить ответственному: звонок / e-mail', 'Outlook · телефон', dy=18)
    d.task('t7', R, 7, '1.1.7. Исправить данные (резерв, классификация, ввод) в АБС Б2', 'АБС Б2')
    d.task('t8', M, 8, '1.1.8. Сформировать ежедневный отчёт, отметить незакрытые расхождения', 'Excel',
           dy=-12)
    d.task('t9', H, 9, '1.1.9. Проверить отчёт')
    d.gate('g2', H, 10, 'Есть замечания?')
    d.task('t10', D, 11, '1.1.10. Получить ежедневный отчёт по портфелю', 'Outlook')
    d.event('e', D, 12, 'end', 'Отчёт направлен')
    d.flow('s', 't1'); d.flow('t1', 't2'); d.flow('t2', 't3'); d.flow('t3', 't4'); d.flow('t4', 'g1')
    d.flow('g1', 't5', 'Да', route='vh', exit='b')
    d.flow('g1', 't8', 'Нет')
    d.flow('t5', 't6')
    d.flow('t6', 't7', route='auto')
    d.flow('t7', 't4', 'Исправлено: повторная сверка', route='hv', exit='l', enter='b')
    d.flow('t6', 't8', route='hv', exit='r', enter='b')
    d.flow('t8', 't9', exit='r')
    d.flow('t9', 'g2')
    d.flow('g2', 't3', 'Да', route='under', ry=d.lane_y[H] + 37)
    d.flow('g2', 't10', 'Нет')
    d.flow('t10', 'e')
    d.data('do', D, 8, 'Ежедневный отчёт по портфелю.xlsx', dx=-6)
    d.data('dr', R, 5, 'Реестр ошибок данных → 2. Мониторинг', dx=-4, dy=12)
    d.flow('t8', 'do', assoc=True, exit='t', enter='b')
    d.flow('t5', 'dr', assoc=True, exit='b', enter='t')
    return d


# ======================================================================= 1.2
def p_monthly():
    d = Diagram('1.2 Ежемесячная отчётность',
                passport('1.2', 'Ежемесячная отчётность: портфель на конец месяца, АКР, презентация для стейкхолдеров'),
                [R_HEAD, R_TOIROV, R_MUKH, R_RESP, R_DIR],
                terms('DWH', 'Power BI', 'АБС Б2', 'АКР', 'NPL', 'Резерв'),
                UNIT, ['Директор департамента /\nстейкхолдеры', ('Начальник управления\n(Обидов Б.)', 74),
                       'Специалисты управления', 'Ответственные подразделения'], ncols=13)
    D, H, S, R = 0, 1, 2, 3
    d.event('s', H, 0, 'timer_start', '1-й рабочий день месяца (закрытие месяца)')
    d.gate('p1', H, 1, '', kind='and')
    d.task('t1', H, 2, '1.2.1. Выгрузить данные на конец месяца: портфель, резервы, баланс',
           'DWH · SQL / Power BI / АБС Б2', dy=-10,
           note='Скрипты DWH, отчёты\nPower BI, выгрузки Б2')
    d.task('t2', S, 2, '1.2.2. Предоставить выверенные данные: выборка обеспечений (1.3), портфель на последний день (1.1)',
           'Excel', sub=True)
    d.gate('p2', H, 3, '', kind='and')
    d.task('t3', H, 4, '1.2.3. Сформировать портфель на конец месяца (продукты, валюты, филиалы, классы)',
           'Excel / Python', dy=-10)
    d.task('t4', H, 5, '1.2.4. Подготовить отчёт АКР', 'Excel', dy=-10)
    d.task('t5', H, 6, '1.2.5. Сверить с балансом и с прошлым месяцем: динамика, аномалии', 'DWH · Excel',
           dy=-10)
    d.gate('g1', H, 7, 'Есть расхождения?', dy=-10)
    d.task('t6', H, 7, '1.2.6. Запросить исправление или пояснение', 'Outlook', dy=17)
    d.task('t7', R, 7, '1.2.7. Исправить данные / дать пояснение', 'АБС Б2')
    d.task('t8', H, 8, '1.2.8. Подготовить презентацию о текущем состоянии кредитного портфеля',
           'PowerPoint', dy=-10)
    d.task('t9', D, 9, '1.2.9. Рассмотреть отчёт и презентацию')
    d.gate('g2', D, 10, 'Есть замечания?')
    d.task('t10', H, 11, '1.2.10. Представить стейкхолдерам, разослать материалы', 'Outlook · PowerPoint',
           dy=-10)
    d.event('e', H, 12, 'end', 'Ежемесячная отчётность представлена', dy=-10)
    d.flow('s', 'p1'); d.flow('p1', 't1', route='vh', exit='t')
    d.flow('p1', 't2', route='vh', exit='b')
    d.flow('t1', 'p2', route='hv', enter='t'); d.flow('t2', 'p2', route='hv', enter='b')
    d.flow('p2', 't3', route='vh', exit='t'); d.flow('t3', 't4'); d.flow('t4', 't5'); d.flow('t5', 'g1')
    d.flow('g1', 't6', 'Да'); d.flow('t6', 't7')
    d.flow('t7', 't5', 'Исправлено', route='hv', exit='l', enter='b')
    d.flow('g1', 't8', 'Нет'); d.flow('t8', 't9', route='vh', exit='t', enter='l')
    d.flow('t9', 'g2')
    d.flow('g2', 't8', 'Да', route='vh', exit='b', enter='r')
    d.flow('g2', 't10', 'Нет', exit='r')
    d.flow('t10', 'd1', assoc=True, exit='t', enter='b')
    d.flow('t10', 'e')
    d.data('d1', D, 11, 'Портфель на конец месяца, АКР, презентация', dx=-4)
    return d


# ======================================================================= 1.3
def p_collateral():
    d = Diagram('1.3 Выборка обеспечений',
                passport('1.3', 'Подготовка ежемесячного отчёта «Выборка обеспечений на начало месяца»'),
                [R_TOIROV, R_RESP, R_HEAD],
                terms('АБС Б2', 'DWH', 'Power BI', 'Сальдо 945%%', 'Реестр ошибок'),
                UNIT, [('Главный специалист\n(Тоиров Ж.)', 100), 'Ответственные подразделения',
                       'Начальник управления'], ncols=14)
    T, R, H = 0, 1, 2
    d.event('s', T, 0, 'timer_start', '1-й рабочий день месяца, начало дня')
    d.task('t1', T, 1, '1.3.1. Выгрузить активные сделки обеспечения', 'АБС Б2', dy=-12,
           note='Сделки → Кредиты+ →\nОбеспечения кредитов;\nF7 «Активные сделки»;\nCtrl+F9 «общие столбцы\nдля учёта обеспечений»')
    d.task('t2', T, 2, '1.3.2. Экспортировать итоги в Excel «Активные обеспечения в Б2 на 01.ММ.ГГГГ»',
           'АБС Б2 → Excel', dy=-12)
    d.task('t3', T, 3, '1.3.3. Присвоить группы видов обеспечения по справочнику', 'Excel', dy=-12,
           note='«Вид залога» =\n«Краткое наименование»\n(лист «Виды обеспечений\nв Б2 Группа»)')
    d.task('t4', T, 4, '1.3.4. Выгрузить сальдо счетов 945%% на последний рабочий день месяца',
           'DWH · SQL-скрипт', dy=-12)
    d.task('t5', T, 5, '1.3.5. Скачать отчёт «ОБЕСПЕЧЕНИЕ-ОБЩИЕ ДАННЫЕ» на ту же дату', 'Power BI', dy=-12,
           note='Папка\n«Управление рисками»')
    d.task('t6', T, 6, '1.3.6. Подтянуть «Сальдо 945» и «Учтено Общие данные» по счёту учёта',
           'Excel (ВПР)', dy=-12)
    d.task('t7', T, 7, '1.3.7. Сальдо > 0 и Учтено > 0: сумма обеспечения = «Учтено»', 'Excel', dy=-12)
    d.gate('g1', T, 8, 'Сальдо > 0, а «Учтено» = #Н/Д?', dy=-12)
    d.task('t8', T, 8, '1.3.8. Проверить сделку по коду: «Учтено» > 0 и дата «Учёт залогов» ≤ конца месяца',
           'АБС Б2', dy=22)
    d.gate('g2', T, 9, 'Оба условия выполнены?', dy=22)
    d.task('t9', T, 10, '1.3.9. Сумма обеспечения = сальдо 945', 'Excel', dy=4)
    d.task('t10', T, 10, '1.3.10. Сумма = 0; внести расхождение в реестр ошибок', 'Excel · реестр ошибок',
           dy=30)
    d.task('t11', R, 10, '1.3.11. Исправить данные обеспечения в АБС Б2', 'АБС Б2',
           )
    d.gate('m1', T, 11, '', dy=-12)
    d.task('t12', T, 12, '1.3.12. Пустые ячейки = 0, снять формулы, сохранить файл', 'Excel', dy=-12)
    d.task('t13', H, 12, '1.3.13. Использовать выборку в ежемесячной отчётности (1.2)', sub=True)
    d.event('e', H, 13, 'end', 'Выборка обеспечений готова')
    for a, b in [('s', 't1'), ('t1', 't2'), ('t2', 't3'), ('t3', 't4'), ('t4', 't5'), ('t5', 't6'),
                 ('t6', 't7'), ('t7', 'g1'), ('m1', 't12'), ('t13', 'e')]:
        d.flow(a, b)
    d.flow('g1', 't8', 'Да')
    d.flow('g1', 'm1', 'Нет')
    d.flow('t8', 'g2')
    d.flow('g2', 't9', 'Да', exit='r')
    d.flow('g2', 't10', 'Нет', route='vh', exit='b')
    d.flow('t9', 'm1', route='hv', enter='b')
    d.flow('t10', 't11', msg=True)
    d.flow('t10', 'm1', route='hv', exit='r', enter='b')
    d.flow('t12', 't13', route='auto', exit='b', enter='t')
    d.data('d1', T, 13, 'Выборка обеспечений на 01.ММ.ГГГГ.xlsx', dy=-12, dx=-8)
    d.flow('t12', 'd1', assoc=True, exit='r', enter='l')
    return d


# ======================================================================= 2
def p_monitoring():
    d = Diagram('2. Мониторинг и декадная рассылка',
                passport('2', 'Мониторинг данных, используемых в отчётах управления, и декадная рассылка'),
                [('Специалисты управления', 'Тоиров Ж. (обеспечение), Мухаммадиев А. (портфель, резервы), Абдураимов У. (автоматические проверки)'),
                 R_HEAD, R_RESP, R_DIR],
                terms('Реестр ошибок', 'Декада', 'АБС Б2', 'DWH', 'Резерв'),
                UNIT, ['Директор департамента', ('Специалисты управления', 62), 'Начальник управления',
                       ('Ответственные подразделения', 50)], ncols=12)
    D, S, H, R = 0, 1, 2, 3
    # (A) the everyday loop
    d.event('s1', S, 0, 'start', 'Выявлено расхождение в ходе работы (1.1, 1.3, автопроверки)', dy=-14)
    d.task('a1', S, 1, '2.1. Внести в реестр ошибок: что, где, сумма, ответственный, дата', 'Excel · реестр',
           dy=-14)
    d.task('a2', S, 2, '2.2. Оперативно уведомить ответственного: звонок / e-mail', 'Outlook · телефон',
           dy=-14)
    d.task('a3', R, 2, '2.3. Исправить данные в АБС Б2', 'АБС Б2')
    d.task('a4', S, 3, '2.4. Проверить исправление, закрыть запись в реестре', 'DWH · Excel', dy=-14)
    d.event('e1', S, 4, 'end', 'Ошибка закрыта', dy=-14)
    # (B) every ten days
    d.event('s2', S, 5, 'timer_start', 'Каждые 10 дней (1, 11, 21 числа) [уточнить]', dy=14)
    d.task('b1', S, 6, '2.5. Собрать новые и незакрытые ошибки за декаду по подразделениям',
           'Excel / Python', dy=14)
    d.task('b2', S, 7, '2.6. Подготовить сводное письмо: перечень, суммы, сроки исправления', 'Outlook', dy=14)
    d.task('b3', H, 7, '2.7. Проверить и согласовать письмо')
    d.task('b4', H, 8, '2.8. Разослать руководителям подразделений, копия – директору', 'Outlook')
    d.task('b5', R, 8, '2.9. Исправить в установленный срок', 'АБС Б2', dy=4)
    d.gate('g1', S, 9, 'Исправлено к следующей декаде?', dy=14)
    d.task('b6', H, 10, '2.10. Эскалация директору департамента')
    d.task('b7', D, 10, '2.11. Принять управленческие меры')
    d.event('e2', S, 11, 'end', 'Декада закрыта', dy=14)
    for a, b in [('s1', 'a1'), ('a1', 'a2'), ('a4', 'e1'), ('s2', 'b1'), ('b1', 'b2'), ('b3', 'b4')]:
        d.flow(a, b)
    d.flow('a2', 'a3', msg=True)
    d.flow('a3', 'a4', route='hv', exit='r', enter='b')
    d.flow('b2', 'b3', route='auto')
    d.flow('b4', 'b5', msg=True)
    d.flow('b5', 'g1', route='hv', exit='r', enter='b')
    d.flow('g1', 'e2', 'Да', exit='r')
    d.flow('g1', 'b6', 'Нет', route='vh', exit='b', enter='l')
    d.flow('b6', 'b7')
    d.flow('b7', 'e2', route='hv', exit='r', enter='t')
    d.data('dr', H, 1, 'Реестр ошибок данных (общий файл)', dx=0)
    d.flow('a1', 'dr', assoc=True, exit='b', enter='t')
    return d


# ======================================================================= 3
def p_request():
    d = Diagram('3. Отчёты по запросу',
                passport('3', 'Подготовка отчётов и данных по запросу (срочные и разовые запросы)'),
                [R_CUST, R_HEAD, ('Исполнитель', 'специалист управления, назначенный начальником (по компетенции, ответственности и загрузке)'),
                 R_AUTO],
                terms('Реестр запросов', 'DWH', 'Power BI', 'АБС Б2', 'SQL/Python'),
                UNIT, ['Заказчик', ('Начальник управления\n(Обидов Б.)', 58),
                       ('Исполнитель\n(специалист управления)', 50), 'Специалист по автоматизации'], ncols=13)
    Z, H, E, A = 0, 1, 2, 3
    d.event('s', Z, 0, 'msg_start', 'Поступил запрос (e-mail, СЭД, устно)')
    d.task('t1', H, 0, '3.1. Принять запрос, внести в реестр запросов', 'Excel · реестр')
    d.gate('g1', H, 1, 'Требования ясны?', lpos='bottom')
    d.task('t2', Z, 1, '3.2. Уточнить: цель, показатели, дата, разрезы, срок', 'Outlook · встреча')
    d.task('t3', H, 2, '3.3. Определить исполнителя: компетенция, ответственность, загрузка', dy=-6)
    d.gate('g2', H, 3, 'Нужна командная работа?', dy=-6)
    d.task('t4', H, 3, '3.4. Распределить части между специалистами, назначить сводящего', dy=17)
    d.gate('m1', E, 4, '')
    d.task('t5', E, 5, '3.5. Получить данные', 'DWH · SQL / Power BI / АБС Б2')
    d.task('t6', E, 6, '3.6. Подготовить отчёт / выгрузку', 'Excel / Python')
    d.task('t7', E, 7, '3.7. Самопроверка: сверка с балансом и другими источниками', 'DWH · Excel')
    d.task('t8', H, 8, '3.8. Проверить результат', dy=-6)
    d.gate('g3', H, 9, 'Есть замечания?', dy=-6)
    d.task('t9', H, 10, '3.9. Направить заказчику, закрыть запрос в реестре', 'Outlook', dy=-6)
    d.event('ez', Z, 10, 'msg_end', 'Заказчик получил ответ')
    d.gate('g4', H, 11, 'Запрос повторяющийся?', dy=-6)
    d.task('t10', A, 11, '3.10. Включить в план автоматизации (процесс 4)', sub=True)
    d.event('e', H, 12, 'end', 'Запрос закрыт', dy=-6)
    d.flow('s', 't1', msg=True)
    d.flow('t1', 'g1')
    d.flow('g1', 't2', 'Нет', route='vh', exit='t', enter='b')
    d.flow('t2', 't3', route='hv', exit='r', enter='t')
    d.flow('g1', 't3', 'Да', route='vh', exit='r')
    d.flow('t3', 'g2')
    d.flow('g2', 't4', 'Да')
    d.flow('g2', 'm1', 'Нет', route='hv', exit='r', enter='t')
    d.flow('t4', 'm1', route='hv', exit='r', enter='t')
    d.flow('m1', 't5'); d.flow('t5', 't6'); d.flow('t6', 't7')
    d.flow('t7', 't8', route='hv', exit='r', enter='b')
    d.flow('t8', 'g3')
    d.flow('g3', 't6', 'Да', route='over', exit='b', enter='t', ry=d.nodes['t6']['cy'] - TH / 2 - 5)
    d.flow('g3', 't9', 'Нет')
    d.flow('t9', 'ez', msg=True)
    d.flow('t9', 'g4')
    d.flow('g4', 't10', 'Да')
    d.flow('g4', 'e', 'Нет')
    d.data('dq', H, 0, 'Реестр запросов', dx=22, dy=17)
    d.flow('t1', 'dq', assoc=True, exit='b', enter='l')
    return d


# ======================================================================= 4
def p_auto():
    d = Diagram('4. Автоматизация',
                passport('4', 'Автоматизация регулярных отчётов и проверок данных'),
                [R_AUTO, ('Владелец задачи', 'специалист, который сейчас делает задачу вручную'), R_HEAD, R_IT],
                terms('SQL/Python', 'DWH', 'Power BI', 'Реестр запросов'),
                UNIT, ['Начальник управления', ('Специалист по автоматизации\n(Абдураимов У.)', 60),
                       'Владелец задачи', 'ИТ / администраторы DWH'], ncols=13)
    H, A, O, I = 0, 1, 2, 3
    d.event('s', A, 0, 'start', 'Повторяющаяся задача (из 3.10) или поручение начальника', dy=-10)
    d.task('t1', H, 1, '4.1. Утвердить задачу и приоритет')
    d.task('t2', O, 1, '4.2. Описать текущий ручной порядок: источники, шаги, формат, срок')
    d.task('t3', A, 2, '4.3. Проанализировать: источники, логика расчёта, формат результата',
           'DWH · Power BI · АБС Б2', dy=-10)
    d.gate('g1', A, 3, 'Нужен доступ к данным?', dy=-10)
    d.task('t4', I, 3, '4.4. Предоставить доступ к таблицам DWH / отчётам', 'DWH')
    d.task('t5', A, 4, '4.5. Разработать решение: SQL-скрипт, Python, шаблон Excel', 'SQL · Python · Excel',
           dy=-10)
    d.task('t6', A, 5, '4.6. Тест: параллельный расчёт с ручным вариантом за несколько дат', 'Excel',
           dy=-10)
    d.gate('g2', A, 6, 'Результаты совпадают?', dy=-10, lpos='bottom')
    d.task('t7', O, 7, '4.7. Приёмка решения владельцем задачи')
    d.task('t8', A, 8, '4.8. Внедрить: запуск по расписанию / кнопкой, инструкция', 'Python · планировщик',
           dy=-10)
    d.task('t9', A, 9, '4.9. Документировать: скрипт, логика, источники, контакты', 'Репозиторий · Word',
           dy=-10)
    d.task('t10', O, 10, '4.10. Обучиться и использовать решение')
    d.task('t11', H, 11, '4.11. Учесть сэкономленное время, перераспределить загрузку')
    d.event('e', A, 12, 'end', 'Задача автоматизирована', dy=-10)
    d.flow('s', 't1', route='vh', exit='t', enter='l')
    d.flow('t1', 't2')
    d.flow('t2', 't3', route='hv', exit='r', enter='b')
    d.flow('t3', 'g1')
    d.flow('g1', 't4', 'Да', route='vh', exit='b', enter='t')
    d.flow('t4', 't5', route='hv', exit='r', enter='b')
    d.flow('g1', 't5', 'Нет')
    d.flow('t5', 't6'); d.flow('t6', 'g2')
    d.flow('g2', 't5', 'Нет', route='over', ry=d.lane_y[A] + 6)
    d.flow('g2', 't7', 'Да', exit='r')
    d.flow('t7', 't8', route='hv', exit='r', enter='b')
    d.flow('t8', 't9')
    d.flow('t9', 't10', route='vh', exit='b', enter='l')
    d.flow('t9', 't11', route='vh', exit='t', enter='l')
    d.flow('t10', 'e', route='hv', exit='r', enter='b')
    d.flow('t11', 'e', route='hv', exit='r', enter='t')
    d.data('dl', A, 10, 'Скрипт + инструкция в общей папке / репозитории', dy=-10, dx=-4)
    d.flow('t9', 'dl', assoc=True, exit='r', enter='l')
    return d


# ======================================================================= map
def top_level():
    W, H = 420, 297
    S = []
    S.append(text(10, 8, W - 20, 10, f'{UNIT}: верхний уровень бизнес-процессов (As Is)', size=13, bold=True,
                  halign='left'))
    S.append(text(10, 17, W - 20, 6, f'{DEPT} · статус: в разработке с {DATE} г. · разработчик: {DEV}',
                  size=7, halign='left', color=C['muted']))

    def cyl(x, y, w, h, t):
        e = 3
        import math
        bot = [(w / 2 + w / 2 * math.cos(a / 20 * math.pi), h - e + e * math.sin(a / 20 * math.pi))
               for a in range(0, 21)]
        geo = [('poly', [(0, e)] + bot[::-1] + [(w, e)], True), ('ell', w / 2, e, w / 2, e)]
        return Shape(x, y, w, h, geo, fill=C['store'], stroke=C['ink'], sw=0.35, runs=t, size=7.5,
                     bold=True, textbox=(0, 2 * e, w, h - 3 * e))

    def proc(x, y, w, h, no, name, who):
        runs = [(no + '  ', True, False, C['ink']), (name + '\n', True, False, C['ink']),
                (who, False, True, C['muted'])]
        geo = [rect_geom(w, h),
               ('poly', [(w / 2 - 2, h - 4.5), (w / 2 + 2, h - 4.5), (w / 2 + 2, h - 0.5), (w / 2 - 2, h - 0.5)], True),
               ('poly', [(w / 2 - 1.3, h - 2.5), (w / 2 + 1.3, h - 2.5)], False),
               ('poly', [(w / 2, h - 3.8), (w / 2, h - 1.2)], False)]
        return Shape(x, y, w, h, geo, fill='#FFFFFF', stroke=C['ink'], sw=0.4, rounding=2.2, runs=runs,
                     size=7.2, textbox=(0, 0, w, h - 4))

    def group(x, y, w, h, title):
        return Shape(x, y, w, h, [rect_geom(w, h)], fill=C['group'], stroke='#7A8AA0', sw=0.35, dash=2,
                     rounding=3, runs=title, size=8.5, bold=True, halign='left', valign='top', margin=6)

    # sources
    S.append(text(12, 30, 60, 6, 'ИСТОЧНИКИ ДАННЫХ', size=7.5, bold=True, color=C['muted'], halign='left'))
    srcs = [('АБС Б2 (B2NG)', 'первоисточник: сделки, обеспечение, ручные проверки'),
            ('DWH', 'SQL-скрипты: портфель, сальдо, баланс, резервы'),
            ('Power BI', 'bi.kapitalbank.uz: готовые отчёты для скачивания')]
    for k, (a, b) in enumerate(srcs):
        y = 40 + k * 46
        S.append(cyl(14, y, 52, 30, a))
        S.append(text(12, y + 30.5, 56, 8, b, size=6, color=C['muted']))
    # groups
    gx, gw = 90, 230
    S.append(group(gx, 30, gw, 98, '1. Подготовка регулярных отчётов'))
    S.append(proc(gx + 6, 42, 70, 30, '1.1', 'Ежедневный отчёт по кредитному портфелю (NPL, PAR, резервы)',
                  'Мухаммадиев А. · ежедневно'))
    S.append(proc(gx + 80, 42, 70, 30, '1.2', 'Ежемесячная отчётность: портфель на конец месяца, АКР, презентация',
                  'Обидов Б. · ежемесячно'))
    S.append(proc(gx + 154, 42, 70, 30, '1.3', 'Выборка обеспечений на начало месяца',
                  'Тоиров Ж. · ежемесячно'))
    S.append(Shape(gx + 6, 82, 218, 40, [rect_geom(218, 40)], fill='#FFFFFF', stroke='#9AA5B4', sw=0.25,
                   rounding=2, halign='left', valign='middle', margin=6, size=9, runs=[
                       ('Периодичность отчётов управления\n', True, False, C['ink']),
                       ('• ежедневно – 1.1 портфель и NPL\n', False, False, C['ink']),
                       ('• каждую декаду (10 дней) – сводное письмо об ошибках данных (процесс 2)\n', False, False, C['ink']),
                       ('• ежемесячно – 1.2 портфель на конец месяца, АКР, презентация; 1.3 выборка обеспечений\n', False, False, C['ink']),
                       ('• ежеквартально / ежегодно – по схеме 1.2 [уточнить перечень отчётов]', False, False, C['ink'])]))
    S.append(group(gx, 136, gw, 46, '2. Мониторинг данных'))
    S.append(proc(gx + 6, 147, 218, 30, '2', 'Мониторинг данных в отчётах управления и декадная рассылка об ошибках',
                  'все специалисты · постоянно + каждые 10 дней'))
    S.append(group(gx, 190, gw, 46, '3. Отчёты по запросу'))
    S.append(proc(gx + 6, 201, 218, 30, '3', 'Срочные и разовые отчёты по запросу директора и других подразделений',
                  'Обидов Б. распределяет → исполнитель или команда'))
    S.append(group(gx, 244, gw, 46, '4. Поддерживающий процесс'))
    S.append(proc(gx + 6, 255, 218, 30, '4', 'Автоматизация регулярных отчётов и проверок (Python, SQL, Excel)',
                  'Абдураимов У.'))
    # consumers
    S.append(text(342, 30, 70, 6, 'ПОЛУЧАТЕЛИ', size=7.5, bold=True, color=C['muted'], halign='left'))
    cons = [('Директор департамента', 40), ('Правление / стейкхолдеры', 86),
            ('Руководители подразделений и филиалов (исправляют ошибки)', 140),
            ('Заказчики запросов', 196)]
    for t, y in cons:
        S.append(Shape(342, y, 66, 26, [rect_geom(66, 26)], fill=C['proc'], stroke=C['ink'], sw=0.35,
                       rounding=2, runs=t, size=7.2, bold=True))
    # arrows
    for k in range(3):
        y = 55 + k * 46
        S.append(line([(66, y), (gx, y)]))
    S.append(line([(gx + gw, 57), (342, 53)]))
    S.append(line([(gx + gw, 70), (342, 99)]))
    S.append(line([(gx + gw, 162), (342, 153)]))
    S.append(line([(gx + gw, 216), (342, 209)]))
    S.append(line([(gx + gw + 4, 270), (gx + gw + 4, 128)], dash=2))
    S.append(text(gx + gw + 5, 230, 18, 14, 'ускоряет\nпроцессы 1–3', size=5.8, italic=True,
                  color=C['muted'], halign='left'))
    return ('Верхний уровень', W, H, S)


def main():
    os.makedirs(OUT, exist_ok=True)
    diagrams = [p_daily(), p_monthly(), p_collateral(), p_monitoring(), p_request(), p_auto()]
    pages = [top_level()] + [(d.tab, d.W, d.H, d.render()) for d in diagrams]
    vsdx = os.path.join(OUT, 'BPMN_Upravlenie_otchetnosti.vsdx')
    write_vsdx(vsdx, pages, title=UNIT, author='Абдураимов У.')
    # preview: one HTML, one page per diagram, every page scaled onto A3 landscape
    html = ['<!doctype html><meta charset="utf-8"><style>@page{size:420mm 297mm;margin:0}'
            'body{margin:0}.pg{width:420mm;height:297mm;display:flex;align-items:center;'
            'justify-content:center;page-break-after:always;overflow:hidden}'
            '.pg svg{width:414mm;height:291mm}</style>']
    for name, W, H, S in pages:
        svg = svg_page(S, W, H).replace(f'width="{W}mm" height="{H}mm"', '', 1)
        html.append(f'<div class="pg">{svg}</div>')
    hp = os.path.join(OUT, 'preview.html')
    open(hp, 'w').write(''.join(html))
    for k, (name, W, H, S) in enumerate(pages):
        open(os.path.join(OUT, f'page{k}.svg'), 'w').write(svg_page(S, W, H))
    if '--pdf' in sys.argv:
        chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        subprocess.run([chrome, '--headless', '--no-pdf-header-footer',
                        f'--print-to-pdf={os.path.join(OUT, "BPMN_Upravlenie_otchetnosti.pdf")}',
                        '--virtual-time-budget=4000', 'file://' + hp], check=True,
                       stderr=subprocess.DEVNULL)
    # step register
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    wb = Workbook()
    ws = wb.active
    ws.title = 'Реестр шагов'
    ws.append(['Процесс', '№', 'Шаг', 'Исполнитель (роль)', 'Система / инструмент', 'Комментарий',
               'Срок / периодичность [заполнить]'])
    for d in diagrams:
        for lab, lane, sysn, note in d.steps:
            no, _, name = lab.partition('. ')
            ws.append([d.tab, no, name, lane.replace('\n', ' '), sysn, note.replace('\n', ' '), ''])
    for c in ws[1]:
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor='1F3864')
    for col, w in zip('ABCDEFG', (30, 8, 60, 32, 28, 40, 24)):
        ws.column_dimensions[col].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical='top')
    ws.freeze_panes = 'A2'
    wb.save(os.path.join(OUT, 'BPMN_Reestr_shagov.xlsx'))
    print('ok:', vsdx, len(pages), 'pages')


if __name__ == '__main__':
    main()
