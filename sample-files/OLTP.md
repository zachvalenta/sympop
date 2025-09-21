# ⛩️

## 参考

📚
* Connolly database systems
* Takahashi manga databases

## 进步

https://fly.io/blog/litestream-revamped/
neon https://softwareengineeringdaily.com/2025/05/20/building-postgresql-for-the-future-with-heikki-linnakangas/

* _22_: 📙 Bradshaw ch. 1/4/7/10/14/18
* _20_: Postgres with Django (psycopg, Docker) 📙 Kleppmann section 1

# 🕸️ DISTRIBUTED / NewSQL

> you can fit 100M records in single table https://news.ycombinator.com/item?id=43989497

> I tell non-technical people that the site reliability engineer job is about creating automation to do what a system administrator would otherwise do. https://entropicthoughts.com/the-reinforcing-nature-of-toil

CHECKLIST https://www.lastweekinaws.com/blog/aurora-vs-rds-an-engineers-guide-to-choosing-a-database/
* install dbms
* maintenance
* monitoring
* security patches
* make backups

SECURITY
* read-only access https://pgexercises.com/about.html
* `statement_timeout` to prevent long-running queries https://pgexercises.com/about.html https://www.postgresql.org/docs/13/runtime-config-client.html
* clear settings from connection after each statement https://pgexercises.com/about.html https://www.pgbouncer.org/
* _row-level_: limit user to specific rows https://pganalyze.com/blog/postgres-row-level-security-django-python https://news.ycombinator.com/item?id=30700899
* StrongDM records remote access sessions https://softwareengineeringdaily.com/2019/07/23/data-engineering-with-tobias-macey/

TIMEZONES
* client sould specify their timezone before querying https://hakibenita.com/sql-dos-and-donts#be-aware-of-timezones
* relational has problems w/ this https://increment.com/software-architecture/architecture-for-generations/ https://en.wikipedia.org/wiki/Temporal_database#Example https://retool.com/blog/formatting-and-dealing-with-dates-in-sql/

## Docker data mgmt

🗄️ `containers.md` volumes
🧠
* https://chatgpt.com/c/673ce340-ca14-8004-b5ee-320faa5c9866
* https://chatgpt.com/c/6724db6b-b820-8004-b8b4-f73f4e6a3c73
* https://chatgpt.com/c/6724c43a-a9cc-8004-809b-2b53075f84af

EXTERNAL
* run Postgres as normal
* Amazon RDS
> 📍 Regarding RDS, you mentioned: "Adds network dependency and potential latency for remote storage." -> Wouldn't that already be the case given that RDS is a service?

VOLUMES
* just save to volume, which persist even if container destroyed
```sh
docker run -d --name postgres -v postgres_data:/var/lib/postgresql/data postgres
```
* backup at intervals
```sh
docker run --rm -v postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/data.tar.gz /data
```
* volume drivers?
> Can you say more about Docker volume drivers?

---

do you have creds for the m

If you're running an app in Docker, and it includes both a backend and a database [let's say Postgres] that it writes to, what are the options for storing that data? Just store in a Docker volume? Save elsewhere?

Let's say that this Dockerized app is hosted on an EC2 instance. How would that change your above assessment?

## Capp

```txt
At its core, Postgres uses a Write-Ahead Log (WAL) - every change is first written to a sequential log before being applied to the database files. Streaming replication works by sending these WAL records from primary to replica in real-time.
```
```sh
Primary                                      Replica
├── Transaction writes WAL                   |
├── WAL sender process starts                |
├── Sends WAL records ──────────────────────>│── WAL receiver process
├── Gets acknowledgment <───────────────────>│── Applies WAL records
└── Can remove old WAL files                 └── Keeps read-only copy in sync
```
```sh
wal_level = replica
max_wal_senders = 3

host replication replica_user 10.0.0.2/32 md5

# On primary
pg_basebackup -D /var/lib/postgresql/data -U replica_user -h primary_host -p 5432 -P -v -R

primary_conninfo = 'host=primary_host port=5432 user=replica_user password=secret'

# The key insight is that it's fundamentally a log-shipping system - changes are streamed as a log of operations rather than sending actual data pages. This makes it efficient and ensures consistency.
```
```yaml
services:
  primary:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - ./primary:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  replica:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - ./replica:/var/lib/postgresql/data
    ports:
      - "5433:5432"
```

* email
* Google Drive
* repo / csvbase https://csvbase.com/ https://csvbase.com/blog/10
* HuggingFace
* metadata
* git lfs
* warehouse
* minio

Your hardware -> Cloud VM as hot spare
- Run Postgres streaming replication
- Use DNS for failover
- Kamal can handle app deployment to both

Your Hardware (Primary) + Single Cloud VPS (Standby)  
- Postgres streaming replication to VPS
- Kamal for deployment
- Nginx for load balancing
- Simple DNS-based failover
Cost: ~$5-10/month for small VPS

Your hardware + Cloud VMs
- Run Patroni for automated Postgres failover
- Use HAProxy for load balancing
- Deploy with Nomad/Kubernetes for automated app failover

Your Hardware + Single $5 VPS
├── App Layer
│   ├── Kamal deploys to both
│   └── Nginx as reverse proxy
└── Database Layer
    └── Postgres streaming replication
        ├── Primary on your hardware
        └── Replica on VPS

## 🪳 CockroachDB

> CockroachDB enables scaling a database across multiple geographies through being based on Google’s Spanner system, which relies on atomic and GPS clocks for extremely accurate time synchronisation. Commodity hardware, however, doesn’t have such luxuries, so CockroachDB has some clever solutions where reads are retried or delayed to account for clock sync delay with NTP, and nodes also compare clock drift amongst themselves and terminate members if they exceed the maximum offset. Another interesting feature of CockroachDB is how multi-region configurations are used, including table localities, where there are different options depending on the read/write tradeoffs you want to make. https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
* compatible with Postgres wire-protocol https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
* usage https://www.cockroachlabs.com/docs/v24.3/movr
* https://www.openmymind.net/Migrating-To-CockroachDB/
* Rethink https://brandur.org/cloud-databases

ALTERNATIVES
* https://github.com/erikgrinaker/toydb https://github.com/maxpert/marmot
* _rqlite_: SQLite https://github.com/rqlite/rqlite https://philipotoole.com/how-is-rqlite-tested/

## 🌐 PlanetScale

📜 https://planetscale.com/

* based on Youtube's Vitess https://vitess.io/
* new thing based for Postgres https://simonwillison.net/2025/Jul/1/planetscale-for-postgres/
* MySQL compatible
* horizontal scaling through sharding
* eventually consistent
* migrations don't need table lock
* doesn't use functions https://www.youtube.com/watch?v=atwwf0qWpYg [20:00] 🗄️ `sql.md` DML > functions
* great docs https://planetscale.com/blog/btrees-and-database-indexes
* BYO VM https://planetscale.com/blog/faster-interpreters-in-go-catching-up-with-cpp

## 🐯 TigerBeetle

📜 https://github.com/tigerbeetle/tigerbeetle https://docs.tigerbeetle.com/

* Postgres impl https://github.com/pgr0ss/pgledger
* uses VSR 📙 Enberg latency
* https://docs.tigerbeetle.com/coding/system-architecture/
* https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/

# 🔑 INTEGRITY

## backup

> Backups don't matter, only restores matter. https://alexgaynor.net/2024/sep/09/signatures-are-like-backups/
🗄 
* `distributed.md`
* `it.md` backup

TYPES
* _full_: reset to specific backup
* _incremental_: apply changes since last full backup https://posetteconf.com/2025/talks/incremental-backup-in-postgresql/
* _point-in-time (PITR)_: restore to any moment

---

* https://news.ycombinator.com/item?id=44473888
* short answer: dump every hour to S3 https://blog.codepen.io/2014/05/27/013-backups/ 5:00 https://simonwillison.net/about/#subscribe
* copy using rsync https://alexwlchan.net/2025/copying-sqlite-databases/
* backup Postgres to parquet https://www.crunchydata.com/blog/incremental-archival-from-postgres-to-parquet-for-analytics

* Postgres https://github.com/pgsty/pg_exporter
* https://postgres.fm/episodes/snapshots
* with stats, pg_upgrade https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=1fd1bd871012732e3c6c482667d2f2c56f1a9395#transferstatistics

```txt
Database Recovery Methods:

PITR
* Uses transaction logs + backup
* More granular than backup/restore
* Higher storage overhead
* Usually more complex to set up

Core mechanism: The database keeps a transaction log recording every change. To recover to time T, it:
* Restores last backup before T
* Replays transaction log entries up to T
* Discards later entries

This solves several broader problems:
* Recovering from data corruption that wasn't immediately noticed
* Meeting compliance requirements for historical state access
* Testing "what if" scenarios by examining past states
* Migrating data between environments at specific points

The general problem this addresses is maintaining perfect history of state changes in any system. Other solutions in this space:
* Git (source code)
* Event sourcing (application architecture)
* Blockchain (distributed systems)
* Append-only logs (various)
```

