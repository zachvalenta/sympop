# ⛩️

## 参考

🗄 `distributed.md`
📚
* Petrov database internals
* Kleppmann ch. 3

## 进步

SQLite by Richard Hipp https://www.youtube.com/watch?v=ZSKLA81tBis

query plan (Polars) read vs. scan

* https://github.com/zillow/fcache
* SQL engines https://chatgpt.com/share/6706c793-1428-8004-af11-613cff56c5af https://news.ycombinator.com/item?id=34189422 BYO in Python https://news.ycombinator.com/item?id=43807593
* CMU https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi https://www.youtube.com/playlist?list=PLSE8ODhjZXjasmrEd2_Yi1deeE360zv5O
* _correlation_: correlation btw storage on disk and order of rows https://hakibenita.com/sql-tricks-application-dba#always-load-sorted-data

CHECKSUMS
* https://news.ycombinator.com/item?id=42094663
* https://avi.im/blag/2024/databases-checksum/
* https://avi.im/blag/2024/sqlite-bit-flip/

# 🏎️ ENGINES

substrait https://news.ycombinator.com/item?id=44404876
https://www.dolthub.com/blog/2025-04-25-sql-engine-anatomy/

## query

🗄️ `data/eng.md` query engines
🔗 https://pganalyze.com/blog/how-postgres-chooses-index

* _query optimizer_: generates query plans, picks execution plan 📙 Beaulieu [46] https://news.ycombinator.com/item?id=30855639
* _selection pushdown_: mv predicate ASAP / closer to data source
* e.g. apply `WHERE o.total > 100` before join to reduce amount of data you need to look at
```sql
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date > '2024-01-01'
AND c.country = 'USA'

-- Optimizer pushes filters down:
-- 1. Filter orders table first (order_date > '2024-01-01')
-- 2. Filter customers table first (country = 'USA')  
-- 3. Join the already-filtered datasets
WHERE o.order_date > '2024-01-01'
AND c.country = 'USA'
JOIN customers c ON o.customer_id = c.id
```

---

* how joins work under the hood
> Adding SQL/PGQ in a DBMS is not as simple as adding support for the new syntax. There are several engineering considerations to ensure graph queries perform well. For example, graph queries perform multi-way joins to traverse the graph. But a problem arises when the intermediate results for these joins are larger than the base tables. A DBMS must use a worst-case optimal join (WCOJ) algorithm to execute such joins more efficiently than the usual hash join used when joining two tables. Another important technique is to use factorization to avoid materializing redundant intermediate results during joins. This type of compression helps the DBMS avoid blowing out its memory with the same join record over and over again. https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html
* _database engine_: container for components https://www.sqlite.org/draft/queryplanner.html https://www.practical-mongodb-aggregations.com/intro/introducing-aggregations.html
* lexer: lex, yac https://news.ycombinator.com/item?id=30086374 https://www.interdb.jp/pg/index.html
* _parser_: https://github.com/reata/sqllineage 🗄 `language.md` compiler https://github.com/pganalyze/pg_query
* https://tokern.io/blog/open-source-sql-parsers/
* transpile btw Presto, Hive Spark https://github.com/tobymao/sqlglot

QUERY OPTIMIZER
* effect on perf https://postgres.fm/episodes/performance-cliffs
* returns hints 📙 Beaulieu [46]
* https://www.shayon.dev/post/2025/119/a-postgresql-planner-gotcha-with-ctes-delete-and-limit/
* aka querry planner 📙 Bradshaw [167]
> decides which parts of the query to execute in which order and which indexes to use 📙 Kleppmann 37
* cost-based 📙 Kleppmann 427 https://blog.jooq.org/10-cool-sql-optimisations-that-do-not-depend-on-the-cost-model/ https://pghintplan.osdn.jp/pg_hint_plan.html
* ❓ virtual machine https://news.ycombinator.com/item?id=32750676
* parse https://simonwillison.net/2025/Feb/7/apsw-sqlite-query-explainer/

