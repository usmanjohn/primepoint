-- Сделки клиента
-- Все сделки контрагента на дату архива. МФО можно оставить пустым — тогда по всем филиалам.
select d.id            as "ID сделки",
       d.siteid        as "МФО",
       d.dealtypeid    as "Тип",
       d.currencyid    as "Валюта",
       d.amounteq / 100 as "Сумма, сум",
       d.closedate     as "Дата закрытия"
from   schema2.deal d
where  d.contragentid = :contragentid
  and  trunc(d.arcdate) = :arcdate
  and  (:siteid is null or d.siteid = :siteid)
order by d.id
