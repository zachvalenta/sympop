# ⛩️

## 参考

🗄️ `#modeling.md` Codd
🔍 https://dba.stackexchange.com
📚
* Beaulieu learning sql
* Conery curious moon https://www.sqlnoir.com/
* Evans star https://sql-playground.wizardzines.com/
* Faroult art of sql
* Molinaro sql cookbook

## 进步


Malloy https://news.ycombinator.com/item?id=45094256 https://github.com/malloydata/malloy
semantic layer = DDD https://news.ycombinator.com/item?id=44953575

https://www.sqlnoir.com/blog/games-to-learn-sql
moving average https://www.jasonthorsness.com/25
INTERVIEWING
* https://sql.programmable.net/dashboard
* https://github.com/alexeygrigorev/data-science-interviews/blob/master/technical.md
* https://leetcode.com/problemset/database/
* https://www.hackerrank.com/domains/sql
* https://www.youtube.com/channel/UCW8Ews7tdKKkBT6GdtQaXvQ/videos

ZA
* https://roadmap.sh/sql
* https://gvwilson.github.io/sql-tutorial/
* Bealieau: port notes to digital copy, domains
* testing SQL https://news.ycombinator.com/item?id=34602318

* _25_: Capp schema
* _23_: port Beaulieu to paper copy, rf, read rest of Beaulieu
* _21_: semantics (migrations, tables), `query-sandbox`
* _20_: start `sjk`, Flask-SQLAlchemy (pagination, 1-m w/ backrefs, Marshmallow for nested serializers)
* _19_: 📙 Beaulieu chapters 1-5 and 10; Flask-SQLAlchemy (FK, through table, raw SQL) SQLite (FK support) SQLAlchemy (core, parameterized queries)
* _18_: Flyway for Dark Canary, modeling course
* _17_: subqueries for Case

# 🚜 DML

CLAUSES
* _clause_: part of select statement 📙 Beaulieu [47]
* _select_: what attr to incl in result set 📙 Beaulieu [49]
* _from_: what tables and how they're linked 📙 Beaulieu [53]
* _where_: filter 📙 Beaulieu [58]

RELATIONAL OPERATIONS 📙 Takahashi [43] 🗄 `language.md` semantics `math.md` set theory > operations
* _projection_: filter on attr i.e. `SELECT` https://stackoverflow.com/a/1031101 📙 Takahashi [43] Beaulieu [44-5]
* _selection_: filter on value i.e. `WHERE` 📙 Beaulieu [52-54]
* _division_: extract records that exist in both numerator/denomenator table but only the columns that exist only in numerator 📙 Takahashi [45]
* + join

CRUD
```sql
-- 1 attr, 1 val
INSERT INTO danzi(customer) VALUES ('alice');
-- 1 attr, n val
INSERT INTO danzi(customer) VALUES ('alice'), ('bob');
-- n attr, 1 val
INSERT INTO danzi(customer, price) VALUES ('alice', 15)
-- n attr, n val
INSERT INTO danzi(customer, price) VALUES ('alice', 15), ('bob', 10);

UPDATE <tab> SET <col>=0 WHERE id=3;
DELETE FROM <tab> WHERE id=3;  -- https://notso.boringsql.com/posts/deletes-are-difficult/

-- update based on value in another row https://amjith.com/blog/2023/sqlite_row_copy/
UPDATE users SET token = (SELECT token FROM users u WHERE u.id = 1) WHERE id = 2;
```

## distinct

🗄️ `math.md` set theory / combos

* _ALL_: default (which is why you never see it) 📙 Beaulieu [52]
* _DISTINCT_: dedupe
* operates on records, not columns https://discuss.codecademy.com/t/can-we-apply-distinct-to-a-select-query-with-multiple-columns/349723
* slow for large result set bc have to sort 📙 Beaulieu [52]
* SQLite lacks `distinct on` syntax so `group by`
```sql
--- all records in RS bc each is a distinct combination btw id/product (id=1/product=widget != id=2/product=widget)
select distinct id, product from orders
+----+----------+-----------+--------+
| id | customer | product   | amount |
+----+----------+-----------+--------+
| 1  | alice    | widget    | 100    |
| 2  | bob      | widget    | 200    |
| 3  | alice    | widget    | 100    |
| 4  | bob      | widget    | 200    |
| 5  | alice    | gadget    | 150    |
| 6  | carl     | gadget    | 175    |
| 7  | carl     | widget    | 225    |
| 8  | alice    | doohickey | 125    |
| 9  | bob      | doohickey | 225    |
| 10 | carl     | doohickey | 175    |
+----+----------+-----------+--------+

select * from orders group by customer, product
+----+----------+-----------+--------+
| id | customer | product   | amount |
+----+----------+-----------+--------+
| 8  | alice    | doohickey | 125    |
| 5  | alice    | gadget    | 150    |
| 1  | alice    | widget    | 100    |
| 9  | bob      | doohickey | 225    |
| 2  | bob      | widget    | 200    |
| 10 | carl     | doohickey | 175    |
| 6  | carl     | gadget    | 175    |
| 7  | carl     | widget    | 225    |
+----+----------+-----------+--------+
```

---

DISTINCT
```sql
-- relationship to group by https://stackoverflow.com/a/54430/6813490 📙 Molinaro

select distinct house_id, addr from house
+----------+-----------------+
| house_id | addr            |
+----------+-----------------+
| 1        | 5 rose street   |
| 2        | 12 main street  |
| 3        | 5 rose street   |
| 4        | 3 nice street   |
+----------+-----------------+

select house_id, addr from house group by addr
+----------+-----------------+
| house_id | addr            |
+----------+-----------------+
| 2        | 12 main street  |
| 3        | 5 rose street   |
| 4        | 3 nice street   |
+----------+-----------------+

SELECT saleprice, saledate
FROM   sales
GROUP  BY saleprice, saledate
HAVING count(*) = 1 

SELECT MIN(id) FROM sales
GROUP BY saleprice, saledate
HAVING COUNT(id) = 1
```

## execution order

* before execution, dbms checks query 1) perms 2) syntax 📙 Beaulieu [41]
* only `select` is mandatory https://hakibenita.com/sql-for-data-analysis#basics
* types of execution order: syntactical/logical (e.g. no `where` after `having`) and actual (e.g. `limit` query engine will limit first) 📙 Bradshaw 166
* syntactical/logical order 📙 Evans 5, 14 https://jvns.ca/blog/2019/10/03/sql-queries-don-t-start-with-select/
* order of tables in join don't matter 📙 Beaulieu [95]
```text
├── from
├── predicates
│   └── where
│   └── group by
│   └── having
├── select
│   └── window functions 📙 Evans [14]
│   └── order by 📙 Evans [13]
│   └── limit
```

## functions

💡 better to have this in application code https://www.youtube.com/watch?v=atwwf0qWpYg [20:30]