* _query plan_: output from query optimizer = imperative steps to impl declarative SQL https://www.youtube.com/watch?v=IwahVdNboc8 https://dataschool.com/sql-optimization/what-is-a-query-plan/ 🗄️ `analytics.md` Polars > IO
* https://vondra.me/posts/so-why-dont-we-pick-the-optimal-query-plan/
* https://chriskiehl.com/article/query-plan-management
* _execution plan_: query plan chosen by optimizer 📙 Beaulieu [46]
> There is a trade-off between the amount of time spent figuring out the best query plan and the quality of the choice https://en.wikipedia.org/wiki/Query_optimization
* _query hint_: explicitly tell optimizer what to do 📙 Beaulieu 3.42 https://en.wikipedia.org/wiki/Hint_(SQL)
* Postgres doesn't support https://wiki.postgresql.org/wiki/Todo
* _query engine_: executes query plan https://en.wikipedia.org/wiki/Presto_(SQL_query_engine) https://news.ycombinator.com/item?id=27006476

## storage

🗄 `distributed.md` transactions

---

* _buffer manager_:
> First of all, what does Postgres buffer manager do? Just briefly, Postgres organizes on-disk data files in 8KB fix-sized pages. It also maintains a fixed-size array of page buffers in memory, to cache recent reads and writes of these disk pages and improve performance through caching and lazy disk flush. https://medium.com/@dichenldc/30-years-of-postgresql-buffer-manager-locking-design-evolution-e6e861d7072f
* _transaction_: https://news.ycombinator.com/item?id=36583317
* _transaction wraparound_: https://github.com/orioledb/orioledb 🗄️ vacuuming
```txt
PostgreSQL assigns a unique transaction ID (XID) to each transaction
XIDs are 32-bit integers with ~4 billion possible values
When XIDs approach max value, they "wrap around" back to low numbers
Without intervention, this causes data loss as new transactions might reuse XIDs of active data
```

* commits https://news.ycombinator.com/item?id=43380622
* ACID https://www.youtube.com/watch?v=GAe5oB742dw
* _page_: + heap https://news.ycombinator.com/item?id=41159180 https://simonwillison.net/2025/Feb/6/sqlite-page-explorer/
* https://supabase.com/blog/postgres-bloat
* physical storage https://drew.silcock.dev/blog/how-postgres-stores-data-on-disk/
* locks https://news.ycombinator.com/item?id=35981238 https://leontrolski.github.io/pglockpy.html https://postgres.fm/episodes/locks
* _journal_: journaling i.e. keep track of transactions? https://fly.io/blog/sqlite-internals-rollback-journal/
* _storage engine_: handle transactions, maintain index https://stackoverflow.com/a/39204302
* row-oriented vs. column-oriented 📙 Kleppmann 586
* log-structured (Riak Bitcask) 📙 Kleppmann 72 https://news.ycombinator.com/item?id=42187766
> RocksDB uses a log structured database engine, written entirely in C++, for maximum performance. Keys and values are just arbitrarily-sized byte streams. https://rocksdb.org/
* page-oriented 📙 Kleppmann 70 https://sirupsen.com/napkin/problem-6 https://news.ycombinator.com/item?id=32250426
* _Berkeley DB_: https://corecursive.com/066-sqlite-with-richard-hipp/
* _InnoDB_: MySQL; locks table row during transaction
* _MyISAM_: locks whole table https://stackoverflow.com/a/5414622/6813490 
* _WiredTiger_: Mongo 📙 Bradshaw [6]
* _OrioleDB_: for Postgres https://github.com/orioledb/orioledb/
> OrioleDB is a new storage engine for PostgreSQL. Our teams use PostgreSQL a lot, but its storage engine was originally designed for hard drives. Although there are several options to tune for modern hardware, it can be difficult and cumbersome to achieve optimal results. OrioleDB addresses these challenges by implementing a cloud-native storage engine with explicit support for solid-state drives (SSDs) and nonvolatile random-access memory (NVRAM). To try the new engine, first install the enhancement patches to the current table access methods and then install OrioleDB as a PostgreSQL extension. We believe OrioleDB has great potential to address several long-pending issues in PostgreSQL, and we encourage you to carefully assess it. https://www.thoughtworks.com/radar/platforms?blipid=202210068

