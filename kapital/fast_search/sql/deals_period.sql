-- Сделки за период
-- Сделки, открытые между двумя датами. Пример с обработкой в process.py (тийины → сумы).
select d.id            as "ID сделки",
       d.siteid        as "МФО",
       d.contragentid  as "ID контрагента",
       d.amounteq      as "Сумма",
       d.opendate      as "Дата открытия"
from   schema2.deal d
where  d.opendate between :startdate and :enddate
  and  (:siteid is null or d.siteid = :siteid)