* _function_: built-in function provided by dbms
* has return value https://stackoverflow.com/a/771959
* e.g. SQLite `substr()`
* _procedure_: user-defined function
* no return value https://stackoverflow.com/a/771959
* aka stored procedure
* impl via procedural language availble in dbms
* too many and you've got business logic split btw application and db https://news.ycombinator.com/item?id=24845300
* _trigger_: hook e.g. on record update write previous state to archive/audit table https://www.youtube.com/watch?v=LFIAqFt9z2s https://til.simonwillison.net/sqlite/sqlite-triggers
* alternative to audit table is abadoning update-in-place entirely https://www.hytradboi.com/2022/baking-in-time-at-the-bottom-of-the-database
* avoid data updates by tracking things from which current info can be derived i.e. DOB instead of age
```sql
--  https://github.com/jOOQ/sakila/blob/main/sqlite-sakila-db/sqlite-sakila-schema.sql
CREATE TRIGGER actor_trigger AFTER INSERT ON actor
 BEGIN
  UPDATE actor SET last_update = DATETIME('NOW') WHERE rowid = new.rowid;
 END
;
```
* _aggregate_: function that returns single val from result set https://www.postgresql.org/docs/12/tutorial-agg.html 🗄 scalar 📙 Beaulieu ch. 8
* operates on whole table or on group 📙 Beaulieu 8.149
* can't use in WHERE clause
* can't layer https://stackoverflow.com/a/2436957
* _count_: ignores null https://hakibenita.com/sql-dos-and-donts#be-careful-when-counting-nullable-columns
```sql
select
    count(distinct addr) as "listings",
    cast (avg(price) as integer) as "avg",
    max(price) as "high",
    min(price) as "low"
from house
```
* operates on grouped result vs. table result set
```sql
select track, count(*) from splits group by track;
```
* counting groups 📍 📙 Beaulieu [149]
```sql
# SPLITS W/ SHARES < 100%: 66
select count(*) over (), track, sum(share), count(*) from splits group by track having cast(sum(share)as int) < 100;
```

## predicates

📙 Beaulieu ch. 4

SEMANTICS
* _predicate_: filter https://www.postgresql.org/docs/13/functions-comparison.html https://use-the-index-luke.com/sql/explain-plan/oracle/filter-predicates
* _condition_: clause in predicate 📙 [67]
* group w/ parentheses 📙 Beaulieu [59]
* _where_: condition on individual records
* occurs before `group by` https://www.helenanderson.co.nz/sql-aggregate-functions/
* _having_: condition on group 📙 Beaulieu [149]
* occurs after `group by` https://stackoverflow.com/a/9253267
```sql
where num >= 5 -- comparison operator 📙 Beaulieu 4.63
where num is not null -- identity operator
where num between 3000 and 5000; -- range; is inclusive 📙 Beaulieu [75]
```

COMPOUND
```sql
select count(*) from products 
where discontinued = 'y' and web > 0.001 and (list_price = 0.001 or list_price = 0.0)
select -- easier just to do this way
  (select count(*) from products where discontinued = 'Y' and web > 0.001 and list_price <= 0.001) * 100.0 /
  (select count(*) from products) as 'web zombie'

-- NOT 💻️ https://github.com/zachvalenta/capp-pu-copeland https://github.com/zachvalenta/capp-datalab/blob/main/src/workflows/cleanup/scope.py
WITH brand_codes AS (
    SELECT brand, priceline, buyline
    FROM pdr
    WHERE brand = 'Copeland'
)
SELECT pv.* FROM pv, brand_codes bc
WHERE pv.description LIKE '%Copeland%'
AND NOT (
    pv.mfg LIKE '%' || bc.brand || '%'
    OR pv.priceline = bc.priceline
    OR pv.buyline = bc.buyline
)

-- CORRECT VERSION
select distinct rfq.`Unique Identifier`, pv.eid, rfq.`Manufacturer Part Number` AS 'RS mpn', pv.mpn as 'capp mpn', pv.cost, pv.list, pv.list_eff
from rfq join pv on rfq.`Manufacturer Part Number` = pv.mpn
and (pv.mfg like '%siemens%' or pv.mfg like '%balluff%' or pv.mfg like '%mcquay%')

-- INCORRECT VERSION WHERE LACK OF PARENS CAUSES CARTESIAN PRODUCT
select distinct rfq.`Unique Identifier`, pv.eid, rfq.`Manufacturer Part Number` AS 'RS mpn', pv.mpn as 'capp mpn', pv.cost, pv.list, pv.list_eff
from rfq join pv on rfq.`Manufacturer Part Number` = pv.mpn
and pv.mfg like '%siemens%' or pv.mfg like '%balluff%' or pv.mfg like '%mcquay%'
```

SEARCH / GLOBBING
* not portable across DBMS 📙 Karwin [15]
* wildcards: `_` single char `%` n char 📙 Beaulieu [80] https://amjith.com/blog/2023/postgres-and-underscore/
* regex in SQLite
```sql
select id from prod_class where id glob '*[^0-9]*' limit 5
select * from customers where name like '%gobain%'

-- dynamic with join
WITH brand_codes AS (
    SELECT brand, priceline, buyline
    FROM pdr
    WHERE brand = 'Copeland'
)
SELECT pv.* FROM pv
JOIN
    brand_codes bc ON (
        pv.mfg LIKE '%' || bc.brand || '%' OR
        pv.priceline = bc.priceline OR
        pv.buyline = bc.buyline
    )
```

ZA
```sql
-- membership
where first_name in ('alice', 'bob'); -- how subqueries work 📙 Beaulieu 4.71
-- math
select (select count(*) from customers where bill_to_id != '') * 100.0 / (select count(*) from customers)
-- string truthy/falsy
select count(*) from executions where height != ''
```

---

case statements
```sql
--- only enforce mfg filter against Trane et. al when mfg = Honeywell
SELECT p.mpn, p.list_price, p.list_price_effective_date
FROM ext
JOIN products p ON ext.manufacturer_part_number = p.mpn
WHERE CASE 
    WHEN ext.manufacturer = 'HONEYWELL' THEN p.mfg NOT IN ('Trane', 'Carrier', 'NORTH SAFETY')
    ELSE TRUE
END
```

SEARCH / GLOBBING
```sql
-- '%query%' = contained anywhere
-- https://github.com/enochtangg/quick-SQL-cheatsheet#1-finding-data-queries
select artists, genres from artist where genres like '%rock%'

LIKE 'foo%'; -- starts w/ 'foo'; '%' is n char [Beaulieu 4.74-5]
LIKE '%foo'; -- ends w/ 'foo'
LIKE '_foo'; -- has a single char before 'foo'
LIKE '%foo%'; -- contains anywhere https://pgexercises.com/questions/basic/where3.html

ILIKE 'Foo'; -- case sensitive
ILIKE 'foo'; -- case insensitive https://docs.djangoproject.com/en/3.1/ref/models/querysets/#iexact

where RIGHT(<col>, 3); -- 📍 slice right: select subset of string ending with index n [Beaulieu 3.59]
where LEFT(<col>, 1) = 'T'; -- attr starts w/ 'T' -- left: select subset of string starting with index n [Beaulieu 4.73]
```

## select

```sql
-- DUMMY COLUMN / CONSTANT PROJECTION: just returns a placeholder for each matching row
select 1 from foo

-- SELECT ALL
select tbl1.*, tbl2.foo

-- CONCATENATE https://pgexercises.com/questions/joins/threejoin.html
select * from products p join cat c
on 'CS' || p.eid = c.product_id  -- eid 1234 produc_id CS1234

-- TRUNCATE OUTPUT
select substr(description, 1, 10) from products where eid = 1000004
```

---