## logging

* _commit log_: summary of transaction
```json
{
  "xid": 98765,
  "total_changes": 5,
  "transaction_summary": {
    "tables_affected": ["orders", "order_items", "inventory"],
    "operations": {
      "inserts": 3,
      "updates": 2, 
      "deletes": 0
    },
}
```
* _transaction log_: everything that happened in a single transaction
```json
{
  "xid": 98765,
  "changes": [
    {
      "kind": "insert", 
      "table": "order_items",
      "columnnames": ["order_item_id", "order_id", "product_id", "quantity", "price"],
      "columnvalues": [1001, 12345, 456, 1, 39.99]
    },
    {
      "kind": "update",
      "table": "inventory",
      "columnnames": ["product_id", "stock_quantity"],
      "columnvalues": [456, 23],
      "oldkeys": {"keynames": ["product_id"], "keyvalues": [456]}
    },
  ]
}
```
* _command log_: stream of commands as they happen
```json
{
  "timestamp": "2025-09-07T14:32:18.467123Z",
  "kind": "insert",
  "schema": "public", 
  "table": "order_items",
  "operation": "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (12345, 456, 1, 39.99)",
  "columnnames": ["order_item_id", "order_id", "product_id", "quantity", "price"],
  "columnvalues": [1001, 12345, 456, 1, 39.99]
}
```

---

* https://www.crunchydata.com/blog/postgres-logging-for-performance-optimization
* https://postgres.fm/episodes/what-to-log
* _log_: append-only data file; used to deal w/ concurrency 📙 Kleppmann 71
* _segment_: chunk of log; immutable 📙 Kleppmann 73
* _compaction_: rm dupe keys from log; done by plucking most recent update for key and writing to new, smaller segment file; done in background while continuing to use existing segments for read/write 📙 Kleppmann 73
* fsync log instead of fsyncing data itself to increase throughput? http://aosabook.org/en/nosql.html
> Several data structures, such as B+Trees, help NoSQL systems quickly retrieve data from disk. Updates to those structures result in updates in random locations in the data structures' files, resulting in several random writes per update if you fsync after each update. To reduce random writes, systems such as Cassandra, HBase, Redis, and Riak append update operations to a sequentially-written file called a log. While other data structures used by the system are only periodically fsynced, the log is frequently fsynced. By treating the log as the ground-truth state of the database after a crash, these storage engines are able to turn random updates into sequential ones. While NoSQL systems such as MongoDB perform writes in-place in their data structures, others take logging even further. Cassandra and HBase use a technique borrowed from BigTable of combining their logs and lookup data structures into one log-structured merge tree. Riak provides similar functionality with a log-structured hash table. CouchDB has modified the traditional B+Tree so that all changes to the data structure are appended to the structure on physical storage. These techniques result in improved write throughput, but require a periodic log compaction to keep the log from growing unbounded.

