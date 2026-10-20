"""
All SQL of the client portfolio, and nothing else.

Five small queries instead of one big join. Each one returns rows that cannot repeat,
and Python (logic.py) puts them together. Why not one join: the client's current
account (20208) is linked in dealid_connection to EVERY deal it ever served, so a join
multiplied the rows (15 accounts became 210).

Parameters everywhere: :pdate (date) and :contragentid (number).
To run a query by hand in your SQL tool, replace :pdate / :contragentid with &pdate / &contragentid.
Amounts in the database are in tiyin, so everything is divided by 100.
"""
# ⚠️ Change this one line to wherever your get_oracle_connection() lives.
from main.oracle import get_oracle_connection


# Q0. Client name.
SQL_CLIENT = """
select c.name as contragent_name
from   schema_1.contragent_table c
where  c.id      = :contragentid
and    c.arcdate = :pdate
"""

# Q1. ACCOUNTS: every account of the client with a non-zero balance on the date.
#     Loans (asset accounts) come out NEGATIVE, deposits positive.
SQL_ACCOUNTS = """
select t.id                       as account_id,
       t.accountno,
       substr(t.accountno, 1, 5)  as bal_acc,         -- 12501, 20208 ...
       substr(t.accountno, 6, 3)  as currency_code,   -- 000 so'm, 840 USD ...
       t.toboid,
       t.summanoweq / 100         as saldo
from   schema_1.account_table_1 t
where  t.arcdate      = :pdate
and    t.contragentid = :contragentid
and    t.summanoweq  <> 0
order by t.accountno
"""

# Q2. DEALS: the client's deals alive in the portfolio on the date.
#     Starts from portfel, not from accounts, so a deal with a zero balance is not lost.
#     currency_rate.base is always 1, so given_amount_eq = givenamount * rate / 100.
SQL_DEALS = """
select p.dealid,
       p.facilitydealid                     as rnk_dealid,
       p.expectedclosedate                  as close_date,
       p.currencyid,
       p.givenamount / 100                  as given_amount,
       p.givenamount * nvl(r.rate, 1) / 100 as given_amount_eq
from   schema_2.portfel_table p
left join schema_2.currency_rate r
       on r.arcdate    = p.arcdate
      and r.currencyid = p.currencyid
where  p.arcdate      = :pdate
and    p.contragentid = :contragentid
order by p.dealid
"""

# Q3. LINKS: which account belongs to which LIVE deal.
#     Only deals from Q2, so links to old closed deals never come in.
SQL_LINKS = """
select distinct dl.accountid, dl.dealid
from   schema_2.dealid_connection dl
where  dl.daiusettingid <> 0
-- and dl.dealcloseid = 0          -- extra safety; switch on once you are sure 0 = open
and    dl.dealid in (select p.dealid
                     from   schema_2.portfel_table p
                     where  p.arcdate      = :pdate
                     and    p.contragentid = :contragentid)
"""

# Q4. TURNOVER: money in / out of the client's current and card accounts,
#     month by month, for the 6 full months before the month of :pdate.
#     Positions 10-17 of an account number = client code; if both sides have the same
#     code it is the client moving his own money (own transfer, loan issued to himself,
#     loan repayment), so it is left out.
SQL_TURNOVER = """
with my_acc as (
    select accountno
    from   schema_1.account_table_1
    where  arcdate      = :pdate
    and    contragentid = :contragentid
    and   (substr(accountno, 1, 3) = '202'                                  -- demand deposits
           or substr(accountno, 1, 5) in ('22618', '22619', '22620', '22621')) -- card accounts
)
select 'IN'                    as direction,
       trunc(d.arcdate, 'MM')  as month,
       sum(d.summaeq) / 100    as amount,
       count(*)                as docs
from   schema_1.account d
join   my_acc m on m.accountno = d.accountbno
where  d.arcdate >= add_months(trunc(:pdate, 'MM'), -6)
and    d.arcdate <  trunc(:pdate, 'MM')
and    substr(d.accountano, 10, 8) <> substr(d.accountbno, 10, 8)
group by trunc(d.arcdate, 'MM')
union all
select 'OUT',
       trunc(d.arcdate, 'MM'),
       sum(d.summaeq) / 100,
       count(*)
from   schema_1.account d
join   my_acc m on m.accountno = d.accountano
where  d.arcdate >= add_months(trunc(:pdate, 'MM'), -6)
and    d.arcdate <  trunc(:pdate, 'MM')
and    substr(d.accountano, 10, 8) <> substr(d.accountbno, 10, 8)
group by trunc(d.arcdate, 'MM')
"""


def fetch(cur, sql, params):
    """Run one query and return a list of dicts with lower-case keys."""
    cur.execute(sql, params)
    cols = [c[0].lower() for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def load_client(contragentid, pdate):
    """Everything the portfolio page needs, straight from Oracle, no calculations."""
    params = {"pdate": pdate, "contragentid": contragentid}
    with get_oracle_connection() as conn:
        cur = conn.cursor()
        client = fetch(cur, SQL_CLIENT, params)
        return {
            "name": client[0]["contragent_name"] if client else None,
            "accounts": fetch(cur, SQL_ACCOUNTS, params),
            "deals": fetch(cur, SQL_DEALS, params),
            "links": fetch(cur, SQL_LINKS, params),
            "turnover": fetch(cur, SQL_TURNOVER, params),
        }