ALIASES
* _alias_: shorthand for identifier
* need n aliases if using same table more than once 📙 Beaulieu 5.92
* `AS` not necessary but advisable 📙 Beaulieu [51] used about half the time [57] https://www.sqlstyle.guide/#aliasing-or-correlations
```sql
select first_name || ' ' || last_name as full_name  -- column alias
    from people as p  -- table alias
    order by full_name  -- can be used in other commands

-- result set labelling
select count(addr) as "listings", max(price) as "high", min(price) as "low" from house
```

ZA
* syntax: select (attrs) from (tables) where (records) 📙 Molinaro 1.1
* _compound query_: combines multiple `SELECT` 📙 Beaulieu [105]
* _scalar query_: query that returns single cell https://stackoverflow.com/a/20425116
* TOP: LIMIT for MySQL https://github.com/enochtangg/quick-SQL-cheatsheet#1-finding-data-queries 📙 Evans 13
* _ordinal notation_: refer to columns in select as ordinals https://stackoverflow.com/q/2253040
```sql
-- DESC: must be final clause
-- ASC: default, which is why you never see it 📙 Beaulieu [63]
select "First Name", count(*) from executions group by "First Name" order by count(*) desc

-- case statements https://pgexercises.com/questions/basic/classify.html https://pgexercises.com/questions/joins/threejoin2.html
SELECT NAME,
	CASE
        WHEN (monthlymaintenance > 100)
        THEN 'expensive'
        ELSE 'cheap'
        END
    AS cost
FROM cd.facilities;  
```

## subqueries

📙 Beaulieu ch. 9

* _subquery_: parenthesized query contained within larger query 📙 Beaulieu [53]
* more readable but generally slower than joins https://stackoverflow.com/a/2577224 https://stackoverflow.com/a/2577188
* _containing query_: query that wraps subquery 📙 Beaulieu [54]
```sql
-- PERCENTAGE OF ATTR W/ VAL
select
  (select count(*) from customers where bill_to_id != '') * 100.0 /
  (select count(*) from customers)
```
* _scalar subquery_: return single val https://learnsql.com/blog/subquery-vs-join/
```sql
containing_query = (subquery)  -- 1 (scalar)
containing_query in (subquery)  -- n
```

# 🐧 GROUPING

🗄 `math.md` stat
📚
* Beaulieu ch. 8
* Evans 8

## group by

* _group by_: form group for each unique combo
* _agg column_: agg func applied to all rows in group
* _regular column_: first row in group
* regular column has dedupe side effect 📙 Evans [8]
```sql
select * from orders
+----+----------+---------+--------+
| id | customer | product | amount |
+----+----------+---------+--------+
| 1  | alice    | widget  | 100    |
| 2  | alice    | widget  | 150    |
| 3  | bob      | gadget  | 200    |
| 4  | bob      | gadget  | 175    |
| 5  | carl     | widget  | 225    |
+----+----------+---------+--------+

-- REGULAR COLUMNS
select * from orders group by customer, product
+----+----------+---------+--------+
| id | customer | product | amount |
+----+----------+---------+--------+
| 1  | alice    | widget  | 100    |
| 3  | bob      | gadget  | 200    |
| 5  | carl     | widget  | 225    |
+----+----------+---------+--------+

-- AGG COLUMNS
select customer, product, id, -- regular columns
count(*) as cnt, sum(amount) total -- agg columns
from orders group by customer, product;
+----------+---------+----+-----+-------+
| customer | product | id | cnt | total |
+----------+---------+----+-----+-------+
| alice    | widget  | 1  | 2   | 250   |
| bob      | gadget  | 3  | 2   | 375   |
| carl     | widget  | 5  | 1   | 225   |
+----------+---------+----+-----+-------+

-- ACCESSING ALL ROWS FROM REGULAR COLUMN
select customer, count(*) as cnt, group_concat(product) as products
from orders group by customer
+----------+-----+---------------+
| customer | cnt | products      |
+----------+-----+---------------+
| alice    | 2   | widget,widget |
| bob      | 2   | gadget,gadget |
| carl     | 1   | widget        |
+----------+-----+---------------+
select customer, count(*) as cnt, group_concat(id || ':' || product) as products
from orders group by customer;
+----------+-----+-------------------+
| customer | cnt | products          |
+----------+-----+-------------------+
| alice    | 2   | 1:widget,2:widget |
| bob      | 2   | 3:gadget,4:gadget |
| carl     | 1   | 5:widget          |
+----------+-----+-------------------+
```

---

diff polars vs. pandas https://labs.quansight.org/blog/dataframe-group-by

GROUP BY
* group data by column value 📙 Beaulieu [60]
* aka binning https://hakibenita.com/sql-for-data-analysis#binning
* aka pivot table https://hakibenita.com/sql-for-data-analysis#pivot-tables https://realpython.com/how-to-pandas-pivot-table/
```sql
-- only columns worth selecting are the grouped by column and aggregates
select count(*) from executions group by "First Name" 
select "First Name", count(*) from executions group by "First Name" 
select "First Name", count(*) from executions group by "First Name" order by 2 desc

-- can't usefully access non-aggregated columns
-- e.g. this query will bring back an execution age for one of the prisoners in the group, but what good is that?
select "Age at Execution" from executions group by "First Name" 
```
* 📍 practice https://www.helenanderson.co.nz/sql-aggregate-functions/
* 📍 rollup https://hakibenita.com/sql-for-data-analysis#subtotals
* 📍 rolling https://ponder.io/python-for-finance-pandas-resample-groupby-and-rolling/
* https://stackoverflow.com/a/24767207
```sql
select col, count(*) from tab group by col
```

## partition by

---

https://grok.com/chat/d8b45276-4216-4441-bc72-febc2bb8f54a

* _partition_: group by but retain individual records w/ group https://stackoverflow.com/a/2404574
* can do in DDL? https://www.postgresql.org/docs/10/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE
* group created for aggregation 📙 Molinaro
* this tutorial is just ok https://www.youtube.com/watch?v=6trOvsL80Oo
* https://www.youtube.com/watch?v=EPUayNC5ku4
* used for bulk deletes in audit table https://sqlfordevs.com/partition-delete-old-rows

## window functions

---

https://grok.com/chat/d8b45276-4216-4441-bc72-febc2bb8f54a

📙 Evans 14-16

* _window_: reference value in previous row 📙 Evans 14
* introduced to SQL in 2005 https://www.youtube.com/watch?v=H6OTMoXjNiM 0:30
```sql
-- syntax
expression OVER (window)
-- functions https://twitter.com/b0rk/status/1179419244808851462/photo/1
lag() sum() ntile() row_number()
```
* link to partition by https://twitter.com/b0rk/status/1179419244808851462/photo/1
* https://www.postgresql.org/docs/9.1/tutorial-window.html
* 📙 Winand 156
* https://www.youtube.com/watch?v=XBE09l-UYTE
* types https://www.helenanderson.co.nz/sql-window-functions-part-1/
* running total https://learnsql.com/blog/what-is-a-running-total-and-how-to-compute-it-in-sql/ https://learnsql.com/blog/sql-non-equi-joins-examples/
* https://hakibenita.com/sql-for-data-analysis#running-and-cumulative-aggregation

# 🧩 JOINS

📙 Beaulieu ch. 5/10