TYPES
* _command log_: log commands to change state but not incremental changes
* _commit log_: append-only list of time-ordered records 📙 Jeffrey distributed [6] https://en.wikipedia.org/wiki/Commit_(data_management)
* _append-only log_: immutability at the db level; conflict w/ GDPR https://www.bloorresearch.com/2018/02/append-databases-gdpr-conundrum/
* _write-ahead log (WAL)_: log changes in state before update so you can recover if failure (power, OS, hw) https://softwareengineeringdaily.com/wp-content/uploads/2018/06/SED613-Database-Reliability-Engineering.pdf BYO https://github.com/khonsulabs/okaywal logical decoding messages https://www.infoq.com/articles/wonders-of-postgres-logical-decoding-messages/ https://pgdash.io/blog/taming-postgresql-wal-file-growth.html https://news.ycombinator.com/item?id=41851051 https://simonwillison.net/2022/Oct/23/datasette-gunicorn distributed https://www.hytradboi.com/2025/f2cc03cb-14fc-42f4-ad38-b4b15a15815f-serverless-primitives-for-the-shared-log-architecture
* used in b-tree 📙 Kleppmann 84
* individual entries known as frames https://news.ycombinator.com/item?id=26583558
* turn off if you're just doing a transformation https://hakibenita.com/sql-tricks-application-dba#use-unlogged-tables-for-intermediate-data

## perf

📙 Winand sql perf https://use-the-index-luke.com/
🗄️
* `dbms.md` indexing
* `telemetry.md` perf

METRICS
* CPU utilization https://news.ycombinator.com/item?id=45110688
* QPS (queries per second)

TACTICS
* use larger instance (lower CPU utilization) https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/
* read replica (higher QPS) https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/

---

* https://2025.djangocon.us/talks/postgresql-tuning-parameters-or-tuning-queries/
* https://postgres.fm/episodes/top-ten-dangerous-issues
* query planner https://postgres.fm/episodes/performance-cliffs
* https://kmoppel.github.io/2025-04-10-postgres-scaling-roadmap/
* https://talkingpostgres.com/episodes/my-journey-into-postgres-monitoring-with-lukas-fittl-rob-treat
* monitoring https://github.com/dalibo/pg_activity
https://www.openmymind.net/Speedig-Up-Queries-Re-Imagining-Your-Data/
https://www.openmymind.net/Speedig-Up-Queries-Understanding-Query-Plans/
* Polars https://chatgpt.com/c/6749f200-3d60-8004-a2ab-1dc8e2c636bb
* use numpy https://realpython.com/numpy-example
* https://substack.com/home/post/p-150506520 https://explain.saby.dev/en/
* https://nchammas.com/writing/database-access-patterns
* https://kmoppel.github.io/2025-04-24-is-striping-postgres-data-volumes-a-free-lunch/
* https://www.crunchydata.com/blog/hacking-the-postgres-statistics-tables-for-faster-queries
* tuning aaS https://ottertune.com/ https://www.cs.cmu.edu/~pavlo/blog/2023/04/the-part-of-postgresql-we-hate-the-most.html
* https://terrastruct.com/blog/post/practical-intermediate-database-tips/
* Postgres
> When modeling a Postgres database, you probably don’t give much thought to the order of columns in your tables. After all, it seems like the kind of thing that wouldn’t affect storage or performance. But what if I told you that simply reordering your columns could reduce the size of your tables and indexes by 20%? This isn’t some obscure database trick — it’s a direct result of how Postgres aligns data on disk.

* https://www.crunchydata.com/blog/is-your-postgres-ready-for-production
@ https://www.figma.com/blog/how-figma-scaled-to-multiple-databases/

