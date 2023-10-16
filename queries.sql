--задание 1
SELECT c.login, count(o.id)
FROM "Couriers" AS c
         INNER JOIN "Orders" o ON "o"."courierId" = "c"."id"
WHERE "o"."inDelivery"
GROUP BY "c"."login";

--задание 2
SELECT track,
       CASE
           WHEN finished THEN 2
           WHEN cancelled THEN -1
           WHEN "inDelivery" THEN 1
           ELSE 0 END AS status
FROM "Orders";