BASICS
* _join_: RS incl attr from n tables based on predicate 📙 Beaulieu [88]
* _driving table (DT)_: starting point of join 📙 Beaulieu [95]
* _through table (TT)_: tables included in the join
* _join narrowing_: additional joins winnow RS count
```sql
select deal.deal_id, house.addr
from deal join house on deal.house = house.house_id
join renter on deal.renter = renter.renter_id
```

ZA
* fuzzy matching join
```sql

```
* predicate syntax history (if no predicate you'd get a cartesian RS) 📙 Beaulieu [35]
```sql
-- WHERE: old syntax 📙 Beaulieu [91]
select * from employee, lob where employee.lob_id = lob.id
-- ON: new syntax (SQL92), portable across dbms 📙 Beaulieu [92]
select * from employee, lob on employee.lob_id = lob.id
-- USING_: use w/ equi join if tables have attr w/ same name 📙 Beaulieu [90] https://www.neilwithdata.com/join-using
select * from employee, lob using (lob_id)
```

---

* merge, right join https://blog.jooq.org/think-about-sql-merge-in-terms-of-a-right-join/
* anti-left https://claude.ai/chat/cc161c00-15d7-40b6-9338-80850b170020 https://claude.ai/chat/485f24b8-a7c6-4cec-8e02-5b392038a30e https://grok.com/chat/562a547e-0b7a-4954-816c-0c587a52faaf https://claude.ai/chat/cd451018-b085-47dd-b971-74df3281ed7e
* https://antonz.org/sql-join/
* https://news.ycombinator.com/item?id=36575784
* https://github.com/enochtangg/quick-SQL-cheatsheet#joins
* visual https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/ https://news.ycombinator.com/item?id=27760154
* wat https://alexpetralia.com/posts/2017/7/19/more-dangerous-subtleties-of-joins-in-sql
* lateral https://sqlfordevs.com/for-each-loop-lateral-join

## IO/LR

* _inner_: RS !incl records for which join fails (dbms default) 📙 Beaulieu [90] Evans [10]
* _outer_: RS incl records for which join fails 📙 Beaulieu [90]
* _left_: outer + DT determines RS count + TT provides matches 📙 Beaulieu [187] Evans [11-12]
```sh
litecli :memory:
```
```sql
create temporary table foo (id);
insert into foo (id) values (1), (2), (4);
create temporary table bar (id);
insert into bar (id) values (1), (2), (3), (4), (5);

select bar.id from bar
left join foo on bar.id = foo.id
where foo.id is null
-- output: 3, 5
```
* _right_: outer + TT determines RS count + DT provides matches 📙 Beaulieu [187]
* _full_: outer + all rows from DT/TT in RS 📙 Beaulieu [187]
```sql
select r.name, d.deal_id
from renter as r
left join deal as d on r.renter_id = d.renter
+---------------+---------+
| name          | deal_id |
+---------------+---------+
| helen boss    | 1       |
| michael lane  | 4       |
| susan sanders | <null>  |
| tom white     | 2       |
| sofia brown   | 3       |
+---------------+---------+
```

## self/cross/natural

* _multi_: use same table n times, need to use multiple aliases 📙 Beaulieu [96-7]
```sql
SELECT *
FROM rfq
    JOIN pv AS pv1 ON rfq.`MANUFACTURER PART NUMBER` = pv1.mpn
    JOIN pv AS pv2 ON rfq.`Manufacturer` = pv2.mfg

select count(*)
from rfq
    join pv on rfq.`MANUFACTURER PART NUMBER` = pv.mpn
    join pv on rfq.`Manufacturer` = pv.mfg
--- ambiguous column name: pv.mpn
```
* _self_: two instances of same table 📙 Beaulieu [98]
* _cross_: generates cartesian product due to lack of `on` clause 📙 Beaulieu [89] Takahashi [42] 🗄 `math.md` set theory
* canonical example
```sql
SELECT * FROM employees
CROSS JOIN departments;

-- SAMPLE DATA
CREATE TABLE employees (
    employee_id INT,
    employee_name VARCHAR(50)
);
CREATE TABLE departments (
    department_id INT,
    department_name VARCHAR(50)
);
INSERT INTO employees VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO departments VALUES (101, 'HR'), (102, 'Engineering'), (103, 'Finance');

employee_id | employee_name | department_id | department_name
------------|---------------|---------------|----------------
1           | Alice         | 101           | HR
1           | Alice         | 102           | Engineering
1           | Alice         | 103           | Finance
2           | Bob           | 101           | HR
2           | Bob           | 102           | Engineering
2           | Bob           | 103           | Finance
```
* hardcore example
```sql
-- The comma in the FROM clause is a shorthand for a CROSS JOIN. In your query, after the explicit JOIN between entity_pn and the subquery alias prod, the comma brings in another derived table (the subquery aliased as total) without any join condition. This means that the result of the join between entity_pn and prod is combined with the single-row result from the total subquery via a cross join.
select count(*) * 100.0 / total.total_count as 'match %'
from entity_pn
join (select manufacturer_part_number from products where manufacturer_part_number != '') as prod
on entity_part_number = prod.manufacturer_part_number,
(select count(*) as total_count from entity_pn where entity_part_number != '') as total;
+--------------------+
| match %            |
+--------------------+
| 11.912705110704556 |
+--------------------+
```
* _natural_: don't specify `on` clause i.e. server figures out (only if matching attr name across tables) i.e. don't use 📙 Beaulieu [198]
* _equi_: equality 📙 Beaulieu [94-digital-copy]
* _non-equi_: membership https://learnsql.com/blog/sql-non-equi-joins-examples/ 📙 Beaulieu [94-digital-copy]
```sql
-- TRICK FOR BOTH OF THESE IS USING A NON-EQUI JOIN TO UNMATCH PERMUTATIONS 🗄 `MATH.MD` SET THEORY
SELECT r1.name, r1.district, r2.name, r2.district
FROM renter as r1
    JOIN renter r2 ON r1.district = r2.district
    AND r1.renter_id < r2.renter_id
-- FIND DUPES
select h1.house_id, h1.addr as "first occurence", h2.house_id, h2.addr as "second occurence"
from house as h1
    join house as h2 on h1.addr = h2.addr
    and h1.house_id < h2.house_id
-- RECOMMENDATIONS
select r.name, h.house_id, h.district, h.addr, h.bedrooms, h.price
from renter as r
join house as h
    on r.district = h.district
    and h.price between r.rent_min and r.rent_max
    and r.bedrooms <= h.bedrooms
where h.house_id not in (select house from deal)
```

# 🔑 KEYS

ATTR TYPES
* _keys_: attr owned by table (PK) or reference other tables (FK)
* _instrinic_: attr owned by and define characteristics of table; aka descriptive
```sql
CREATE TABLE customer (
    id TEXT PRIMARY KEY, -- PK
    bill_to_id TEXT,     -- FK
    name TEXT,           -- intrinsic
);
```

---

* https://news.ycombinator.com/item?id=44026201
* Capp identifiers vs. classifications vs. attributes https://grok.com/chat/977a1321-578e-4e0d-9895-db2df5005838
* fixing dupe primary https://www.crunchydata.com/blog/postgres-troubleshooting-fixing-duplicate-primary-key-rows

## primary (PK)

🗄 indexing `connolly.pdf`

* _candidate key_: key(s) that could serve as PK https://stackoverflow.com/a/12813385 📙 Winand [5]
* _primary key_: attr w/ unique constraint that serves as ID of record 📙 Beaulieu [6]
* _composite key_: n keys unique together used as PK https://csirmazbendeguz.github.io/2025/04/15/you-dont-need-composite-primary-keys.html
* use in pre-sorted tables (sorted by key vs. time of insertion) for faster lookups https://sqlfordevs.com/sorted-table-faster-range-scan range scan unique scan skip scan https://sqlfordevs.com/sorted-table-faster-range-scan
* slower than surrogate https://news.ycombinator.com/item?id=2786238
* https://github.com/aswinkarthik/csvdiff
* https://sirupsen.com/napkin/problem-5
* _compound key_: composite key + all keys also FK https://en.wikipedia.org/wiki/Composite_key
* e.g. join table https://www.youtube.com/watch?v=vsGDtnBCwgg
* sometimes used interchangeably w/ 'composite' https://dba.stackexchange.com/a/3137/201798 https://www.youtube.com/watch?v=lnfrcHdE_HI 1:40
```sql
-- TODO
```
* _natural key_: attr that goes together with other attr in table (vs. surrogate key) https://news.ycombinator.com/item?id=40580549
* _surrogate key_: unrelated to table attr https://stackoverflow.com/a/36773462
* typically auto-incremented but doesn't necessarily have to be 📙 Beaulieu [34]
```sql
-- TODO
```
* _sequence_: https://stackoverflow.com/a/1649128 📙 Beaulieu [34] Karwin ch. 4
* don't expose via API, use uuid https://0of1.com/blog/posts/django-staples/
* auto-increment https://retool.com/blog/how-to-work-with-auto-increment-in-sql-query/ aka identity column https://www.sqltutorial.org/sql-identity/
```sql
-- TODO
```

## foreign (FK)

🗄️ `analytics.md` EDA

* _foreign key_: constraint enforcing reference to another table's PK 📙 Beaulieu [33,39]
```sql
foreign key (band) references bands (band_id)
```
* aka referential integrity aka prevent garbage in garbage out https://www.postgresql.org/docs/8.3/tutorial-fk.html
* footguns https://djangotv.com/videos/djangocon-europe/2025/djangocon-europe-2025-how-to-get-foreign-keys-horribly-wrong-in-django/
* _parent_: table to which FK refers 📙 Beaulieu [40] https://sqlite.org/foreignkeys.html#fk_basics
* _child_: table w/ FK 📙 Beaulieu [40] 5.82
* can be self-referencing? 📙 Beaulieu 5.93
* find FK referencing table ` SELECT * FROM information_schema.TABLE_CONSTRAINTS WHERE CONSTRAINT_SCHEMA='tableName' AND CONSTRAINT_TYPE='FOREIGN KEY'`
* bad when it comes to sharing and migrations? https://github.com/github/gh-ost/issues/331#issuecomment-266027731
* https://www.semicolonandsons.com/episode/foreign-keys-and-uniqueness-constraints
* _dangling identifier_: bad FK bc pointing to no longer extant ID

# 🗺️ SCHEMA (DDL)

🗄️ `data/modeling.md` name spaces

COMMANDS
```sql
-- DB/TABLE
CREATE DATABASE <db>;  -- `sqlite3 local.db`
CREATE TABLE test_table ();
ALTER TABLE old_name RENAME TO new_name;
DROP TABLE <table>;
DROP DATABASE <db>;

-- ATTR
ALTER TABLE <table> ADD <col> <type>;  -- add
ALTER TABLE <table> ALTER COLUMN <col> TYPE <type> -- update type https://news.ycombinator.com/item?id=40286403
UPDATE <table> set <col>=concat('prependThis_', <col>)  -- update name
ALTER TABLE $tbl RENAME COLUMN $old_name TO $new_name
ALTER TABLE <table> DROP COLUMN <col>; -- rm  https://www.thenile.dev/blog/drop-column
DESCRIBE mytable; -- list constraints/indexes
SHOW CREATE TABLE <tab>; -- MySQL version https://serverfault.com/q/231952 https://stackoverflow.com/a/201678
PRAGMA index_list('<tab>') -- SQLite version https://stackoverflow.com/a/49311235
```

## approaches

� core insight: let the data tell you what it is, rather than forcing it into predetermined boxes
🗄️
* `modeling.md`
* `ai/clients.md` in use > db
* `OLAP.md` pipelines
* `stat.md` outlier detection

* _schema on-read_: enforce contraints on write
* _schema on-write_: don't enforce contraints until write https://www.hytradboi.com/2025/0e959091-26f0-43fa-87e0-b2c1e4536f6b-shapeshifter-using-llms-inside-a-database-for-schema-flexibility
```python
class Catalog:
    """
    >>> cat = Catalog()
    >>> cat.add_product({'sku': 1234, 'name': 'foo'})
    >>> cat.add_product({'sku': 5678, 'name': 'bar'}, mode='strict')
    >>> cat.get_product(sku=1234)
    """
    def __init__(self):
        self.products = []

    def __repr__(self):
        return f'{self.products}'

    def _validate_product(self, product, mode):
        required = {'sku', 'name'}
        if mode == 'strict':
            required |= {'price'}
        missing = required - set(product)
        if missing:
            raise ValueError(f"missing required fields: {' '.join(missing)}")

    def add_product(self, product, mode='flex'):
        self._validate_product(product, mode)
        self.products.append(product)

    def get_product(self, sku):
        defaults = {'price': None}
        for product in self.products:
            if product['sku'] == sku:
                return {**defaults, **product}
        return None
```
* _schema-first_: define upfront
* _schema-aware_: learns schema
```sh
# infers: book title (text), author name (text), year (integer)
add-book "Snow Crash" "Neal Stephenson" 1992

# "there's a publisher field now. Should I update the schema? Y/N"
# On Y: Adds publisher column, leaves it NULL for previous entries
add-book "Neuromancer" "William Gibson" 1984 "Ace Books"

# "I notice you're adding categories. Should these be: single text field with comma-separated values | separate table with a many-to-many relationship?"
add-book "Dune" "Frank Herbert" 1965 "Chilton Books" "sci-fi, politics"
```
* _constraint inference_: pattern detection
* start permissive, get strict only when patterns emerge i.e. opposite of traditional db design where you define everything upfront
```sh
# distribution: if every book year is between 1900-2024
system: "should i enforce year >= 1900?"

# normalization: if you enter "ace books" multiple times
System: "I notice 'Ace Books' appears often. Make it a foreign key?"

# typing: if ISBN field always matches \d{13}|\d{10}
System: "This looks like an ISBN. Add format validation?"
```

## constraints

📙 Beaulieu chapter 13

* _constraint_: rule for attr type/value 📙 Beaulieu [30]

TYPES
* _not null_: https://www.semicolonandsons.com/episode/data-integrity-null-constraint-check-constraint
* interpolation https://hakibenita.com/sql-for-data-analysis#interpolation
* _unique_: prevents dupes values in column https://stackoverflow.com/a/21049722/6813490 https://www.semicolonandsons.com/episode/foreign-keys-and-uniqueness-constraints
* _default_: value that will be inserted in the absence of an explicit value in an insert / update statement https://stackoverflow.com/a/11862246/6813490
```sql
CREATE TABLE test_table (
    foo default 'this is the default value', -- https://www.youtube.com/watch?v=lnfrcHdE_HI 3:15
```
* _check_: value for attr must satisfy boolean expression https://www.semicolonandsons.com/episode/data-integrity-null-constraint-check-constraint 📙 Beaulieu [30]
```sql
-- https://www.postgresql.org/docs/12/ddl-constraints.html#DDL-CONSTRAINTS-CHECK-CONSTRAINTS
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CHECK (price > 0)
);
```

## migrations

💻 `lang/python/django/migrations-sandbox`
🗄
*️ `api.md` schema
* `architecture.md` factors > compatibility
* `infra.md` deployment
* `task-mgmt.md` Task Warrior > database https://github.com/zachvalenta/dotfiles-mini23/blob/main/cli/taskwarrior.sql
* `data/eng.md` pipelines
* `django.md` migrations

TOOLS
* https://atlasgo.io/
* pgroll, squitch https://news.ycombinator.com/item?id=42388973
* https://github.com/sqldef/sqldef
* https://github.com/xataio/pgroll
* https://github.com/sqldef/sqldef/tree/master

DATA
* _data migration_: DML i.e. change data itself
* prod data in lower env is bad? https://www.thoughtworks.com/radar/techniques/production-data-in-test-environments
* backsies https://news.ycombinator.com/item?id=30788768
* dry run https://adamj.eu/tech/2022/10/13/dry-run-mode-for-data-imports-in-django/
* _fixture_: data migration using serialization
* _factory_: data migration using ORM obj https://github.com/FactoryBoy/factory_boy/

FLYWAY
https://flywaydb.org/documentation/ https://github.com/zachvalenta/flyway-tutorial
* how it works
> It's semi automatic because it does not find out what has actually changed in your model. You need to write actual SQL scripts that have versions. It will create a separate table to keep track what version you have in your data base and that execute the script automatically up to the point where the latest version is reached.
* _alternatives_: Liquibase https://return.co.de/blog/articles/java-development-fast/ https://github.com/amacneil/dbmate
* _CLI_: db you're connected to, what migrations need to be run; selects subset of `flyway_schema_history`; can change name of `flyway_schema_history` in `flyway.conf > flway.table`
* _config_: `flyway.conf` unless overriden from CLI
* _directory structure_: `flyway` (CLI; bash script gathers input and then runs Flyway, itself a Java app) `lib` (actual Flyway application) `sql` (ur scripts here)
* _migration script location_: `classpath:db/migration` (in src) `libexec/sql` (in local Flyway install)
* _naming conventions_: whole numbers or timestamps, pad your numbers, don't alter in `flyway.conf`
* _types_: versioned (default) repeatable https://flywaydb.org/getstarted/repeatable undo https://flywaydb.org/getstarted/undo just make a new migration file (vs. using `flyway repair`) ['How to Correct a Mistake in a Migration']
* _versions_: looks at `version` table; version numbers https://flywaydb.org/documentation/migrations#naming
* _with Java_: if you drop tables and rerun app, run `mvn clean install` before rerun (think something cached between runs (in `target`?) indicating that scripts have already been run --> this is weird bc Flyway should look to version table in the database for that)

SCHEMA
* _schema migration_: DDL i.e. change schema (alongside related change in src) https://en.wikipedia.org/wiki/Schema_migration
* https://news.ycombinator.com/item?id=40186752
* no needs to manually alter tables https://realpython.com/django-migrations-a-primer/#ensuring-model-definitions-and-the-database-schema-in-sync
* can be generated from model changes https://realpython.com/django-migrations-a-primer/#avoiding-repetition
* version controllable https://realpython.com/django-migrations-a-primer/#tracking-database-schema-change-in-version-control
* aids deployment (easy rollback to previous) 🗄 `system.md` deployment
* don't run on app start https://pythonspeed.com/articles/schema-migrations-server-startup/
* BYO https://news.ycombinator.com/item?id=24577239
* moving to a difference schema entirely
```txt
There was zero downtime over the course of development. So, at no point in time could we stop support for the old model, migrate, and then start with the new model. Here’s how that worked:

* Update everything that reads the data model to support both the old and new models.
* Update everything that updates the data model to support both.
* Update everything that creates to use the new model.
* Run a task to migrate existing data to the new model.
* Once everything above is stable on prod (we waited a sprint), drop support of the old data model.
* Rename the fields in the old data model so that anything that still depends on them will break.
* (TODO) Actually delete the old data model.

This makes development much more involved than the traditional “flip a switch” approach. Namely, we have two parallel codebases live for a period of time. But, there are some advantages:

* No downtime.
* Other developers don’t have to ask “Do I develop X feature against the new model or old?”. They develop it against whatever code is currently checked in.
* You can safely roll back at any time.
* You can migrate data incrementally.
```

---

https://news.ycombinator.com/item?id=41935730
https://github.com/xataio/pgroll
https://xata.io/blog/migrations-and-exclusive-locks
https://github.com/pressly/goose
https://github.com/amacneil/dbmate#alternatives
* SQLite https://news.ycombinator.com/item?id=31249823
* https://github.com/fabianlindfors/reshape
* linear migrations https://github.com/adamchainz/django-linear-migrations?utm_campaign=Django%2BNewsletter&utm_medium=email&utm_source=Django_Newsletter_89

failover, failback https://www.highgo.ca/2023/04/10/setting-up-postgresql-failover-and-failback-the-right-way/

schema migrations - scenarios
* https://www.caktusgroup.com/blog/2021/05/25/django-migrations-and-deployment
* _rollback_: https://about.gitlab.com/blog/2020/09/16/year-of-kubernetes/
> We learned in the process of moving from VMs to Kubernetes that it was extremely beneficial for us to have an easy way to move traffic between the old and new infrastructure, and to keep legacy infrastructure available for rollback in the first few days after the migration.
> And if what you care about is downtime, your first thought shouldn’t be "how do I reduce deployment downtime from 1 second to 1ms", it should be "how can I ensure database schema changes don’t prevent rollback if I screw something up." - https://pythonspeed.com/articles/dont-need-kubernetes/
> Applying a schema migration to a production database is always a risk...the migration process needs a high level of discipline, thorough testing and a sound backup strategy. https://en.wikipedia.org/wiki/Template:Database https://en.wikipedia.org/wiki/Schema_migration
* _rm attr_: instead of dropping can just hide from interface https://www.reddit.com/r/django/comments/47k7kl/how_do_i_make_a_migration_without_dropping_columns/
* _add attr_: nullable or add default for old records; if nullable, need to update API if you don't want to return those null values; defaults not recommended [Kleppmann 4.130]
> in Django, if you add default at model level, the old records are still null, yes? so you'd still have to update API to handle those, as you would if you'd made the attr nullable
> in Django, how do people handle the one-off default for existing data? before you have prod data, foo values seem fine, but curious to hear a discussion on this topic
```diff
class Foo(models.Model):
    bar = models.CharField(max_length=255)
+   baz = models.CharField(max_length=255, null=True)
```
```sh
+----+---------+----------+
| id | bar     | baz      |
+----+--------------------+
| 1  | bar val | <null>   |
| 2  | bar val | baz val  |
+----+--------------------+
```

* _sink_: https://www.tarynpivots.com/post/migrating-40tb-sql-server-database/ https://github.blog/2020-02-14-automating-mysql-schema-migrations-with-github-actions-and-more/ pivot https://news.ycombinator.com/item?id=39353502

## typing

📜 https://www.postgresql.org/docs/current/datatype.html
🗄 `db.md` SQLite/design
📙 Beaulieu chapter 7

TYPES
* money https://www.youtube.com/watch?v=lxVzLAHnPOE https://news.ycombinator.com/item?id=41776878
* _char_: fixed e.g. state abbreviations 📙 Beaulieu [20]
* _varchar_: variable 📙 Beaulieu [21]
* _blob_: `text` in Postgres, `longtext` in MySQL https://news.ycombinator.com/item?id=40317485
* _datetime_: https://stackoverflow.com/q/1933720 as integer https://stackoverflow.com/a/17227196 🗄 `sjk/golf` https://news.ycombinator.com/item?id=42364372 https://boringsql.com/posts/know-the-time-in-postgresql/ https://simonwillison.net/2025/May/8/sqlite-create-table-default-timestamp/
```sql
-- how to order by a date in sql when the date col in fmt MM/DD/YYYY (and I think the col type is string not an actual datetime fmt) using sqlite
SELECT p.eid, psub.unit_price, psub.ext_price, ar.subtotal_amt, ar.ord_date
FROM sales_psub psub
JOIN sales_ar ar ON psub.full_ord_id = ar.full_ord_id
JOIN products p ON psub.product_id = p.eid
WHERE psub.product_id = 684148
ORDER BY strftime('%Y-%m-%d', substr(ar.ord_date, 7, 4) || '-' || substr(ar.ord_date, 1, 2) || '-' || substr(ar.ord_date, 4, 2)) DESC
```
* _integer_: 
> The type integer is the common choice, as it offers the best balance between range, storage size, and performance. The smallint type is generally only used if disk space is at a premium. The bigint type is designed to be used when the range of the integer type is insufficient. https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-INT
* _boolean_: 
* _numeric_: int (normal stuff) bigint (item number, GUID) float (precision) [Beaulieu 2.21] 🗄 `math.md` encoding
* avoid non-floating point types unless stricty necessary https://www.sqlstyle.guide/#choosing-data-types
* avoid vendor-specific data types https://www.sqlstyle.guide/#choosing-data-types
* type conversion https://news.ycombinator.com/item?id=28259104
```sql
-- casting
select cast (avg(price) as integer) as "average sale price" from house;
-- timestamp https://pgexercises.com/questions/basic/date.html non-overlapping times https://sqlfordevs.com/non-overlapping-time-ranges more on times https://simonwillison.net/2024/Nov/27/storing-times-for-human-events
YYYY-MM-DD HH:MM:SS  -- fmt
where foo_date > '1962-07-03' -- compare
-- user names
family_name, other_given_names  -- https://www.youtube.com/watch?v=458KmAKq0bQ 7:30 https://www.w3.org/International/questions/qa-personal-names
```

NULL 📙 Beaulieu [32,82]
* check
```sql
where products.mpn is not null
where products.mpn != ''
```
* https://jirevwe.github.io/sql-nulls-are-weird.html
* _null_: absence of a value e.g. `termination_date` for newly hired employee
* wat: an expression can be null but never equal null 📙 Beaulieu [82]
```sql
null != null  -- true 📙 Beaulieu [82]
select (0 is not null) and ('' is not null)  -- true
```

MATH
* integer division yields integer (`select 51/2` = `25`) 🗄 FUQ - percent
* cast to float for precision division https://hakibenita.com/sql-dos-and-donts#be-careful-when-dividing-integers
* for decimals, multiply something by 1.0 (`select 1.0*51 / 2` = `25.5`)
* boolean: `0` falsy `1` truthy https://selectstarsql.com/beazley.html
```sh
select 0 or 1  # 1
```
* avoid doing math w/ floating point https://dba.stackexchange.com/questions/76391/sum-of-double-precision-gives-weird-results
```sql
select track, sum(share), count(*) from splits group by track having sum(share) > 100.0;
foo_isrc,200.0,4
bar_isrc,100.0,10
baz_isrc,100.0,4
qux_isrc,200.0,2

select track, sum(share), count(*) from splits group by track having cast(sum(share) as int) > 100.0;
foo_isrc,200.0,4
qux_isrc,200.0,2
```

# 🪵 TABLES

TYPES
* _table_: set of related rows
* _permanent_: table in storage 📙 Beaulieu [53]
* impl as heap or b-tree https://calpaterson.com/activerecord.html
* _derived_: return from subquery and held in memory 📙 Beaulieu [53]
* _temporary_: table in mem 📙 Beaulieu [53] aka non-persistent 📙 Beaulieu [8]
* _result set (RS)_: temp table returned from query 📙 Beaulieu [8] Evans [4]
* intermediate RS created at each stage in join 📙 Beaulieu [90-digital-copy]
* _virtual_: created using `create view` cmd 📙 Beaulieu [53] https://news.ycombinator.com/item?id=43719830 https://paultraylor.net/blog/2025/sqlite-virutal-tables-django/
* _intemediate_: table instaniated for a job and then deleted https://hakibenita.com/sql-tricks-application-dba#implement-complete-processes-using-with-and-returning
* _scalar table_: table w/ single column and single row https://pgexercises.com/questions/basic/agg2.html
* _temporal_: https://news.ycombinator.com/item?id=29733854 https://news.ycombinator.com/item?id=29735695 https://stackoverflow.com/questions/50199752/comparing-csv-entries-against-entries-in-postgresql-table-using-python 

GENERATED COLUMNS
* _generated column_: col whose value generated based on other columns https://chatgpt.com/c/6734cd95-6754-8004-b89c-8d25d8da8048 https://news.ycombinator.com/item?id=31396578
* _virtual generated columns_: expression for a virtual column is computed at read-time so they're not stored on disk like generated columns
* same as a virtual table? https://llm.datasette.io/en/stable/logging.html
* in Django https://realpython.com/podcasts/rpp/227/ https://www.paulox.net/2023/11/07/database-generated-columns-part-1-django-and-sqlite/#tldr

## CTE

* _CTE (common table expression)_: one-off view using `WITH` keyword
```sql
with web_zombies as (
  select * from products 
  where discontinued = 'Y' and web > 0.001 and list_price <= 0.001
)
select 
  (select count(*) from web_zombies) * 100.0 / 
  (select count(*) from products) as 'web zombie %'
```

WHY?
* _readability_: break complex queries into logical, named components
* _reusability_: reference the same subquery multiple times without duplication

---

* https://hakibenita.com/sql-tricks-application-dba#implement-complete-processes-using-with-and-returning
* https://hakibenita.com/sql-for-data-analysis#common-table-expressions
* https://hakibenita.com/sql-for-data-analysis#sql-vs-pandas-performance
* https://github.com/enochtangg/quick-SQL-cheatsheet#find
* https://chatgpt.com/c/67bf4043-3e88-8004-aa0c-13c54fb38cc2
* https://news.ycombinator.com/item?id=34603691
* https://news.ycombinator.com/item?id=42230384
* Postgres filters as a replacement for https://stokerpostgresql.blogspot.com/2025/02/how-postgresqls-aggregate-filter-will.html
* enable recursive queries (with `with recursive`) http://www.jeffwidman.com/blog/ https://dba.stackexchange.com/q/14490 https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b https://aiven.io/blog/solving-the-knapsack-problem-in-postgresql https://pgexercises.com/questions/recursive/ https://bofh.org.uk/2019/02/25/baking-with-emacs/

## views

📙 Beaulieu chapter 14

```sql
-- CREATE
create view view_name as select column1, column2 from table_name where condition;
-- RM
drop view if exists view_name;

-- EXAMPLES
create view sales as
select psub.full_ord_id, ar.full_ord_id, psub.unit_price, psub.ext_price, ar.subtotal_amt, ar.ord_date
from sales_psub psub join sales_ar ar on psub.full_ord_id = ar.full_ord_id

CREATE VIEW pv AS
SELECT
    eid, mpn, substr(description, 1, 25) as 'desc', -- identifiers
    mfg, buyline, priceline,  -- grouping
    cost, list_price as 'list', list_price_effective_date as 'list_eff', web, year_sales, last_sale, gross_profit as 'gp', -- pricing
    discontinued as 'discon', status,  -- discon
    creator, date_created as 'created', date_updated as 'updated'  -- creation
FROM
    products

-- LIST 🗄️ `analytics.md` REPL > litecli
select name, type from sqlite_master
select name from sqlite_master where type='view';

+------------+-------+
| name       | type  |
+------------+-------+
| customer   | table |
| contact    | table |
| sales_ar   | table |
| catalog    | table |
| mars       | table |
| sales_osub | table |
| prod_class | table |
| entity     | table |
| orders     | table |
| products   | table |
+------------+-------+
```

---

* view columns `pragma table_info('your_view_name');`
* late-binding https://eradman.com/posts/late-binding-views.html
* _view_: pre-computed partial query (e.g. `where is_active = 0`) recomputed as more full query w/ additional user filtering 📙 Kleppmann [101]
* doesn't hold any data itself 📙 Beaulieu [55]
* restrict users to subset of data https://stackoverflow.com/a/4378291/6813490
* simplifies queries for users but lose info about relationships 📙 Beaulieu [56] https://dataschool.com/sql-optimization/views/
* for some dbms (SQLite) you can't write using views https://sqlite.org/omitted.html
* _materialized view_: actual data i.e. cached version of the table https://news.ycombinator.com/item?id=34186098
* faster queries but needs to be manually maintained so not typically used in OLTP 📙 Kleppmann [102]
* maintenance https://github.com/sraoss/pg_ivm
* _data cube_: type of materialized view used in OLAP, precomputed for speed results 📙 Kleppmann [102] https://hakibenita.com/sql-for-data-analysis#cube
* not often used limited query flexiblity 📙 Kleppmann [103]

# 🟨️ ZA

SEMANTICS
* _object_: anything e.g. table, user, trigger https://docs.oracle.com/cd/B19306_01/server.102/b14200/sql_elements007.htm https://github.com/jOOQ/sakila/blob/ee1a637656aec2d82183ab451c56a3845315e761/mysql-sakila-db/mysql-sakila-drop-objects.sql ownership model https://www.red-gate.com/simple-talk/uncategorized/postgresql-basics-object-ownership-and-default-privileges/
* _collation_: order in which char in character set are sorted 📙 Beaulieu [77]
* _fuzzy matching_: merging n datasets that don't have a common UUID e.g. merging contacts based on name https://pbpython.com/record-linking.html
* _deterministic matching_: https://github.com/zinggAI/zingg
* _enrichment_: https://simonwillison.net/2024/Dec/5/datasette-enrichments-llm/

DCL
* _get current user_: `select current_user;` or `select user();`
* _create user_: `CREATE USER alice WITH PASSWORD '1234';` `CREATE USER '<name>'@'localhost';
* scope reads to currrent user https://news.ycombinator.com/item?id=23308945
* give user perms to db
```sql
GRANT ALL PRIVILEGES ON <dbName>.* to '<userName>'@'localhost' WITH GRANT OPTION; 
FLUSH PRIVILEGES;
```
* test user privileges
```sql
mysql -u user_name
USE db_name;
CREATE TABLE test_table (c CHAR(20));
INSERT INTO test_table(name, age) values('zach', 31);
SELECT * FROM test_table;
DROP TABLE test_table;
```

## commands

SEMANTICS 🗄 `language.md` semantics
* _command_: keyword + identifier
* _keyword_: part of SQL lang spec; not case sensitive
* _identifier_: value (cell, attribute); case-sensitive
* quotes: single for value, double for attr https://stackoverflow.com/q/1992314
```sql
SELECT "from" FROM foo WHERE something = 'val';
```
* _query_: `SELECT` command 📙 Karwin [6]
* _statement_: non-`SELECT` commands 📙 Karwin [6]

TYPES
* _DCL_: control; user perms https://stackoverflow.com/a/44898661
* _DDL_: definition; table structure and inter-table relationships https://stackoverflow.com/a/2578207
* _DML_: manipulation; CRUD

KEYWORDS https://www.postgresql.org/docs/8.1/sql-keywords-appendix.html https://www.sqlstyle.guide/#reserved-keyword-reference
* _reserved_: word that cannot use as identifier e.g. `create`
* _non-reserved_: word that you can use as identifier but should use backtickets for e.g. `assertion`, `name`
```sql
-- SQLite and SQL Server use brackets instead of quotes/backticks for this https://llm.datasette.io/en/stable/logging.html
CREATE TABLE [conversations] (
  [id] TEXT PRIMARY KEY,
  [name] TEXT,
  [model] TEXT
);
```
* _keyword_: reserved + non-reserved; case-insensitive
> As a general rule, if you get spurious parser errors for commands that contain any of the listed key words as an identifier you should try to quote the identifier to see if the problem goes away. - https://www.postgresql.org/docs/8.1/static/sql-keywords-appendix.html

## style

TABLES
* case: lower + snake
* avoid reserved words

---

pipe syntax https://www.hytradboi.com/2025/f8582cd3-1e39-43a8-8749-46817b2910cf-pipe-syntax-in-sql-its-time

📜 https://www.sqlstyle.guide/
* ✅ constraints next to the attr they constrain https://www.sqlstyle.guide/#layout-and-order
> this seems to violate parsing rules for SQLite 🗄 `golf`
* ✅ suffixes https://www.sqlstyle.guide/#uniform-suffixes
* ✅ uppercase keywords https://www.sqlstyle.guide/#reserved-words
* indentation along root keywords (select, from, where) https://www.sqlstyle.guide/#indentation https://www.sqlstyle.guide/#spaces
* white space / tabs not significant
* ✅ ubiquitous language ❌ but no Hungarian notation https://news.ycombinator.com/item?id=24403236 
* ✅ starts w/ char, use underscores where you'd use a space in natural language https://www.sqlstyle.guide/#naming-conventions
* ❌ _Hungarian notation_: type in signature https://www.sqlstyle.guide/#tables https://news.ycombinator.com/item?id=24403236
* ❌ through table as concatentation of its constituents https://www.sqlstyle.guide/#tables
* ❌ `id` as PK https://www.sqlstyle.guide/#columns https://github.com/jOOQ/jOOQ/tree/master/jOOQ-examples/Sakila
* ✅ singular for attr https://www.sqlstyle.guide/#columns

LINTING
* https://github.com/alanmcruickshank/sqlfluff https://www.thoughtworks.com/radar/tools?blipid=202203065
* https://www.eversql.com/sql-syntax-check-validator/
* https://github.com/purcell/sqlint
* https://github.com/darold/pgFormatter
* https://sqlfum.pt/