EXPLAIN
* https://www.pgmustard.com/blog/postgres-query-plan-visualization-tools
* plan hints https://news.ycombinator.com/item?id=35963572
> In some circumstances, you have knowledge of your data that the optimizer does not have, or cannot have. You might be able to improve the performance of a query by providing additional information to the optimizer https://hakibenita.com/sql-dos-and-donts#add-faux-predicates
* `explain`: view preflight execution plan  https://thoughtbot.com/blog/reading-an-explain-analyze-query-plan https://dataschool.com/sql-optimization/optimization-using-explain/ "returns the steps a database will take to execute a query" https://render.com/blog/postgresql-slow-query-to-fast-via-stats
* how to interpret https://render.com/blog/postgresql-slow-query-to-fast-via-stats
* adds overhead caused by the Volcano model https://www.ongres.com/blog/explain_analyze_may_be_lying_to_you/
* `analyze`: update table stats after bulk index https://sqlfordevs.com/table-maintenance-bulk-modification
* `explain analyze`: view postflight analysis 📙 Evans 25 https://jaywhy13.hashnode.dev/that-time-postgresql-said-no-thanks-i-dont-need-your-index https://www.pgmustard.com/blog/postgres-query-plan-visualization-tools https://dev.to/franckpachot/a-case-where-sql-joins-struggle-but-mongodb-documents-shine-11kj
* `seq scan`:  query plan doesn't use an index 📙 Evans 25
* aka full table scan https://hakibenita.com/sql-tricks-application-dba#always-load-sorted-data
* making sense of Postgres output https://www.pgmustard.com/docs/explain https://explain.depesz.com/
* more precision yields faster query plan
> The query fetches sales that were modified before 2019. There is no index on this field, so the optimizer generates an execution plan to scan the entire table. Let's say you have another field in this table with the time the sale was created. Since it's not possible for a sale to be modified before it was created, adding a similar condition on the created field won't change the result of the query. However, the optimizer might use this information to generate a better execution plan https://hakibenita.com/sql-dos-and-donts#add-faux-predicates
```diff
FROM sale
WHERE modified < '2019-01-01 asia/tel_aviv'
+ AND created < '2019-01-01 asia/tel_aviv'
```

https://www.timescale.com/blog/13-tips-to-improve-postgresql-insert-performance/

* queries: avoid `distinct`, `having`, subqueries, `*` https://dataschool.com/sql-optimization/optimize-your-sql-query/
* query plan
* use indexes
* https://github.com/ankane/pghero
* https://klotzandrew.com/blog/quickly-debugging-postgres-problems
* _QPS (queries per second)_: https://www.youtube.com/watch?v=kEShMV4VfWE
* https://stackoverflow.com/a/11275107/6813490/ 
* https://numeracy.co/blog/life-of-a-sql-query
* https://www.digitalocean.com/community/tutorials/how-to-use-mysql-query-profiling

# 🛠️ MAINTENANCE

https://chatgpt.com/c/68cc8391-c97c-8332-88a1-278e8208142a
https://www.cybertec-postgresql.com/en/database-is-not-accepting-commands/

## vacuuming
## analyze
## reindexing
## checkpoint

# 🔍 INDEXING

📚
* Bradshaw ch. 5
* Winand https://use-the-index-luke.com/
* https://sqlfordevs.com/ebooks/indexing
🗄
* `algos.md` search engine
* `vim.md` ctags

START HERE
* https://testdriven.io/blog/django-db-indexing/
* https://news.ycombinator.com/item?id=42134964
* https://calpaterson.com/how-a-sql-database-works.html
* https://www.jefftk.com/p/you-dont-always-need-indexes
* make invisible > delete https://sqlfordevs.com/invisible-index-before-delete
* https://news.ycombinator.com/item?id=35978757&utm_term=comment
* Postgres has partial indexes
* notes for Karwin chapter 13
> mention of caching? https://hakibenita.com/sql-tricks-application-dba#always-load-sorted-data
* https://dataschool.com/sql-optimization/how-indexing-works/
* BRIN https://hakibenita.com/sql-tricks-application-dba#index-columns-with-high-correlation-using-brin https://www.highgo.ca/2020/06/22/types-of-indexes-in-postgresql/ https://en.wikipedia.org/wiki/Block_Range_Index https://hakibenita.com/postgresql-correlation-brin-multi-minmax
* https://www.youtube.com/watch?v=HubezKbFL7E
* Beaulieu chapter 13, 15
* Faroult 3
* https://github.com/BurntSushi/xsv
* https://news.ycombinator.com/item?id=32250426
* ghost conditions https://sqlfordevs.com/ghost-conditions-for-unindexed-columns

## basics

---