* _DR (disaster recovery)_: https://www.lastweekinaws.com/blog/the-cold-hard-truth-about-your-cloud-dr-strategy/?ck_subscriber_id=512830619
* https://drewdevault.com/2019/01/13/Backups-and-redundancy-at-sr.ht.html
* https://github.com/eduardolat/pgbackweb
* hard drive health: 2% annual fail rate https://drewdevault.com/2020/04/22/How-to-store-data-forever.html DriveDX https://binaryfruit.com/drivedx/usb-drive-support Wear_Leveling_Count https://superuser.com/q/1037644 SMART https://en.wikipedia.org/wiki/Self-Monitoring,_Analysis_and_Reporting_Technology https://news.ycombinator.com/item?id=11110902
* https://news.ycombinator.com/item?id=38961463
* _snapshot_: backup whole table
* _date-based_: backup portion of table i.e. acts as an immutable log
* _cold storage_: infrequent reads/writes https://drewdevault.com/2020/04/22/How-to-store-data-forever.html
* _hot storage_: frequent reads/writes https://drewdevault.com/2020/04/22/How-to-store-data-forever.html
* _deduplication_: only touch new data (vs. entire file)
* _durability_: data exists https://news.ycombinator.com/item?id=26428688
* _reliability_: data available
* _redundant_: same data stored multiple places e.g. RAID https://drewdevault.com/2020/04/22/How-to-store-data-forever.html

## replicate

PATTERNS
* _read replica_: scale read workloads
* _reporting replica_: separate analytics from operational load
* _failover replica_: high availability/disaster recovery

TIMING
* _synchronous_: write commits only after replicas confirm receipt
* _semi-synchronous_: waits for at least one replica before committing
* _asynchronous_: primary commits immediately, replicas catch up later

WRITE HANDLING
* _active-passive_: primary handles reads/writes, secondary is standby-only
* _streaming_: 1 server accepts writes, replicas are read-only
* _active-active_: n servers accept writes https://percona.community/blog/2025/06/18/postgresql-active-active-replication-do-you-really-need-it/

DATA TRANSFER METHOD
* _physical_: replicates disk blocks/WAL files byte-for-byte
* _logical_: replicates data changes/operations https://github.com/xataio/pgstream
```conf
# postgresql.conf
wal_level = logical
max_wal_senders = 4
```
```sql
-- PUB SERVER
CREATE PUBLICATION my_publication FOR TABLE orders;  -- pub
SELECT pg_create_logical_replication_slot('my_slot', 'pgoutput');  -- replication slot
SELECT * FROM pg_stat_subscription; SELECT * FROM pg_replication_slots;  -- monitoring
-- SUB SERVER
CREATE TABLE orders ();
CREATE SUBSCRIPTION my_subscription
CONNECTION 'host=pub_host port=5432 dbname=mydb user=repl_user'
PUBLICATION my_publication;
```
* _statement-based_: logical + replicate SQL statements themselves
```sql
INSERT INTO logs VALUES (uuid_generate_v4(), NOW());  -- same statement for pub/sub but breakage bc non-deterministic
```
* _row-based_: logical + replicate actual row changes; used by Postgres
```sql
Insert: id='550e8400-e29b-41d4-a716-446655440000', ts='2025-09-20 10:30:15'  -- sends exact values
```

---

https://www.enterprisedb.com/blog/evolution-logical-replication-postgresql-firsthand-account
migrate https://blog.bytebytego.com/p/how-atlassian-migrated-4-million

* https://www.morling.dev/blog/postgres-replication-slots-confirmed-flush-lsn-vs-restart-lsn/
> Replication slots keep Postgres from discarding WAL (Write-Ahead Log) segments till all consumers have read them. Consumers track progress via log sequence numbers (LSNs), but Postgres exposes multiple LSNs with subtly different meanings. Gunnar Morling explains their differences, as well as why both matter in production.

https://clickhouse.com/blog/sigterm-postgres-mystery
📚
* Enberg latency https://www.manning.com/books/latency
* Kleppmann ch. 5
🗄️
* `dbms.md` Mongo
* `system.md` distributed
* `sql.md` migrations

* _pgdog_: split btw read-replica and write https://news.ycombinator.com/item?id=44099187 https://news.ycombinator.com/item?id=44099187
* sync https://github.com/electric-sql/electric https://electric-sql.com/ https://news.ycombinator.com/item?id=44929478&
* https://github.com/PeerDB-io/peerdb
* postgres https://github.com/xataio/pgstream https://news.ycombinator.com/item?id=42383136
* https://github.com/bruin-data/ingestr
* _replication_: same data on diff nodes 📙 Kleppmann [199] https://news.ycombinator.com/item?id=37066284
* secondaries only accept writes from primary 📙 Bradshaw [236]
* very slow if synchronous https://lethain.com/distributed-systems-vocabulary/
* https://news.ycombinator.com/item?id=44580257
* _lag_: when secondaries fall behind primary 📙 Bradshaw [235]
* will refuse read requests to avoid serving stale data
* _RAID_: form of replication https://www.kalzumeus.com/2010/04/20/building-highly-reliable-websites-for-small-companies/ https://news.ycombinator.com/item?id=28405695 use ZFS/Zed https://drewdevault.com/2020/04/22/How-to-store-data-forever.html
* _ZFS_: https://eradman.com/posts/zfs-quickstart.html
* backup https://github.com/benbjohnson/litestream https://github.com/maxpert/marmot https://news.ycombinator.com/item?id=30883015 SQLite for edge computing https://news.ycombinator.com/item?id=33081159
* using Redis https://andrewbrookins.com/python/scaling-django-with-postgres-read-replicas/
* always use write db vs. read replica to avoid creating 2 records
* http://eradman.com/posts/pubsub-pgoutput.html
* https://news.ycombinator.com/item?id=31341392
* cutover
> There's an ongoing sync job as well, so writes that land on the old database are pushed to the new one, so low risk of data loss.
* replicate Postgres to SQLite on the edge https://github.com/zknill/sqledge
* https://lukeplant.me.uk/blog/posts/keeping-things-in-sync-derive-vs-test/

## shard

---

📚
* Enberg latency https://www.manning.com/books/latency
* Kleppmann ch. 6 https://en.wikipedia.org/wiki/Partition_(database)
🗄️ `dbms.md` Mongo

* https://gadget.dev/blog/sharding-our-core-postgres-database-without-any-downtime
* https://planetscale.com/blog/announcing-neki
* database-per-tenant https://news.ycombinator.com/item?id=43811400
* _partition_: diff data on diff nodes 📙 Kleppmann 199
* pruning https://eradman.com/posts/partition-pruning.html
* why: horizontal scaling, put more frequently accessed data on better hardware or more geographically proximate 📙 Bradshaw [289]
* aka sharding https://news.ycombinator.com/item?id=28776786 📙 Bradshaw [289] Kleppmann [199]
* avoid by scaling vertically as long as you can 📙 Conery imposter 343 https://news.ycombinator.com/item?id=28430852
* howto https://github.blog/2021-09-27-partitioning-githubs-relational-databases-scale/ 📙 Conery imposter 343
* https://stackoverflow.com/questions/20771435/database-sharding-vs-partitioning https://medium.com/@jeeyoungk/how-sharding-works-b4dec46b3f6 https://news.ycombinator.com/item?id=28425379
* _shard_: node in cluster 📙 Bradshaw [290] https://tomlinford.com/posts/robinhood-sharding-to-scale https://pgdog.dev/blog/you-can-make-postgres-scale
* _pgdog_: https://github.com/pgdogdev/pgdog https://news.ycombinator.com/item?id=43484399 https://postgres.fm/episodes/pgdog https://news.ycombinator.com/item?id=44099187

## version control

🗄️ `OLAP.md` Bauplain
🧠 https://chatgpt.com/c/673a8de0-7cd8-8004-9325-7943f380d4d7

* people don't really care about this https://news.ycombinator.com/item?id=22731928
* Jonathan Edwards https://www.hytradboi.com/2025/3b6de0f0-c61c-4e70-9bae-cca5a0e5bb7b-db-usability-as-if
* _DVC_: https://github.com/iterative/dvc https://www.youtube.com/watch?v=ITvSs23lTQE https://realpython.com/python-data-version-control/
* _Dolt_: 🎯 https://github.com/dolthub/dolt https://www.dolthub.com/blog/2025-04-16-doltgres-goes-beta/

# 🟩 MONGO

📚
* Bradshaw guide
* https://www.manning.com/livevideo/talk-python-mongodb-for-developers
📜
* Mongo https://www.mongodb.com/docs/manual https://learn.mongodb.com/
* PyMongo https://pymongo.readthedocs.io/en/stable/tutorial.html
* Beanie (async) https://github.com/BeanieODM/beanie

---

lookups
> workaround for $$ notation just eliminate aliasing?
* dot nota
```js
// dot notation: reference subdocument key 📙 Bradshaw [63] https://www.mongodb.com/docs/manual/core/document/#dot-notation
db.people.find({"name.first": "bob"})

// field path ($) = dot notation for stage's input documents 📙 Bradshaw [173]
{$project: {amount: "$funding_rounds.amount"}}

// variable notation ($$) = reference variable in expression 📙 Bradshaw [174]
{
    $project: {
        rounds: {$filter: {
            input: "$funding_rounds",
            as: "round",  // variable definition
            cond: {$gte: ["$$round.raised_amount", "$1M"]}  // reference
        }}
    }
}
```