* _index_: binning vs. full table scan 📙 Evans 24
```sql
CREATE INDEX idx_fk_country_id ON city(country_id) -- https://github.com/jOOQ/sakila/blob/main/sqlite-sakila-db/sqlite-sakila-schema.sql
```
* impl: metadata as tree
* subset of data (vs. concordance)
* why: faster reads but slower writes 📙 Kleppmann [71] Karwin [6]
> If you need to access data quickly, you index it...that's 90% of what you need to know https://www.bennadel.com/blog/3467-the-not-so-dark-art-of-designing-database-indexes-reflections-from-an-average-software-engineer.htm
* _reindex_: 📍 https://news.ycombinator.com/item?id=29858083
* _vacuum_: https://news.ycombinator.com/item?id=29858083 https://pgdog.dev/blog/you-can-make-postgres-scale autovacuum https://www.youtube.com/watch?v=RfTD-Twpvac
```txt
* storage reclamation: removes dead tuples (deleted/obsolete rows)
* transaction id wraparound prevention: prevents database age-related failures
* table statistics updates: improves query planning
```
```python
import psycopg2

conn = psycopg2.connect(creds)
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
vacuum_type = "VACUUM FULL" if full else "VACUUM"
table_spec = table_name if table_name else ""
cursor.execute(f"{vacuum_type} {table_spec}")
cursor.close()
conn.close()
```

## data structures

🗄️ `algos.md` data structures

---

* _b-tree_: most popular 📙 Kleppmann 83 Winand vii Petrox ch. 2,4,6
* Postgres vs. SQL Server https://pganalyze.com/blog/postgresql-vs-sql-server-btree-index-deduplication
> The cloud replaces a lot of Enterprise Edition’s HA/DR capabilities – if you needed high availability and disaster recovery scattered across multiple data centers, plus the ability to read from those replicas, AWS could do that for you, even a decade ago. You didn’t have to pay licensing fees for each replica. https://smartpostgres.com/posts/why-i-started-using-postgres-and-you-might-too/
* sorted keys, pointers to range of keys on disk 📙 Kleppmann 80
* bad for filtering? https://sirupsen.com/napkin/problem-13-filtering-with-inverted-indexes
* diff than hash index bc in memory and updates in place (vs. append-only) 📙 Kleppmann 80
> Several data structures, such as B+Trees, help NoSQL systems quickly retrieve data from disk. Updates to those structures result in updates in random locations in the data structures' files, resulting in several random writes per update if you fsync after each update. http://aosabook.org/en/nosql.html
* _bitmap index_: used for low-cardinality columns https://en.wikipedia.org/wiki/Bitmap_index https://www.youtube.com/watch?v=5imhr4ye3Tw 📙 Kleppmann 97, 561
* semantic confusion? https://en.wikipedia.org/wiki/Bitmap https://github.com/RoaringBitmap/roaring
* bitmap scan https://hakibenita.com/sql-tricks-application-dba#always-load-sorted-data https://spacelift.io/blog/tricking-postgres-into-using-query-plan
* _hash index_: in-mem hash table
* V location in physical storage e.g. append-only log as in Riak Bitcask 📙 Kleppmann 72
* hash table must fit in memory 📙 Kleppmann 75 https://hakibenita.com/postgresql-hash-index
* _SSTable (sorted string)_: hash index but sorted keys 📙 Kleppmann 76
* doesn't need to have all keys in memory 📙 Kleppmann 77
* impl w/ LSM tree 📙 Kleppmann 78
* _LSM tree_: faster for writes 📙 Kleppmann 83 Petrov ch. 7 https://news.ycombinator.com/item?id=35634673
* compress more easily 📙 Kleppmann 84
* used in Cassandra, LevelDB 📙 Kleppmann 79, 85 https://nakabonne.dev/posts/write-tsdb-from-scratch/ 🗄 `algos.md` trees
* _BRIN_: https://hakibenita.com/sql-tricks-application-dba#index-columns-with-high-correlation-using-brin

## usage

WHY NOT
* if writes are frequent
* if reads are rare
> When I worked in ads I would often need to debug issues using production logs, and would use Dremel to run a distributed scan of very large amounts of data at interactive speeds. Because queries were relatively rare, an index would have been far more expensive to maintain. https://www.jefftk.com/p/you-dont-always-need-indexes

## types

---

https://www.highgo.ca/2020/06/22/types-of-indexes-in-postgresql/
* _covering_: store additional columns in index https://hakibenita.com/django-32-exciting-features#covering-indexes
> A covering index is when you have an index and it has multiple columns in the index and you’re doing a query on just the first couple of columns in the index and the answer you want is in the remaining columns in the index. When that happens, the database engine can use just the index. It never has to refer to the original table, and that makes things go faster if it only has to look up one thing. https://corecursive.com/066-sqlite-with-richard-hipp/
* _primary_: keeping track of order of entry i.e. having a primary key 📙 Kleppmann 85
* _partial_: normal index + `WHERE` clause https://heap.io/blog/engineering/basic-performance-analysis-saved-us-millions https://hakibenita.com/sql-tricks-application-dba https://dataschool.com/sql-optimization/partial-indexes/ 📙 Bradshaw [5]
* _secondary_: https://calpaterson.com/non-relational-beartraps.html 📙 Kleppmann [85] Bradshaw [5]
* _multicolumn_: aka concatenated 📙 Kleppmann 87 https://dataschool.com/sql-optimization/multicolumn-indexes/

# 🟨 ZA

## async

* Django: not yet supported https://docs.djangoproject.com/en/3.2/topics/async/
* Encode `databases`; adds async to SQLAlchemy https://www.encode.io/databases/database_queries/ https://fastapi.tiangolo.com/advanced/async-sql-databases/
* Postgres: can use async functions that underly synchronous `PQexec` https://www.postgresql.org/docs/9.5/libpq-async.html

## BYO

📙 Dibernardo, Kleppmann

* Volvano model https://news.ycombinator.com/item?id=43956547
* https://blog.sylver.dev/build-your-own-sqlite-part-1-listing-tables 
* CMU Pavlo https://www.youtube.com/watch?v=APqWIjtzNGE
* https://github.com/avinassh/py-caskdb
* https://www.youtube.com/watch?v=5Pc18ge9ohI
* https://tontinton.com/posts/database-fundementals
* https://github.com/spandanb/learndb-py
* https://build-your-own.org/database
* https://build-your-own.org/
* https://github.com/weinberg/SQLToy https://news.ycombinator.com/item?id=26811279 https://github.com/joaoh82/rust_sqlite https://github.com/auxten/go-sqldb https://github.com/erikgrinaker/toydb/blob/master/docs/references.md?utm_source=pocket_mylist https://github.com/codecrafters-io/build-your-own-x#build-your-own-database
* https://architecturenotes.co/things-you-should-know-about-databases/
* https://www.hytradboi.com/
* https://cstack.github.io/db_tutorial/
* https://github.com/eatonphil/gosql
* https://notes.eatonphil.com/database-basics.html
* https://notes.eatonphil.com/database-basics-expressions-and-where.html
* https://notes.eatonphil.com/database-basics-indexes.html
* https://notes.eatonphil.com/database-basics-a-database-sql-driver.html

## connections

ORDER OF OPERATIONS
* auth 📙 Beaulieu [41]
* assign connection ID 📙 Beaulieu [41]
* before each query, check user perms for query, able to access data, and statement syntax 📙 Beaulieu [41]

* _wire protocol_: protocol for db client-server https://datastation.multiprocess.io/blog/2022-02-08-the-world-of-postgresql-wire-compatibility.html https://github.com/crate/crate https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html
* e.g. can translate Mongo protocol to SQL and store in Postgres https://github.com/FerretDB/FerretDB https://pythonbytes.fm/episodes/show/318/gil-how-we-will-miss-you

---