queries
* _query document_: arg to `find()`, `aggregate()` 📙 Bradshaw [53]
* _cursor_: return from aggregation
* iterator, also a connection object 📙 Bradshaw [66]
* lazy evaluation i.e. cursor doesn't query db until all operators evaluated 📙 Bradshaw [66]
* only fetches 100 results or 4 MB on evaluation
* `hasNext()`: bool on whether next el to fetch 📙 Bradshaw [66]
* `next()`: fetches next el
* _immortal_: cursor that you explicitly need to iterate fully through or kill 📙 Bradshaw [71]
* _projection_: specify keys to return per document i.e. select 📙 Bradshaw [196]
* via dict keys in PyMongo
* do last bc expensive operation and want to run on as few documents as possible 📙 Bradshaw [166]
* _mongoexport_: output result set to file https://stackoverflow.com/a/47450934
> have code for this from a UM ticket

semantics
* _field_: key
* _normal collection_: size dynamic 📙 Bradshaw [151]
* _capped collection_: size static 📙 Bradshaw [151]
* _natural order_: order of documents on disk https://www.mongodb.com/docs/v4.4/reference/method/db.collection.findOne/

monitoring
* slow queries
> Anyone know if we have the equivalent of a mongo slow query log, or some other way to identify slow queries?
> usually you can spot slow mongo in API traces that have a long span for pymongo.get_socket. but yeah, it doesn't tell you which query. so if there are a bunch that it could be, I've had to run an explain on each one. mongodb has slow query logs though.
* `db.currentOp()` connection id, operation id, seconds running 📙 Bradshaw [371]
* stats: `db.stats()` and `db.col.stats()`
* some long-running ops are not normal queries but for replication 📙 Bradshaw [375]
* profiler will slow down db, can set it to only observe queries that take long than 100ms 📙 Bradshaw [376,378]
* _acknowledged write_: waits until previous write completed vs. just sitting in an os buffer 📙 Bradshaw [376]
* _phantom writes_: write waiting in the os buffer after you've already stopped client from sending further writes 📙 Bradshaw [376]

za
* implementation http://aosabook.org/en/nosql.html
* certification https://university.mongodb.com/certification/developer/about exam https://university.mongodb.com/certification/exam-prep
* indexes 📙 Bradshaw [384] `db.col.getIndexes()`
* _mongod_: server daemon; port 27107 📙 Bradshaw [227,290]
* _MongoEngine_: ODM i.e. doesn't return dicts like PyMongo https://stackoverflow.com/a/41323384
* _Mongo tools_: https://github.com/mongodb/homebrew-brew `brew install mongodb-database-tools`
* _Beanie_: ODM https://talkpython.fm/episodes/show/349/meet-beanie-a-mongodb-odm-pydantic
* _Atlas_: managed Mongo
* _Charts_: Atlas + visualization

replication 🗄 `system.md` data
* _replica set_: cluster 📙 Bradshaw [227]
* changing normal mongod server to replica set involves downtime so just config as 1-server set from start 📙 Bradshaw [231]
* connection config comes from primary 📙 Bradshaw [230]
* 1 primary (writes) n secondaries (replication)
* if primary unavailable secondaries elect new primary 📙 Bradshaw [227,235,243,244]
* secondaries become primary due to priority + election algorithm 📙 Bradshaw [244]
* need majority to elect primary bc don't want two primary in event of network partition 📙 Bradshaw [241]
* _data node_: node that holds data 📙 Bradshaw [247]
* _arbiter_: secondary holding no data whose only point is to participate in elections for 2-member replica sets 📙 Bradshaw [246]
* generally shouldn't be used [247]
* _passive_: secondaries w/ priority of 0 i.e. can never become primary 📙 Bradshaw [244]
* _hidden member_: secondary that doesn't get requests routed to it and won't get replicated to often 📙 Bradshaw [245]
* for low-powered servers

partition 🗄 `system.md` data
* _mongos_: routing process in front of sharding cluster 📙 Bradshaw [290,293]
* can shard on single machine 📙 Bradshaw [291]
* _shard key_: field used to chuck data e.g. if `username` then alice-candace, david-fred, etc. 📙 Bradshaw [294]
* Postgres https://github.com/ankane/pgslice

## aggregation

📜
* https://docs.mongodb.com/manual/aggregation/
* https://www.practical-mongodb-aggregations.com

grouping https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/group/
* output document per group by `_id` 📙 Bradshaw [189] https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/group/#group-title-by-author
```js
// regular syntax
$group : { 
    _id : "$author",  // group
    books: { $push: "$title" }  // accumulator
}

// label syntax; neither Bradshaw [193] nor the docs explain https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/group/#optimization-to-return-the-first-document-of-each-group
$group : { 
    _id : { author: "$author"},
    books: { $push: "$title" }
}
```
* _accumulator_: mostly SQL aggregates (min/mix/avg) + misc functionality (push) https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/group/#std-label-accumulators-group
* can run w/out grouping e.g. count https://www.mongodb.com/docs/upcoming/reference/operator/aggregation/group/#count-the-number-of-documents-in-a-collection
* _push_: add el to list as obj added to group 📙 Bradshaw [194]
* only works in group stage 📙 Bradshaw [196]
* _addToSet_: push + no dupes 📙 Bradshaw [186]

operations
* array expressions: filter, slice, `$arrayElemAt` 📙 Bradshaw [181,184,186]
* _filter_: comparison operator for projection stage of aggregation 📙 Bradshaw [181]
```js
$project: {
    items: {
        $filter: {
            input: "$items",
            as: "item",
            cond: { $gte: [ "$$item.price", 100 ] }
        }
    }
}
db.sales.aggregate([
   {
   }
])
```
* find doesn't require projection for this so idky aggregation does
* _match_: predicate; earlier the better 📙 Bradshaw [165,180]
* _unwind_: create output document for each el in array field 📙 Bradshaw [174]
```diff
- {
-    k: v,
-    k: [1,2]
- }
+ {
+    k: v,
+    k: [1]
+ }
+ {
+    k: v,
+    k: [2]
+ }
```
* _lookup_: left outer join https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/
```js
db.orders.aggregate([             // FROM orders
    {
        $lookup: {
            from: "inventory",    // JOIN inventory
            localField: "item",   // ON orders.item
            foreignField: "sku",  // = inventory.sku
            as: "inventory_docs"  // stdout alias
        }
    }
])
```

semantics
https://www.singer.io/ pipeline, taps
* _aggregation_: operation on a pipeline 📙 Bradshaw [166]
* _pipeline_: array of stages 📙 Bradshaw [166]
* same idea as UNIX pipes 📙 Bradshaw [162]
* introduced w/ version 3.2 📙 Bradshaw [5]
* preceded by MapReduce https://www.practical-mongodb-aggregations.com/intro/history.html
* no SSoT for how to do things btw `find()` and `aggregate()`
* _stage_: input document + operator = output document 📙 Bradshaw [162,166]
* can have multiple of the same type 📙 Bradshaw [180]
* each stage takes input from previous stage 📙 Bradshaw [161]
* input and output of each stage also a document 📙 Bradshaw [161]

## find

📜 Mongo https://www.mongodb.com/docs/manual/crud/

---

* key exists: `list(db.col.find({"ur_key": {"$exists": False}}))`
* syntax: `db.col.find(query)`
* get collections `sorted(db.collection_names())`

basic
* can't refer to another key in document e.g. `find({"balance": "this.profit - this.loss})` 📙 Bradshaw [55]
* null 📙 Bradshaw [57]
* regex 📙 Bradshaw [58]
```sh
# SELECT * FROM TAB
db.col.find()

# SELECT * FROM TAB LIMIT 1
db.col.findOne()  # for n, returns 1 according to natural order https://www.mongodb.com/docs/v4.4/reference/method/db.collection.findOne/
db.col.find_one() # same as mongosh? https://github.com/mongodb/mongo-python-driver/blob/6e99bf451503825577213ef148ec6b519a41257b/pymongo/collection.py#L1388

# SELECT * FROM TAB LIMIT N
db.col.find().limit(n)  # for pagination 📙 Bradshaw [69] can also use slice() or skip() 📙 Bradshaw [60,67]

# COUNT https://stackoverflow.com/a/4415593
db.col.find().count()

# SORT
db.col.find().sort({age: 1})  # asc
db.col.find().sort({age: -1}) # desc
```

predicates
* can use `$where` queries but shouldn't bc slower, use `$expr` instead 📙 Bradshaw [65]
```sh
# SELECT * FROM TAB WHERE COL = VAL 📙 Bradshaw [54]
{f:v}
# NESTED
{f1.f2: v}

# MEMBERSHIP 📙 Bradshaw [56]
{f: {$in: [a, b]}}
# EXACT MATCH ON N 📙 Bradshaw [59]
{f: { $all: [a, b]}}

# LOGICAL OPERATORS 
{f1: v, f2: v}
# `[]` for empty list https://stackoverflow.com/a/25142571
{$and: [{f1: {$eq: null}}, {f2: {$ne: null}}]}  # 📙 Bradshaw [56] https://stackoverflow.com/a/69314784

# EQUALITY
db.col.find({likes: 0})
# INEQUALITY
db.col.find({likes: {$ne: 1}})

# COMPARISON 📙 Bradshaw [55]
db.post.find({likes: {$gt: 1}})
```

* find all active artists using big_corp as pg
```js
// feed artist IDs into Mongo
db.subs.findOne({"pg": "big_corp", "status": "active", "artist_id": {$in: [list_of_artist_ids]}})
```

## shell

https://github.com/kopecmaciej/vi-mongo?ref=terminaltrove
🗄 utils/GUIs

workflows
* _iPython_: write in driver language (PyMongo), run in REPL
* ✅ good at reuse
* ❌ slow for sketching
* need for work bc can only access some collections via corpus obj
* _RoboMongo_: https://github.com/Studio3T/robomongo https://www.practical-mongodb-aggregations.com/intro/getting-started.html
* _Compass_: write in GUI query editor, run in GUI https://www.mongodb.com/products/compass
* ❌ doesn't work with server versions before 3.6
* ✅ good at sketching simple queries
* ❌ bad at sketching complex queries bc bad editing (no Vim or syntax highlighting)
* ❌ bad at reuse
* ✅ good at aggregations https://www.practical-mongodb-aggregations.com/intro/getting-started.html#mongodb-compass-gui
* _DbGate_: queryless via GUI, run in GUI
* ✅ good at sketching
* ❌ bad at reuse
* _mongosh_: write in text editor, run in terminal
* ❌ slow at sketching bc vim mode in readline never seems to work
* ✅ text editor = Vim, syntax highlighting but 1) slow 2) ephemeral
* ✅ text editor = Vim, syntax highlighting but 1) slow 2) ephemeral

REPL
* mongorc
```js
function foo(value){return [{$match: {"key": `${value}`}}]}
db.col.aggregate(foo(arg))
```
* `edit`: for writing more complex queries/aggregations https://stackoverflow.com/a/28074078
* not actually a good solution bc will fail silently if parsing error
```js
// edit q
{
    $and: [
        { "id": "foo" },
        { "other_col_id": { $ne: "bar"} } 
    ]
},
// edit p
{"thing1": 1, "thing2":1, "_id":0}
// run
db.col.find(q, p)
```

MONGO CLI
* warning https://docs.mongodb.com/v4.4/mongo/#start-the-mongo-shell-and-connect-to-mongodb
* install as standalone https://github.com/mongodb/homebrew-brew#installing-only-the-shell-or-the-database-tools
```sh
$ brew tap mongodb/brew
$ brew install mongodb-community-shell
```
* prompt: display host/user https://www.mongodb.com/docs/manual/tutorial/configure-mongo-shell/#customize-prompt-to-display-database-and-hostname https://stackoverflow.com/a/21417240

MONGOSH CLI https://docs.mongodb.com/mongodb-shell 
* methods https://docs.mongodb.com/mongodb-shell/reference/methods/
* config: if you're connecting to remote, mongo will still use config on local https://docs.mongodb.com/mongodb-shell/run-commands/#.mongoshrc.js-file https://stackoverflow.com/a/11397470
* enhanced https://github.com/TylerBrock/mongo-hacker
```sh
# shell history https://docs.mongodb.com/mongodb-shell/logs/#view-mdb-shell-command-history
~/.mongodb/mongosh/.mongosh_repl_history
# shell logs https://docs.mongodb.com/mongodb-shell/logs/#view-the-log-for-the-session
~/.mongodb/mongosh/
# clear console
cls

# connect https://docs.mongodb.com/mongodb-shell/connect/
mongo -u user -p pw 127.0.0.1:6017/db
mongosh --port 27017

# view connection info https://docs.mongodb.com/mongodb-shell/connect/#verify-current-connection
db.getMongo()          # Mongo shell
db.collection_names()  # PyMongo REPL https://stackoverflow.com/a/9805506

db  # view current db
show dbs  # view all dbs
use <db>  # switch/create db
show collections  # view collections
```

# 🐘 POSTGRES

> There are extensions for almost everything you could want - AGE enables graph data structures and the user of the Cypher query language, TimescaleDB enables time-series workloads, Hydra Columnar provides an alternate columnar storage engine https://matt.blwt.io/post/building-a-postgresql-extension-line-by-line/

WIRE PROTOCOL https://news.ycombinator.com/item?id=43693326 🗄️ `OLAP.md` DuckDB
> we’re seeing even more non-Postgres services rely on the Postgres wire protocol as a general-purpose Layer 7 protocol to provide client compatibility https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
> We embed DuckDB as the query engine for in-memory analytics that work for complex queries. With efficient columnar storage and vectorized execution, we’re aiming for faster results without heavy infra. BemiDB communicates over the Postgres wire protocol to make all querying Postgres-compatible.

---

ADMIN
* https://eradman.com/posts/pg-admin-queries.html
* https://boringsql.com/posts/postgresql-predefined-roles/

* kernels https://www.postgresql.org/about/news/pigsty-36-the-meta-distribution-for-postgresql-3111/
* adapter to use SQLite as backend https://github.com/erans/pgsqlite
* listen/notify https://news.ycombinator.com/item?id=44490510
* ubiquity https://www.youtube.com/watch?v=3JW732GrMdg
* cancel queries https://pert5432.com/post/postgres-query-cancellation
* binary mgmt? https://github.com/theory/pgenv
* terabyte scale https://simonwillison.net/2025/Mar/14/merklemap-runs-a-16tb-postgresql/
* AI https://simonwillison.net/2025/Mar/13/xata-agent/

hosted Neon, pg_cron https://www.youtube.com/watch?v=3JW732GrMdg https://news.ycombinator.com/item?id=43899016

weird bits https://www.hytradboi.com/2025/b479d9ff-3dd9-4548-940d-24698e7cff71-learning-about-the-odd-bits-of-sql-by-reading-the-postgresql-docs

https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb
🏔️ https://github.com/Olshansk/postgres_for_everything
📚
* Magda just use postgres https://www.manning.com/books/just-use-postgres
* Suzuki postgres internals https://www.interdb.jp/pg/ https://djangotv.com/videos/djangocon-us/2024/a-guided-tour-through-postgres-internals-with-elizabeth-garrett-christensen/
🔗 https://challahscript.com/what_i_wish_someone_told_me_about_postgres
📜
* general https://www.postgresql.org/docs/current/index.html
* guide http://postgresguide.com/
* wiki https://wiki.postgresql.org/wiki/Main_Page

HOW TO https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb https://news.ycombinator.com/item?id=39273954
* AI https://github.com/xataio/agent
* BYO with Zig https://github.com/xataio/pgzx
* analytics https://news.ycombinator.com/item?id=43270712
* monitor / metrics https://github.com/CrunchyData/pgmonitor-extension
* duckdb extension https://motherduck.com/blog/pg_duckdb-postgresql-extension-for-duckdb-motherduck/ https://github.com/duckdb/pg_duckdb
* copy btw tables https://ongres.com/blog/fastest_way_copy_data_between_postgres_tables/
* perf, memory https://news.ycombinator.com/item?id=40642803 https://github.com/nexsol-technologies/pgassistant
* generate `create table` from existing table https://github.com/lacanoid/pgddl
* Elasticsearch https://github.com/paradedb/paradedb https://github.com/pgroonga/pgroonga
* serverless https://neon.tech/ https://news.ycombinator.com/item?id=31536827
* embedded for testing https://github.com/wey-gu/py-pglite https://github.com/electric-sql/pglite https://news.ycombinator.com/item?id=39960537 https://news.ycombinator.com/item?id=44196945
* sharding https://github.com/postgresml/pgcat
* Snowflake, DuckDB, Clickhouse https://github.com/scottpersinger/pgwarehouse
* result set to CSV https://stackoverflow.com/a/1517692
* high availability https://github.com/zalando/patroni
* upgrade: pg_upgrade https://about.gitlab.com/blog/2020/09/11/gitlab-pg-upgrade/ https://news.ycombinator.com/item?id=42867657 https://why-upgrade.depesz.com/show
* delete data from table: `DELETE FROM <tab>` https://www.postgresql.org/docs/11/dml-delete.html
* drop all tables: `DROP SCHEMA <schema> CASCADE`
* get date from timestamp: `SELECT date(startime) FROM bookings` https://stackoverflow.com/a/6133147
* random/seed data https://www.postgresonline.com/journal/index.php?/archives/419-PG-17-new-random-functions.html#newrandom
* regex https://www.caktusgroup.com/blog/2025/03/19/how-use-regexp_matches-and-regexp_match-postgresql/

SEMANTICS
* _cluster_: server instance managing n databases https://www.postgresql.org/docs/12/tutorial-concepts.html https://www.crunchydata.com/blog/postgres-databases-and-schemas
* _foreign data wrapper_: access data from another data store e.g. document store for a relational db https://github.com/pgspider/sqlite_fdw
* _system columns_: ctid, xmin, xmax https://www.youtube.com/watch?v=AveRgUrC7FM