* how rows are stored https://ketansingh.me/posts/how-postgres-stores-rows/
* _connection_: has an ID 📙 Beaulieu [45]
* _connection pool_: cache for connections https://en.wikipedia.org/wiki/Connection_pool
* _pool_: group of open connections we keep around for when the app needs them (vs. opening a new one w/ each request or using a single one for each req) 📙 Conery IH 252 https://brettwooldridge.github.io/HikariCP/ https://brandur.org/postgres-connections
* uses TCP/IP as connection protocol
* _at dbms level_: process per connection (Postgres) coroutine per connection (RethinkDB) https://news.ycombinator.com/item?id=12649712
> The PostgreSQL server can handle multiple concurrent connections from clients. To achieve this it starts (“forks”) a new process for each connection. From that point on, the client and the new server process communicate without intervention by the original postgres process. Thus, the master server process is always running, waiting for client connections, whereas client and associated server processes come and go. - https://www.postgresql.org/docs/12/tutorial-arch.html
* _serialization_: query responses typically in binary and parsed by language specific API 📙 Kleppmann 4.128
* _sink_: https://www.usegolang.com/ in Flask https://stackoverflow.com/questions/16311974/connect-to-a-database-in-flask-which-approach-is-better https://flask.palletsprojects.com/en/1.1.x/tutorial/database/ https://github.com/questionlp/api.wwdt.me https://brandur.org/postgres-connections

## 🦠 FoundationDB

📜 https://github.com/apple/foundationdb/

https://www.complexsystemspodcast.com/episodes/software-testing-with-will-wilson/
over Postgres https://fabianlindfors.se/blog/making-postgres-distributed/
https://www.youtube.com/watch?v=OJb8A6h9jQQ
https://www.youtube.com/watch?v=MqbVoSs0lXk
Swift https://www.youtube.com/watch?v=ZQc9-seU-5k
https://www.dataengineeringpodcast.com/episodepage/foundationdb-distributed-systems-episode-80

> When you choose a database today, you’re not choosing one piece of technology, you’re choosing three: storage technology, data model, and API/query language. For example, if you choose Postgres, you are choosing the Postgres storage engine, a relational data model, and the SQL query language. If you choose MongoDB you are choosing the MongoDB distributed storage engine, a document data model, and the MongoDB API. In systems like these, features are interwoven between all of the layers. For example, both of those systems provide indexes, and the notion of an index exists in all three layers. https://apple.github.io/foundationdb/layer-concept.html

```txt
We now enter the “mind expanding” section of this list, with FoundationDB. Arguably, FoundationDB is not a database, but quite literally the foundation for a database. Used in production by Apple, Snowflake and Tigris Data, FoundationDB is worth your time because it is quite unique in the world of key-value storage.

Yes, it’s an ordered key-value store, but that isn’t what is interesting about it. At first glance, it has some curious limitations - transactions cannot exceed 10MB of affected data and they cannot take longer than five seconds after the first read in a transaction. But, as they say, limits set us free. By having these limits, it can achieve full ACID transactions at very large scale - 100+ TiB clusters are known to be in operation.

FoundationDB is architected for specific workloads and extensively tested using simulation testing, which has been picked up by other technologies, including another database on this list and Antithesis, founded by some ex-FoundationDB folks. For more notes on this, check out Tyler Neely’s and Phil Eaton’s notes on the topic.

As mentioned, FoundationDB has some very specific semantics that take some getting used to - their Anti-Features and Features docs are worth familiarising yourself with to understand the problems they are looking to solve.

But why is it the “layered” database? This is because of the Layers concept. Instead of tying the storage engine to the data model, instead the storage is flexible enough to be remapped across different layers. Tigris Data have a great post about building such a layer, and there are some examples such as a Record layer and a Document layer from the FoundationDB org.

Spend a week going through the tutorials and think about how you could use FoundationDB in place of something like RocksDB. Maybe check out some of the Design Recipes and go read the paper.
```