UTILS
* lint https://github.com/sbdchd/squawk https://steve.dignam.xyz/2025/06/20/interesting-bits-of-postgres-grammar/
* generate harmful workloads https://github.com/lesovsky/noisia
* generate test data https://news.ycombinator.com/item?id=26564168 https://hakibenita.com/sql-for-data-analysis#generating-data
* tmp db for testing: https://eradman.com/posts/schema-definition.html https://github.com/eradman/ephemeralpg/ https://stackoverflow.com/questions/14314026/embedded-postgresql-for-java-junit-tests 🗄 `testing.md`
* show view's underlying query `select pg_get_viewdef('my_vw')` https://stackoverflow.com/a/25738887/6813490

---

> And before you think being open-source insulates you from a company going under, few DBMS projects continue on and thrive when their founding for-profit company fails. PostgreSQL sort of counts even though the open-source version we have today is based on the UC Berkeley source code and not the commercial Illustra version (which was acquired by Informix in 1996). https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html

misc
* arrays https://www.openmymind.net/Introduction-To-PostgreSQL-Arrays/
* fuzzy match https://news.ycombinator.com/item?id=26236772
* local dev https://jamey.thesharps.us/2019/05/29/per-project-postgres/
* chaos https://github.com/lesovsky/noisia
* config https://news.ycombinator.com/item?id=25024224
* cron https://github.com/citusdata/pg_cron
* debug https://iamsafts.com/posts/postgres-gin-performance/
* functions https://blog.jonudell.net/2021/08/05/the-tao-of-unicode-sparklines/
* gotchas https://wiki.postgresql.org/wiki/Don%27t_Do_This https://news.ycombinator.com/item?id=26709019
* internals http://www.interdb.jp/pg/ https://postgrespro.com/blog/pgsql/5969985 https://lwn.net/SubscriberLink/934940/3abb2d4086680b78/
* typing https://www.postgresql.org/docs/current/datatype.html 🗄 `sql.md` typing
* stored procedures https://www.postgresql.org/docs/current/xplang.html https://dev.nextthought.com/blog/2018/09/getting-started-with-pgsql-plpythonu.html 

* _anonymize_: https://postgresql-anonymizer.readthedocs.io/en/latest/
* _audit_: https://github.com/pgaudit/pgaudit https://supabase.com/blog/2022/03/08/audit https://news.ycombinator.com/item?id=36004925&utm_term=comment https://news.ycombinator.com/item?id=30615470 https://blog.sequin.io/all-the-ways-to-capture-changes-in-postgres/
* _backup_: https://www.crunchydata.com/blog/introduction-to-postgres-backups https://github.com/2ndquadrant-it/barman/ https://github.com/ankane/pgsync https://github.com/postgrespro/pg_probackup https://pgbackrest.org/index.html https://github.com/aiven/pghoard https://github.com/orgrim/pg_back https://www.youtube.com/watch?v=kbCytSYPh0E https://github.com/EnterpriseDB/barman https://github.com/pgmoneta/pgmoneta
* _benchmarking_: https://github.com/ankane/pghero https://blog.codeship.com/tuning-postgresql-with-pgbench/ https://softwareengineeringdaily.com/2022/09/22/automatic-database-tuning/
> Benchmarking is a dark art of deceiving yourself with highly precise numbers. And benchmarketing datastores is even more fraught. Every single flipping database benchmark I've ever seen has been covered in a layer of asterisks and qualifications, and the comments on HN are full of "if you'd just set this flag when compiling it, you'd get 3% more speed out of reads, and the fact that the people running this didn't do this is proof that they were paid off and that they actively sell shady NFT scams of deranged yacht rock Harambe memes. https://wafris.org/blog/rearchitecting-for-sqlite
* ERD: https://pgmodeler.io/ https://github.com/akarki15/dbdot
* _extensions_: https://news.ycombinator.com/item?id=23821112 https://github.com/zombodb/pgx https://tech.marksblogg.com/postgresql-extension-rust.html distributed/multitentant https://github.com/citusdata/citus https://www.crunchydata.com/blog/citus-the-misunderstood-postgres-extension ydb https://news.ycombinator.com/item?id=31081272 https://tech.marksblogg.com/postgresql-extension-rust.html https://github.com/tcdi/pgx
> For these types of applications, Citus distributes the data for each tenant into a shard. Citus handles the splitting of data by creating placement groups that know they are grouped together, and placing the data within shards on specific nodes. A physical node may contain multiple shards. Let me restate that to understand Citus at a high-level https://www.crunchydata.com/blog/citus-the-misunderstood-postgres-extension
* build in Rust https://github.com/pgcentralfoundation/pgrx
* _GUI_: pgadmin https://retool.com/blog/best-postgresql-guis-in-2020/
* _GraphQL_: https://github.com/graphile/postgraphile
* _import_: pgloader https://www.twilio.com/blog/sqlite-postgresql-complicated https://github.com/dimitri/pgloader https://www.youtube.com/watch?v=DA1Trq51JZs https://www.youtube.com/watch?v=yDtgk_OLHUc http://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/ https://stackoverflow.com/questions/2987433/how-to-import-csv-file-data-into-a-postgresql-table/2987451#2987451 https://mattsegal.dev/restore-django-local-database.html https://bigmachine.io/all/importing-a-csv-into-postgresql-like-a-pro/
* _logs_: https://github.com/darold/pgbadger
* _monitoring_: https://minervadb.xyz/postgresql-dba-daily-checklist/ https://pgstats.dev/ https://info.crunchydata.com/blog/postgresql-monitoring-for-application-developers-dba-stats https://klotzandrew.com/blog/quickly-debugging-postgres-problems https://github.com/lesovsky/pgcenter Vivid Cortex https://github.com/lob/pg_insights https://github.com/cybertec-postgresql/pgwatch2 https://pganalyze.com/ https://github.com/dalibo/temboard
* _queries_: https://news.ycombinator.com/item?id=22432254 explain http://www.helenanderson.co.nz/sql-query-tweaks/ `pg_stat_statements` https://pgdash.io/blog/postgres-features.html https://github.com/mgartner/pg_flame
* _search_: https://czep.net/17/full-text-search.html https://www.imagescape.com/blog/2020/03/11/website-search-using-django-and-postgresql-trigrams 🗄 `algos.md` FTS pg_search https://news.ycombinator.com/item?id=43627646
* _scheduling_: https://github.com/cybertec-postgresql/pg_timetable

## auth

* start in read-only mode https://kmoppel.github.io/2025-03-27-til-starting-in-read-only-the-easy-way/
* _role_: Postgres equivalent of a user, necessary to connect 📙 Conery [4.5] https://www.postgresql.org/docs/8.1/user-manag.html
* are complex https://news.ycombinator.com/item?id=40186752
* _role creation_: PG will create role/db matching Linux user that installed PG; sometimes this doesn't happen w/ Homebrew 📙 Conery 4.4 0:15
* _list roles_: `\du`
* _connection string_: `postgresql://user:pass@host:port/db` https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#docker https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
* _pure authentication_: Linux user matching PG role can log into that role 📙 Conery 4.3 2:30
* login
```sh
# same syntax for both pgcli and psql
# defaults to user/role and db matching Linux user name https://www.postgresql.org/docs/12/tutorial-accessdb.html
psql -d <db> -U <user>
$ whoami  # alice
$ pgcli  # role (alice) db (alice)
```

---

install https://superuser.com/a/1501253 https://neil.computer/notes/how-to-install-postgresql-in-a-custom-directory/
```sh
# as root
$ apt-get install postgresql postgresql-client postgresql-contrib

# shows that psql and CLI work, both should fail w/ error that Postgres doesn't have user named root
$ psql
$ createdb

# only role in db in `postgres`
# installing PG also creates os user of `postgres`
# idky switching to `postgres` also switches directory to `/root`
$ su postgres
$ createdb scifi
$ psql scifi
```

* macos installation and start https://www.postgresql.org/docs/12/installation-platform-notes.html#INSTALLATION-NOTES-MACOS https://postgresapp.com/ https://stackoverflow.com/a/18832331 🗄 `brew/postgres*.log`
```sh
# start manually
pg_ctl -D /usr/local/var/postgres start
# start on os startup w/ Homebrew
brew services start postgresql
```

* Docker image: roles only set during initializatio https://hub.docker.com/_/postgres if you update auth credentials `docker-compose down -v` might not be enough, may need to rm image as well https://stackoverflow.com/q/53820456 https://github.com/docker-library/postgres/issues/537
```sh
# debug cmd
docker-compose exec <service> env # env var ingested?
docker-compose exec <service> psql -U <user> # can you log in?
```
```yaml
services:
  db:
    image: "postgres:11"  # which image to use; unlike 'web', we're not building this one ourselves
    command: ["postgres", "-c", "log_statement=all", "-c", "log_destination=stderr"]  # logs https://stackoverflow.com/a/59313245
    environment:
      - POSTGRES_HOST  # defaults to service name i.e. 'db' https://www.youtube.com/watch?v=A9bA5HpOk30 6:50 can set manually as well https://stackoverflow.com/a/52543774
      - POSTGRES_DB=zjv_db
      - POSTGRES_USER=zjv_user  # creates role https://stackoverflow.com/q/46669759
      - POSTGRES_PASSWORD=zjv_pw  # cannot be empty or undefined
      - POSTGRES_HOST_AUTH_METHOD=trust  # allow connections w/out password https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
    volumes:  # create dir in WORKDIR (pg_data) and map to where PG stores data https://www.youtube.com/watch?v=A9bA5HpOk30 2:30
      - pg_data:/var/lib/postgresql/data/  # or does this create file in CWD on local machine? https://www.youtube.com/watch?v=A9bA5HpOk30 9:25

volumes:  # yj
  pg_data:
```

* app tier ingestion of env
```conf
# Flask
DB_USER=zjv_user
DB_PW=zjv_pw
DB_NAME=zjv_db
```
```python
# Django https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'PORT': 5432,  # docker images defaults to 5432 so we don't need to specify in docker-compose.yml
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}
# Flask
user = os.getenv("DB_USER")
pw = os.getenv("DB_PW")
name = os.getenv("DB_NAME")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{user}:{pw}@db:5432/{name}"
```

## CLI

CMD
* Postgres specific cmd: `\h`
* connection URL: `postgresql://user:pass@host:5432/db`

---

https://github.com/zachvalenta/dotfiles/blob/7f843714b3c3d6eb531dfb292e91214c051ef82e/db/.sqliterc

* SQL/psql tips https://psql-tips.org/psql_tips_143.html https://news.ycombinator.com/item?id=34909670
> psql more specific about semicolons? `DELETE FROM $TABLE` works in pgcli but need semicolon in psql

* _change output_: `\pset`
* _set var_: `\set`

psql https://tomcam.github.io/postgres/ https://mydbanotebook.org/psql_tips_all.html
* conf: `.psqlrc` https://www.digitalocean.com/community/tutorials/how-to-customize-the-postgresql-prompt-with-psqlrc-on-ubuntu-14-04 https://robots.thoughtbot.com/improving-the-command-line-postgres-experience https://robots.thoughtbot.com/an-explained-psqlrc
* connect: `-d <db> -U <user> -h <host> -p <port>`; defaults (user=root, host=localhost, port=5432) https://startcodingnow.com/psql-in-docker-compose/
* connect after login: `\c <db>`
* connection info: `\conninfo`
* https://stackoverflow.com/questions/41591386/postgresql-column-does-not-exist-but-it-actually-does

CLI util (psql, postgres, pg_dump, createdb/dropdb) https://gist.github.com/apolloclark/ea5466d5929e63043dcf
* _postgresql-client_: CLI for backups
* create: `createdb <db>` (if 0 doesn't write to stdout) https://www.postgresql.org/docs/12/tutorial-createdb.html comes w/ PG installation https://www.postgresql.org/docs/12/tutorial-createdb.html
* rm: `dropdb <db>`
* dump: `pg_dump <db> > <file>` https://www.postgresql.org/docs/11/backup-dump.html
* load: `psql -f <file>`; https://www.postgresql.org/docs/11/backup-dump.html#BACKUP-DUMP-RESTORE might need to create db beforehand (idk if way to dump such that db automatically created on load, also don't know if safer to use `-d <db>` to ensure loaded to correct db but `verbos` db worked without it) https://raw.githubusercontent.com/ghidinelli/fred-jehle-spanish-verbs/master/jehle_verb_postgresql.sql
* start/status: `pg_ctl`
* version: `postgres -V`

## extensions

* trusted https://www.cybertec-postgresql.com/en/postgresql-trusted-extensions-for-beginners/
* registry https://pgt.dev/
BYO https://matt.blwt.io/post/building-a-postgresql-extension-line-by-line/
https://www.postgresql.org/about/news/announce-pig-the-postgres-extension-wizard-2988/

## internals

* bring your own storage format https://github.com/orioledb/orioledb https://www.orioledb.com/blog/better-table-access-methods https://misachi.github.io/
* version 18 much smaller in Docker https://ardentperf.com/2025/04/07/waiting-for-postgres-18-docker-containers-34-smaller/
* `synchronous_commit`: governs whether a transaction waits for data to be physically written to disk before returning a commit success status to the client. https://postgres.fm/episodes/synchronous_commit

## pgcli

```sh
# install https://github.com/dbcli/pgcli/issues/1413#issuecomment-2028781741
$ pipx install pgcli
$ pipx inject pgcli psycopg_binary
# connect
pgcli postgresql://$USER:$PW@$HOST:$PORT/$DB
# dump table to CSV
\COPY (SELECT * FROM $TBL LIMIT 100) TO '$TBL.csv' WITH CSV HEADER;
# as snippet
[alias_dsv]
$TBL = "\COPY (SELECT * FROM {0} LIMIT 100) TO '{0}.csv' WITH CSV HEADER"
\d $TBL product_template
```

## psycopg

* _driver_: lib for (db) connection https://stackoverflow.com/a/8588766 
* _psycopg_: Python driver for Posgres
* define driver https://news.ycombinator.com/item?id=42984457
* impl https://www.varrazzo.com/blog/2020/03/06/thinking-psycopg3/
* _psycopg2_: uninstallable w/ Poetry even w/ Brew install of Postgres https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
* _psycopg2-binary_: installable w/ Poetry, problem with pipenv https://github.com/pypa/pipenv/issues/4073
* reasons for split https://github.com/psycopg/psycopg2/issues/674
* seems like people just use psycopg2-binary instead of psycopg2 http://www.dark-hamster.com/programming/how-to-solve-error-on-installing-psycopg2-using-pip-by-using-psycopg2-binary-instead/ https://gitlab.com/mailman/mailman/commit/3b2a3e199601961b8b195d4a7713e170ce6f9935
* erred out w/ `python:3-alpine` even with installing `psycopg2-binary` as separate dep https://stackoverflow.com/q/60461406
```log
Collecting psycopg2-binary==2.8.5
  Downloading psycopg2-binary-2.8.5.tar.gz (381 kB)
    Error: pg_config executable not found.
    pg_config is required to build psycopg2 from source.
    If you prefer to avoid building psycopg2 from source, please install the PyPI
    'psycopg2-binary' package instead.
```
* worked with new image and installing psycopg2-binary as separate dep in Dockerfile https://github.com/psycopg/psycopg2/issues/684#issuecomment-538423955
```diff
- FROM python:3-alpine
+ FROM python:3.6-slim
+ RUN pip install psycopg2-binary
```
* SQLAlchemy seems to have psycopg as sub dep, but still need to install as standalone https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
```ini
[[package]]
name = "sqlalchemy"

[package.extras]
postgresql = ["psycopg2"]
postgresql_psycopg2binary = ["psycopg2-binary"]
```
```log
web_1  | 172.18.0.1 - - [25/Jun/2020 18:54:01] "GET /healthcheck HTTP/1.1" 200 -
web_1  | [2020-06-25 18:54:13,597] ERROR in app: Exception on /get-things [GET]
web_1  | Traceback (most recent call last):
web_1  |   File "/usr/local/lib/python3.8/site-packages/sqlalchemy/util/_collections.py", line 1020, in __call__
web_1  | During handling of the above exception, another exception occurred:
web_1  | Traceback (most recent call last):
web_1  |     import psycopg2
web_1  | ModuleNotFoundError: No module named 'psycopg2'
```

# 🟦 SQLITE

🗄️ CockroachDB > rqlite
📜 https://sqlite.org/docs.html
🛠 https://github.com/simonw/sqlite-utils
🔗 https://tech.marksblogg.com/sqlite3-tutorial-and-guide.html

USAGE
* atuin
* iPython
* Neovim
* prod! https://simonw.substack.com/p/video-scraping-using-google-gemini
* WhatsApp https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
* Basecamp
> SQLite has also had a small resurgence thanks to Ruby on Rails 8.0 - 37signals has gone all in on SQLite, building a bunch of Rails modules like Solid Queue and configuring Rails to manipulate multiple SQLite databases via database.yml for this purpose.
* social media
> Bluesky uses SQLite for the Personal Data Servers - every user has their own SQLite database. https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/

---

* functions https://blog.julik.nl/2025/01/supercharge-sqlite-with-ruby-functions
* https://blog.julik.nl/2025/01/maximum-speed-sqlite-inserts
> Beyond that, we’re starting to see more creative uses of SQLite rather than “just” a local ACID-compliant database. With the advent of tools like Litestream enabling streaming backups and LiteFS to provide distributed access, we can devise more interesting topologies. Extensions like CR-SQLite allow the use of CRDTs to avoid needing conflict resolution when merging changesets, as used in Corrosion. https://matt.blwt.io/post/7-databases-in-7-weeks-for-2025/
* durable object https://simonwillison.net/2024/Oct/13/zero-latency-sqlite-storage-in-every-durable-object/

ZA
* vector https://github.com/asg017/sqlite-vec https://blog.vectorchord.ai/vector-search-at-10000-qps-in-postgresql-with-vectorchord embeddings https://www.cybertec-postgresql.com/en/pgai-importing-wikipedia-into-postgresql/
* https://news.ycombinator.com/item?id=40637303
* single-tenant i.e each user gets own db https://news.ycombinator.com/item?id=38171322
* transactions for perf https://news.ycombinator.com/item?id=36583317
* _APSW_: alternative to Python's sqlite3 https://github.com/litements/s3sqlite
* db file extension incl. `.db` and `.sqlite` https://www.visidata.org/ https://sqlite.org/fileformat.html
* can do blob https://stackoverflow.com/q/29008721/6813490 https://www.youtube.com/watch?v=TLgVEBuQURA
* backups https://github.com/benbjohnson/litestream https://news.ycombinator.com/item?id=34517474 https://github.com/maxpert/marmot https://litestream.io/alternatives/cron/ https://news.ycombinator.com/item?id=31152490 https://news.ycombinator.com/item?id=31318708

HOWTO
* diff changes / changelog https://news.ycombinator.com/item?id=38110286&utm_term=comment
* tuning https://news.ycombinator.com/item?id=35547819 https://news.ycombinator.com/item?id=39955288
* config (journal, wal, timeout) https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html https://avi.im/blag/2021/fast-sqlite-inserts/
* migrations: https://news.ycombinator.com/item?id=22367104
* perf https://news.ycombinator.com/item?id=26103776 https://kerkour.com/sqlite-for-servers https://fractaledmind.github.io/2024/04/15/sqlite-on-rails-the-how-and-why-of-optimal-performance/
* diff databases https://news.ycombinator.com/item?id=31256704
* corrupt a database https://news.ycombinator.com/item?id=31214131

## CLI

🗄️ `analytics.md` REPL > litecli
📜 https://sqlite.org/cli.html

CONF
* config location: `~/.sqliterc`
* cmd history: `~/.sqlite_history`

ZA
* create db from SQL script 💻 https://github.com/zachvalenta/query-sandbox-sakila
```sh
sqlite3 sakila.sqlite < schema.sql
sqlite3 sakila.sqlite < data.sql
```

---

CMD
```sh
# IO
sqlite3 / .quit # open/close
sqlite3 <name.db> # create empty
.open <file> # open / reload https://github.com/dbcli/litecli/issues/76

# LIST
l  # show file
.da  # list db
.tables # list tables
.schema <table> # describe schema

# MODES
.mode column  # overrides `.mode csv`  https://sqlite.org/cli.html#changing_output_formats https://dba.stackexchange.com/a/40672
.mode csv # query https://news.ycombinator.com/item?id=28299729 -> this doesn't work in litecli?
.headers on
.width  # https://dba.stackexchange.com/a/40672
.import foo.csv $ALIAS
select * from alias

# BACKUP https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html
sqlite3 $DB .dump > $DUMP.sql
sqlite3 my_database .dump | gzip -c > my_database.dump.gz  # dump
cat my_database.dump.gz | sqlite3 my_database  # restore
```

config
* default file location: pgcli(`~/.config/litecli/config`) sqlite()
* specify config file: `litecli --liteclirc <conf> <db_file>` 🗄 `query-sandbox`

db files
* create db file from script: interactive `sqlite3; .read seed.sql` https://sqlite.org/cli.html#special_commands_to_sqlite3_dot_commands_ interactive `sqlite3 test.db < test_schema.sql` https://stackoverflow.com/q/42245816/6813490 http://flask.pocoo.org/docs/0.12/tutorial/dbinit/#tutorial-dbinit

## design

🗄️ `OLAP.md` Graft

META
* all tables live in the `main` schema https://www.sqlite.org/lang_naming.html 🗄️ `modeling.md` namespaces

REASONS NOT TO USE https://pid1.dev/posts/siren-call-of-sqlite-on-the-server/ https://news.ycombinator.com/item?id=43049659
* need LiteFS for multiserver
* bad at schema migrations
* bad at multi-user https://news.ycombinator.com/item?id=43535943

ALTERNATIVES
* Postgres for Java https://github.com/zonkyio/embedded-postgres-binaries
* Postgres for Rust https://github.com/theseus-rs/postgresql-embedded https://github.com/faokunega/pg-embed
* _pglite_: embedded Postgres for WASM https://pglite.dev/ https://github.com/wey-gu/py-pglite
* _turso/limbo_: https://github.com/tursodatabase/libsql https://github.com/tursodatabase/limbo/
* from guy who did TigerBeetle? + deterministic simulation testing (DST) https://changelog.com/podcast/626 🗄️ TLA https://www.hytradboi.com/2025/c222d11a-6f4d-4211-a243-f5b7fafc8d79-rocket-science-of-simulation-testing https://www.hytradboi.com/2025/0c713342-7476-480e-b1ab-2ae97246826d-language-agnostic-simulation-testing-on-a-budget
* sync https://news.ycombinator.com/item?id=43535943
* https://news.ycombinator.com/item?id=42378843
* https://simonwillison.net/2024/Dec/15/in-search-of-a-faster-sqlite/ https://avi.im/blag/2024/faster-sqlite/

---

internals https://news.ycombinator.com/item?id=43682006
concurrent writers, Litestream for backups/replication https://avi.im/blag/2024/sqlite-bad-rep/ https://sqlite.org/talks/howitworks-20240624.pdf https://news.ycombinator.com/item?id=42665708 https://news.ycombinator.com/item?id=42666847

📜 https://sqlite.org/quirks.html

https://joyofrails.com/articles/what-you-need-to-know-about-sqlite

COMPONENTS
* _SQLite_: library https://tech.marksblogg.com/sqlite3-tutorial-and-guide.html
* Go port https://simonwillison.net/2022/Jan/30/a-cgo-free-port-of-sqlite/
* plumbing https://jvns.ca/blog/2014/09/27/how-does-sqlite-work-part-1-pages/ https://jvns.ca/blog/2014/10/02/how-does-sqlite-work-part-2-btrees/
* BYO https://github.com/alexpasmantier/resql https://news.ycombinator.com/item?id=43183891 hex dump https://blog.jabid.in/2024/11/24/sqlite.html
* _sqlite3_: CLI
* _sqlite3_: also the name of the Python lib/driver https://github.com/zachvalenta/sqlite3-demo https://github.com/zachvalenta/bookcase-sjk https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

STRONG POINTS https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html https://www.sqlite.org/whentouse.html
* stability https://news.ycombinator.com/item?id=41347188
* dbms in a C library
* ACID-compliant
* multithreaded https://sqlite.org/threadsafe.html
* reads parallelized 
* writes concurrent
> This means that writers queue up. Each application does its database work quickly and moves on, and no lock lasts for more than a few milliseconds
* file-based/serverless = good for unreliable network (smartphone, airplane)
* db files can deal w/ TB https://news.ycombinator.com/item?id=24178013
* faster than filesystem https://news.ycombinator.com/item?id=41085376

LIMITATIONS
* auth https://news.ycombinator.com/item?id=36922518
* files https://news.ycombinator.com/item?id=32146245
* schema changes require downtime, PRAGMA https://news.ycombinator.com/item?id=31152490
* doesn't support right join or full outer join https://sqlite.org/omitted.html added for 3.9 https://sqlite.org/releaselog/3_39_0.html
* only support single user 📙 Osborn 6.33 https://news.ycombinator.com/item?id=31152490
* data types differ from other dbms, problem for porting?
* no perms, security 📙 Takahashi 1.19 no users 📙 ibid 1.20

TYPES
* types: text, blob, null, int (whole num) real (decimal)
* _class_: type for cell https://stackoverflow.com/a/3388158
* _affinity_: type for attr
> The type affinity of a column is the recommended type for data stored in that column. The important idea here is that the type is recommended, not required. Any column can still store any type of data. It is just that some columns, given the choice, will prefer to use one storage class over another. The preferred storage class for a column is called its "affinity". - https://www.sqlite.org/datatype3.html#type_affinity
* _manifest typing_: type information scoped to cell instead of column (as in most other dbms)
* dynamic vs. static https://www.sqlite.org/datatype3.html https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html
* can ️lead to problems when porting to other DBMS
* avoid type conversion https://news.ycombinator.com/item?id=28259104
```sql
CREATE TABLE tIssue (
    id   INTEGER PRIMARY KEY NOT NULL CHECK (typeof(id) = 'integer'),
    col1 BLOB NOT NULL                CHECK (typeof(col1) = 'blob'),
    col2 TEXT                         CHECK (typeof(col2) = 'text' OR col2 IS NULL)
);
```

constraints
* _PK_: `integer primary key` will autoincrement https://stackoverflow.com/a/8519985/6813490
* just points to `rowid` https://stackoverflow.com/a/7906029/6813490
* typically don't need `autoincrement` https://sqlite.org/autoinc.html https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html
* `rowid`: default attr on all tables https://www.sqlite.org/rowidtable.html https://sqlite.org/withoutrowid.html
* _FK_: `pragma foreign_keys = on;`; have to turn on each time you connect https://sqlite.org/foreignkeys.html https://stackoverflow.com/a/9937992/6813490 🗄 `bookcase`
* FK w/ SQLAlchemy: w/ Flask https://fastapi.tiangolo.com/tutorial/sql-databases/ https://www.youtube.com/watch?v=lnfrcHdE_HI https://stackoverflow.com/questions/38792722/flask-foreign-key-constraint https://stackoverflow.com/questions/2614984/sqlite-sqlalchemy-how-to-enforce-foreign-keys have access to engine http://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#road-to-enlightenment
> rn Flask-SQLA will happily violate FK or just leave null 
* `pragma`: cmd to set env var

## extensions

---

SQLEAN
* pkg manager https://github.com/nalgeon/sqlpkg-cli

* https://github.com/nalgeon/sqlean https://github.com/zachvalenta/golf https://sqlpkg.org/
https://github.com/nalgeon/sqlean/blob/main/docs/shell.md
https://github.com/nalgeon/sqlean/blob/main/docs/install.md#download-package-manager
PG version https://pgt.dev/
https://grok.com/chat/e78c92cc-0d1f-4445-81de-8c55947f34c5
* sqlean using with litecli https://github.com/dbcli/litecli/pull/220

* fewer functions than other dbms
* _FTS4_: extension for search https://simonwillison.net/2019/Jan/7/exploring-search-relevance-algorithms-sqlite/ https://llm.datasette.io/en/stable/logging.html https://www.philipotoole.com/building-a-highly-available-search-engine-using-sqlite/ 🗄 `algos.md` FTS https://amjith.com/blog/2023/fts_search/

## 🟠 litecli

📜 https://github.com/dbcli/litecli
🗄️
* `OLTP.md` SQLite > CLI
* `python/pkg.md` venv
💻
* https://github.com/dbcli/litecli/pull/216
* https://github.com/dbcli/litecli/pull/217

* dot commands
```sh
.schema       # all schemas
.schema $TBL  # schema for table
.tables       # list tables
.databases    # list databases
.views        # list views -> even though they screwed me on credit last time, probably worth updating this to show both the name and the actual content of the view
```
* open db: `litecli $DB`
* config: `~/.config/litecli/config` https://litecli.com/config/
* query to CSV
```sh
# if the query is dealing with quoting around goofy column names, you may need to `echo $QUERY > query.sql` and then `litecli db.sqlite --csv < query.sql > out.csv`

litecli db.sqlite -e "select eid, mfg, mpn, apn, buyline, priceline, year_sales, last_sale, list_price, list_price_effective_date, date_created, date_updated, gross_profit from products where buyline like '%dongan%'" --csv > dongan-products.csv

litecli db.sqlite -e "select wh.hash, q.* from quote q join with_hashes wh on q.manufacturer_input = wh.manufacturer_input where q.manufacturer_part_number_input = wh.manufacturer_part_number_input" --csv > with-hashes.csv

litecli db.sqlite -e "select * from festo" --csv > with-hashes.csv
```
* LLM features forces install of Willison's lib into global pip userspace https://github.com/dbcli/litecli/issues/222
> In general, Python packaging is still unsettled to the point where IMO feels a bit odd to dictate the installation method (for a CLI) in a way that it wouldn't be in Rust given cargo's ubiquity.

---

* favorites/snippets https://github.com/zachvalenta/query-sandbox
* sqlite-utils plugin https://amjith.com/blog/2023/sqlite_utils_litecli/
* interview https://talkpython.fm/episodes/show/421/python-at-netflix

LLM
* https://amjith.com/blog/2024/introducing-llm-to-litecli/
* https://amjith.com/blog/2025/llm-in-litecli-1/
* https://amjith.com/blog/2025/llm-in-litecli-2/

## ⚛️ sqlite-utils

🛠️ https://github.com/simonw/sqlite-utils

LOAD CSV TO SQLITE
```sh
sqlite-utils insert db.sqlite $SQLITE_TABLE_NAME $PATH_TO_CSV --csv

# idky but remember this being broken for a while
vd orders.csv -b -o foo.sqlite

# ❓ couldn't do from litecli/sqlite3 directly?
.import entity-pn.csv entity_pn  # just tried to import this CSV
entity-pn.csv:177587 expected 0 columns but found 3 - ignored  # got this error -> Strange, since when do i need to spec out the exact number of columns, seems like something that should just work. Is there a way you can config sqlite to do type inference on a sample subset of data and just figure it out. Imagine if you had to manually configure the column names and types every time you loaded a pandas dataframe. Barbaric!
```

OTHER USE CASES
```sh
$DB "SELECT * FROM $TBL LIMIT 5" --json      # RS as JSON
query $DB "SELECT COUNT(*) FROM $TBL"        # RS to stdout
transform $DB $TBL --rename $COL foo         # rename column
insert $DB $TBL $CSV --csv; serve $DB        # serve table as API
insert $DB $TBL $CSV --csv --pk=id --upsert  # upsert
rows $DB $TBL --csv > $CSV                   # export
schema $DB                                   # validate schema
```

# 🟨 ZA

## 💿 dbcli

📜 https://www.dbcli.com/

---

ALTERNATIVES
* CLI query https://github.com/neilotoole/sq https://github.com/PeepDB-dev/peepdb
* https://github.com/theseus-rs/rsql
* usql as alternative https://news.ycombinator.com/item?id=42161987

* exit: `exit`, `\q`
* open with env var: `cli -h`
* list tables: `\dt`
* help: `\?`
* autocomplete: `ctrl e`
* clear screen: `ctrl l`
* _metacommand_: preceded w/ backslash https://www.pgcli.com/commands
* set pager to bat: `pager = less -SRXF` https://www.pgcli.com/docs
* _named query_: snippet, saved query https://www.pgcli.com/named_queries.md https://simonwillison.net/2024/Dec/3/datasette-queries/
* syntax: `f` (litecli) `n` (pgcli)
* list: `\f` https://github.com/dbcli/pgcli/issues/1236
* save: `\fs <name> <query>` https://github.com/dbcli/pgcli/issues/938
* save w/ param: `\fs <name> <query where foo = $1>` https://github.com/dbcli/pgcli/issues/938
> broken in sandbox: could be pager, Python version, config (try default config installed in $HOME) https://github.com/dbcli/pgcli/search?q=codec&type=issues
* use: `\f <name>`
* use w/ param: `\f <name> "arg"`
* rm: `\fd <name>` https://litecli.com/favorites/

## MySQL

* https://news.ycombinator.com/item?id=42881012
> MariaDB was in the news a lot this past year, and not in a good way. We found out that the MariaDB Corporation (which is separate from the MariaDB Foundation) is apparently a dumpster fire. In 2022, the Corporation backdoor IPO-ed through a sketchy merger instrument known as a SPAC. But the stock ($MRDB) immediately lost 40% of its value three days after its IPO. Because the Corporation decided to speedrun its way to the NYSE and become a publicly traded company, its dirty laundry became public. By the end of 2023, the stock price had dropped by over 90% since its opening. Things are so rotten at MariaDB Corporation that the Foundation's CEO wrote an article complaining about how their relationship with the Corporation has soured since the IPO and they are hoping to "reboot" it. Other problems include Microsoft announcing in September 2023 that they will no longer offer MariaDB as a managed Azure service. Microsoft will instead focus on supporting MySQL. And just in case you are not aware, MariaDB is a fork of MySQL that MySQL's original creator, Monty Widenus, started after Oracle announced its acquisition of Sun Microsystems in 2009. Recall that Sun bought MySQL AB in 2008 after Oracle bought InnoBase (makers of InnoDB) in 2005. But now MySQL is doing fine and MariaDB is one with problems. You don't need to watch movies or television shows for entertainment! You can get all the drama you need in your life through databases! https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html
* TUI: https://github.com/charles-001/dolphie
* MariaDB is done https://news.ycombinator.com/item?id=27922687 https://news.ycombinator.com/item?id=35467243
* CLI: https://www.mycli.net/docs flags https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html
* GUI: https://sequelpro.com/
* no suppport previously for checking constraints https://www.youtube.com/watch?v=lnfrcHdE_HI 4:45 https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html
```sql
-- current db
select database();
-- list db
show databases;
-- use db
use <name>;
-- tables
show tables;
```
```sh
# LOGIN
mysql -h <host> -u <user> -p
# CMD FROM SHELL
mysql -u <user> -e <cmd>
# RUN SCRIPT
mysql -u <user> <dbname> < script.sql
# DUMP LOCAL https://github.com/zachvalenta/flyway-tutorial/blob/master/db-backup.sh
mysqldump -u <user> <db> > backup.sql
# DUMP REMOTE https://github.com/zachvalenta/flyway-tutorial/blob/master/db-restore.sh
mysqldump -h <host> -u <user> --single-transaction -p <db> > backup.sql
# LOAD
mysql -u <user> -e "DROP DATABASE IF EXISTS $DB; CREATE DATABASE $DB;
mysql -u $USER $DB < $BACKUP.sql
```

## Oracle

* apparently still much more feature rich than Postgres https://news.ycombinator.com/item?id=24582937
* CLI: seems like you need an account and the docs are shoddy https://dba.stackexchange.com/questions/65032/connect-to-sql-plus-from-command-line-using-connection-string
* account: same as work / phone 123456789 / ABC Corp 100 Commerce Blvd Orlando FL 32801
* GUI: SQL Developer; comment `CMD ALT /` exec `CTRL /`
* Oracle dev https://stackoverflow.com/users/146325/apc
* _Sybase_: SAP counterpart
