# ⛩️

## 参考

> All models are wrong, but some are useful - George Box 📙 Zuckerman simons [245]
🗄
*️ `OLAP.md` factors
* `data/internals.md`
* `science.md` metascience / categories
* `sql.md` keys, schema
📚
* Kent data/reality https://www.amazon.com/Data-Reality-Perspective-Perceiving-Information/dp/1935504215

## 进步

* https://buttondown.com/hillelwayne/archive/software-books-i-wish-i-could-read/ https://schema.org/docs/full.html
* Use UUID primary keys, Give everything created_at and updated_at, on update restrict on delete restrict, use schemas, enum tables, Mechanically name join tables, Almost always soft delete, Represent statuses as a log https://news.ycombinator.com/item?id=43379764 https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns
* metadata, timestamps https://news.ycombinator.com/item?id=43776967
* https://swizec.com/blog/why-software-only-moves-forward/

🔍 https://drawsql.app/templates
* enum > FK
* modeling payments https://news.ycombinator.com/item?id=36775098
* https://news.ycombinator.com/item?id=41146239&utm_term=comment

IMPORTANCE
> Data models are perhaps the most important part of developing software, because they have such a profound effect: not only on how the software is written, but also how we think about the problem that we are solving. 📙 Kleppmann [31]
> This is one reason it's so important to model your domain correctly: if, for example, you make something a property of A when it should be a property of B, the penalty is often that operations that formerly required checking all the As or all the Bs now require checking all the As and all the Bs. https://www.natemeyvis.com/writing/on-quadratic-complexity/
> Take data access patterns very seriously!...it's easy to turn something that should be logarithmic time into polynomial time https://calpaterson.com/activerecord.html

SEMANTICS
* _domain_: thing you're trying to model https://calpaterson.com/non-relational-beartraps.html
* _schema_: model of thing https://calpaterson.com/non-relational-beartraps.html
* general usage: table names + column name/type https://news.ycombinator.com/item?id=22723277
* Postgres usage: container for obj such as table or view https://news.ycombinator.com/item?id=22721914

https://news.ycombinator.com/item?id=42245927
abstraction and math https://neugierig.org/content/dfw/

# ⭕️ FACTORS

💻
* `OLAP.md` schemas
* `serde.md` columnar

TYPES 📙 Verdhan
* quantitative: discrete, continuous
* qualitative: binary, nominal, ordinal
* _continuous variable_: on a sliding scale e.g. weight of animal https://entropicthoughts.com/dichotomisation-discards-data
* _discrete variable_: distinct states e.g. coin is either heads or tails; aka categorical, dimensional https://en.wikipedia.org/wiki/Categorical_variable https://astralcodexten.substack.com/p/ontology-of-psychiatric-conditions
* _nominal_: unordered category e.g. flavors of ice cream
* _ordinal_: in a sequence e.g. negative/neutral/positive https://www.freecodecamp.org/news/types-of-data-in-statistics-nominal-ordinal-interval-and-ratio-data-types-explained-with-examples/

---

* fact tables: wide, often sparse, store metrics (e.g., sales data).
* dimension tables: narrow, dense, store descriptive attributes (e.g., product details).

## access

* _access pattern_: how you have to query based on schema https://calpaterson.com/non-relational-beartraps.html
* what you're prioritizing e.g. read/write vs. aggregations 📻 Macey [6:10]
* _upsert_: insert|update 📙 Bradshaw [46]
* _resolve_: `get_or_create()` in Django

## density

* _dense_: few nulls
* con: less flexible
* _sparse_: many nulls
* optional attributes e.g. `battery_life` for electronics but null for books
* con: slower queries due to null checks

### EAV

🗄️ column store

* approach to handling sparse data useful when dealing w/ situations where the number of attr associated with an entity can vary widely, and many attr don't apply to every entity
* example: medical records (EMR) where each patient might have different tests or conditions e.g. blood pressure = 120/80 or allergy = penicillin
* _entity_: obj e.g. product, user
* _attribute_: characteristic e.g. color, email
* _value_: val for attr e.g. red, `alice@gmail.com`
```md
| Entity_ID | Attribute | Value           |
|-----------|-----------|-----------------|
| 1         | Type      | Chair           |
| 1         | Color     | Red             |
| 1         | Price     | 45.99           |
| 2         | Name      | Alice           |
| 2         | Email     | alice@gmail.com |
| 2         | Age       | 42              |
```

## width

WIDE
* _wide_: high number of col relative to records
* akin to fact tables 🗄️ `OLAP.md`
* pro: reduces joins
* con: hard to maintain 📍 get example of mechanics

NARROW
* _narrow_: few col
* e.g. lookup table for country codes
* pro: good for normalization
* con: bad for joins
* _tall_: few col but many records
* e.g. time series

## taxonomy

🧠 https://chatgpt.com/c/672d1eca-8194-8004-a7bb-ab67c03b2a58

* design process https://www.amazon.com/gp/product/0136788041

---

ONTOLOGY
> semantic web, ML https://owlready2.readthedocs.io/en/latest/intro.html
* https://www.stephendiehl.com/posts/bfo/
* https://www.amazon.com/gp/product/1484265513
* https://www.amazon.com/gp/product/0262527812
* OWL files

relational to graph https://www.amazon.com/gp/product/1804618039 https://www.amazon.com/gp/product/1492044075
knowledge graph https://www.amazon.com/gp/product/1098127102 https://www.manning.com/books/knowledge-graphs-applied
semantic https://www.amazon.com/gp/product/1492054275

❗️ https://en.wikipedia.org/wiki/Information_science https://en.wikipedia.org/wiki/Ontology_(information_science)
🔗 https://en.wikipedia.org/wiki/Data_modeling

https://en.wikipedia.org/wiki/Domain_model
https://www.amazon.com/gp/product/1573875864

```sh
# start here https://en.wikipedia.org/wiki/Three-schema_approach
├── Conceptual # https://en.wikipedia.org/wiki/Conceptual_schema
│   └── Entity-Relationship (ER) # https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model https://en.wikipedia.org/wiki/Relational_Model/Tasmania https://en.wikipedia.org/wiki/Information_model
│   └── Object-Oriented  # https://en.wikipedia.org/wiki/Object%E2%80%93role_modeling
│   └── Semantic Data # Alexopoulos semantic https://www.amazon.com/gp/product/1492054275 https://claude.ai/chat/1951b863-e794-4d77-971b-5e9a515f15ee https://en.wikipedia.org/wiki/Semantic_data_model semantic web https://en.wikipedia.org/wiki/Semantic_technology Codd https://en.wikipedia.org/wiki/Relational_Model/Tasmania
│       ├── Ontologies
│       ├── Taxonomies
│       ├── Conceptual Graphs # https://en.wikipedia.org/wiki/Conceptual_graph https://en.wikipedia.org/wiki/Concept_map
├── Logical # https://en.wikipedia.org/wiki/Logical_schema
│   └── Relational
│   └── Object-Relational # https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping
│   └── Hierarchical
│   └── Network
├── Physical  # https://en.wikipedia.org/wiki/Physical_schema
│   └── Database Schema Design
│   └── Indexing and Optimization
│   └── Partitioning and Replication
├── Dimensional
│   └── Star Schema
│   └── Snowflake Schema
│   └── Fact and Dimension Tables
├── Graph
│   └── Node and Edge
│   └── Property Graph
│   └── RDF (Resource Description Framework)
├── Temporal
│   └── Historical
│   └── Time-Series 
├── NoSQL
│   └── Key-Value Store
│   └── Document Store
│   └── Column-Family Store 
│   └── Graph Store
├── Object-Oriented Data
│   └── Classes and Inheritance
│   └── Encapsulation and Polymorphism
```

* https://www.amazon.com/gp/product/1573875864 https://www.hedden-information.com/
```txt
Hierarchical taxonomies – for browsing topics tagged to content
Faceted taxonomies – for filtering or refining results by topical aspects
Thesauri – for consistent indexing and accurate retrieval of large numbers of documents
Metadata schema – for effective content management, organization, and retrieval
Ontologies – for modeling semantic relationships between defined classes and their entities
Book indexes – for indicating page numbers of topics and names in printed books
```

# 🗺️ NON

📙 Kleppmann ch. 2
🗄️ `data/graphs.md`

> There are data stores that are also used as message queues (Redis), and there are message queues with database-like durability guarantees (Kafka), so the boundaries between the categories are becoming blurred 📙 Kleppmann [12]

* modeling from different angles https://www.openmymind.net/2011/7/5/Rethink-your-Data-Model/

---

* 📙 Thomas pragmatic programmer [166]
* Datomic (Hickey), datalog/prolog https://news.ycombinator.com/item?id=21742222 https://kevinlynagh.com/newsletter/2022_04_on_datalog_application_databases/ https://news.ycombinator.com/item?id=31154039 https://news.ycombinator.com/item?id=35094017 https://news.ycombinator.com/item?id=35727967 https://clojure.org/news/2023/08/04/next-rich https://www.hytradboi.com/2022/simple-graph-sqlite-as-probably-the-only-graph-database-youll-ever-need https://news.ycombinator.com/item?id=41642969
* can be a problem is you need to change the PK https://calpaterson.com/non-relational-beartraps.html
> Changing the primary key of a table is a surprisingly common activity. In truth, it's pretty easy to pick something that initially looks like it will be unique but which later turns out to not be unique...Unfortunately, in many non-relational database systems the primary key is "special". For example, Dynamo-style systems will use the primary key to decide which of the partitions the record will go on.
* _polyglot persistence_: using multiple types of data stores 📙 Kleppmann 2.29 because choosing just one is no fun :) https://old.reddit.com/r/learnpython/comments/glbuog/whats_is_your_decision_process_between_csv_json/
* _block_: https://news.ycombinator.com/item?id=27200177
* immutable https://github.com/codenotary/immudb

## column store

🗄️
* EAV
* `serde.md` columnar

---

akin to EAV, implement in SQLite https://chatgpt.com/c/67d9846c-0f08-8004-aa74-31e6e5e825b2

A "wide column store," as I previously defined, is a NoSQL database architecture, not a file format. It’s designed for scalability and flexibility in handling dynamic, sparse, or massive datasets:

Structure: Data is organized by rows, where each row has a key (e.g., user_id) and an associated set of columns. Unlike columnar file formats, the columns per row can differ—some rows might have 5 columns, others 50,000. Columns are often grouped into "column families" for performance.
Purpose: Built for big data systems needing high write throughput, scalability, and flexibility. It’s less about analytics and more about operational workloads (e.g., real-time user data lookups).
Key Trait: Dynamic schema. Each row can have a unique set of columns, and the system doesn’t enforce a fixed structure across all rows. This sparsity and variability distinguish it from columnar file formats.
Examples: Apache Cassandra, Google BigTable, HBase.
Focus: Distributed database storage and retrieval, optimized for scale and adaptability.

* _column store_: not row-oriented (like OLTP)
* can do in Sqlite? https://news.ycombinator.com/item?id=39207570&utm_term=comment
* 不明觉厉 https://news.ycombinator.com/item?id=36571110
* e.g. instead of looking for all `price` values by iterating over every sale record, just grab `price` column 📙 Kleppmann 96
* ❓ stores data differently on disk https://nchammas.com/writing/database-access-patterns
* in order to reconstruct a row, everything in row must be stored as nth in column 📙 Kleppmann 100
* _wide column store_: ❓
* CMU, Pavlo https://www.youtube.com/watch?v=fr5lIchF6pw
* vectorized execution https://talkpython.fm/episodes/transcript/491/duckdb-and-python-ducks-and-snakes-living-together

DBMS https://en.wikipedia.org/wiki/List_of_column-oriented_DBMSes
* Cassandra https://stackoverflow.com/q/13010225 https://www.youtube.com/watch?v=J-cSy5MeMOA 📙 Kleppmann 99 https://news.ycombinator.com/item?id=28292369 https://simonwillison.net/2021/Aug/24/how-discord-stores-billions-of-messages/ https://news.ycombinator.com/item?id=41683293
* _Bigtable_: wide table = document store in SQL https://en.wikipedia.org/wiki/Wide-column_store
* _HBase_: Hadoop db

## document

---

📙 Kleppmann 2.28-42

https://news.ycombinator.com/item?id=42103788

> The thrust of it is that databases that are in the same genre as DynamoDB - which includes Cassandra and MongoDB - are fantastic if - and this is a load bearing if: You know exactly what your app needs to do, up-front. You know exactly what your access patterns will be, up-front. You have a known need to scale to really large sizes of data. You are okay giving up some level of consistency. This is because this sort of database is basically a giant distributed hash map. The only operations that work without needing to scan the entire database are lookups by partition key and scans that make use of a sort key. Whatever queries you need to make, you need to encode that knowledge in one of those indexes before you store it. You want to store users and look them up by either first name or last name? Well you best have a sort key that looks like `$FIRST_NAME $LAST_NAME>`. Your access patterns should be baked into how you store your data. If your access patterns change significantly, you might need to reprocess all of your data. https://mccue.dev/pages/8-16-24-just-use-postgres

document store
* _document_: JSON "obj"
* replaces row as paradigm 📙 Bradshaw [3]
* _schema_: structure of document https://docs.mongodb.com/realm/schemas/
* not fixed i.e. inconsistent intra-collection 📙 Bradshaw [3]
* _document reference_: UUID 📙 Kleppmann 3.38
* _field_: key
* _subdocument_: document key whose value is itself a document https://youtu.be/SM9gJv08dm0 1:20
* aka embedded 📙 Bradshaw [174]
* _collection_: group of documents

design
* 1-M w/in document itself
* M-M via document reference 📙 Kleppmann 3.38
* joins https://news.ycombinator.com/item?id=22834036
* good for 1-M or no relationships 📙 Kleppmann 2.49
* flexiblity: schema per doc aka schemaless/schema-on-read, obviates need for migrations 📙 Kleppmann 2.63, 4.111
* easier to scale/shard apparently, locality 📙 Kleppmann 2.32
* transactions only at level of single document https://docs.mongodb.com/v3.4/core/write-operations-atomicity/
* easy to have dupes 📙 Kleppmann 2.33
* hands off processing to application, so it's both slower in dev time and execution time 📙 Bradshaw [8]

DBMS
* more embedded https://claude.ai/chat/16d7d074-a06e-4a93-9d29-87181f9c9e74
* BYO https://notes.eatonphil.com/documentdb.html
* _CouchDB_: good at replication https://www.dataengineeringpodcast.com/couchdb-document-database-episode-124/ 7:15 
* _Dante_: 🎯 embedded https://github.com/senko/dante
* _DocumentDB_: https://github.com/microsoft/documentdb
* _Lungo_: 🎯 embedded, Mongo compatible Golang impl https://github.com/256dpi/lungo
* _JameSQL_: 🎯 embedded https://github.com/capjamesg/jamesql
* _Mongo_: OSS alternative https://github.com/FerretDB/FerretDB https://pythonbytes.fm/episodes/show/318/gil-how-we-will-miss-you
* _Polo_: embedded https://github.com/vincentdchan/PoloDB
* _Postgres_: JSON https://www.enterprisedb.com/blog/representing-graphs-postgresql-sqlpgq
* _TinyDB_: 🎯 embedded https://github.com/msiemens/tinydb
* not atomic but potential workaround https://tinydb.readthedocs.io/en/latest/extensions.html#tinyrecord

HIERARCHICAL
* _hierarchical database_: document store + tree structure i.e. child only has one parent 📙 Takahashi [39] Beaulieu [2]
* too rigid for a data store https://stratechery.com/2016/oracles-cloudy-future/ https://twobithistory.org/2017/12/29/codd-relational-model.html
* e.g. file system, DNS https://www.postgresql.org/docs/12/tutorial-concepts.html 📙 Kleppmann 2.36-38
* used in Zookeeper https://www.youtube.com/watch?v=Vv4HpLfqAz4 8:50
* can be done in relational as well https://hoverbear.org/blog/postgresql-hierarchical-structures/
* _IMS_: https://twobithistory.org/2017/10/07/the-most-important-database.html

## graph

📚
* https://www.manning.com/books/graph-databases-in-action
* https://www.amazon.com/gp/product/1492044075

---

start here https://www.richard-towers.com/2025/02/16/representing-graphs-in-postgres.html

* _Memgraph_: https://memgraph.com/blog/nasa-memgraph-people-knowledge-graph
* _EdgeDB_: graph-relational = no impedance mismatch but still relational https://news.ycombinator.com/item?id=30290225 built on Postgres https://www.geldata.com/blog/edgedb-is-now-gel-and-postgres-is-the-future
* Postgres https://supabase.com/blog/pgrouting-postgres-graph-database
* _Age_: graph for Postgres https://age.apache.org/
* _PGQ_: property graph queries https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html
> SQL now supports defining read-only queries on graphs. This allows an application to declare a property graph structure over existing tables. It is left up to the DBMS to decide whether to create an auxiliary data structure (e.g., adjacency matrix) for the property graph or just keep track of the meta-data. You can then write graph traversal queries in SQL using the MATCH keyword. The syntax builds on existing languages (e.g., Neo4j's Cypher, Oracle’s PGQL, and TigerGraph’s GSQL), and shares aspects of the emerging GQL standard. As of January 2024, the only DBMS that I am aware of that supports SQL/PGQ features is Oracle. There is an experimental branch of DuckDB that also supports SQL/PGQ.
> SQL/PGQ is a big deal. However, I do not foresee it being an immediate deathblow for graph DBMSs, as there are already several ways to translate graph-oriented queries to SQL. Some DBMSs, including SQL Server and Oracle, provide built-in SQL extensions that make storing and querying graph data easier. Amazon Neptune is a graph-oriented veneer on top of their Aurora MySQL offering. Apache AGE provides an OpenCypher interface on top of PostgreSQL. I expect other major OLAP systems (e.g., Snowflake, Redshift, BigQuery) will support SQL/PGQ in the near future.
> Adding SQL/PGQ in a DBMS is not as simple as adding support for the new syntax. There are several engineering considerations to ensure graph queries perform well. For example, graph queries perform multi-way joins to traverse the graph. But a problem arises when the intermediate results for these joins are larger than the base tables. A DBMS must use a worst-case optimal join (WCOJ) algorithm to execute such joins more efficiently than the usual hash join used when joining two tables. Another important technique is to use factorization to avoid materializing redundant intermediate results during joins. This type of compression helps the DBMS avoid blowing out its memory with the same join record over and over again.

* Tiger Graph, Dgraph https://softwareengineeringdaily.com/2021/01/19/dgraph-native-graphql-database-with-manish-jain/ Memgraph, Terminus db, embedded https://github.com/CodyKochmann/graphdb https://github.com/dpapathanasiou/simple-graph cache for dgraph https://github.com/dgraph-io/ristretto

* _Neo4J_ https://media.pragprog.com/titles/pwrdata/neo4j.pdf https://calmcode.io/course/neo4j/introduction

https://danluu.com/yegge-predictions/
DBMS
* Mongo offers as well https://www.mongodb.com/databases/mongodb-graph-database
* SQLite, Postgres https://news.ycombinator.com/item?id=35386948
* _Age_: Postgres extension https://github.com/apache/age
* written in Python on top of Postgres https://talkpython.fm/episodes/show/355/edgedb-building-a-database-in-python
* _cozo_: 🎯 embedded w/ Datalog https://news.ycombinator.com/item?id=33518320 https://github.com/cozodb/cozo
* _Janus_: distributed, OSS https://github.com/JanusGraph/janusgraph
* _SQLite_: https://www.hytradboi.com/2022/simple-graph-sqlite-as-probably-the-only-graph-database-youll-ever-need
* _Tao_: distributed https://news.ycombinator.com/item?id=29045443 https://www.micahlerner.com/2021/10/13/tao-facebooks-distributed-data-store-for-the-social-graph.html
* _network database_: similar to graph https://stackoverflow.com/a/52325525 📙 Takahashi [2.39]
* anything that would have ever been network is now SQL https://www.prisma.io/blog/comparison-of-database-models-1iz9u29nwn37 📙 Kleppmann [2.36]

QUERY LANGUAGES
* _Cypher_: declarative
* _GQL_: emerging standard https://stackoverflow.com/q/13824962 https://www.youtube.com/watch?v=h8cyPIEfxQY 11:30
* _Gremlin_: wrapper over Neo4J Java API https://www.manning.com/books/graph-databases-in-action

## key

---

EMBEDDED
* disk for storage https://github.com/peterbourgon/diskv
* _pickledb_: https://github.com/patx/pickledb
* _sled_: https://github.com/spacejam/sled
* _skate_: https://github.com/charmbracelet/skate
* _badger_: https://github.com/dgraph-io/badger

* _KV store_: hash map + persistence 📙 Kleppmann [72]
* distributed KV store used for service discovery (etcd) ()
* used for metadata, counters
> ZippyDB serves a number of use cases, ranging from metadata for a distributed filesystem, counting events for both internal and external purposes, to product data that’s used for various app features https://engineering.fb.com/2021/08/06/core-data/zippydb/
* impl: hash index; faster not bc they don't have to go to disk but bc don't have to translate in-mem data structure to something that can be written to disk 📙 Kleppmann [89]
* typed values allow for in/decrement, push/pop from list
* used for caching db result set e.g. memcached 📙 Kleppmann [89] https://github.com/akrylysov/pogreb
* RocksDB, memcached used as storage for distributed KV https://github.com/bitleak/kvrocks https://engineering.fb.com/2021/08/06/core-data/zippydb/ https://www.micahlerner.com/2021/05/31/scaling-memcache-at-facebook.html
* RocksDB alternative https://github.com/cockroachdb/pebble
* BYO: https://aosabook.org/en/500L/dbdb-dog-bed-database.html https://notes.eatonphil.com/2023-05-25-raft.html Bitcask https://github.com/avinassh/py-caskdb
> In short, keys are stored in a hash table in RAM, k/v pairs are written to log files. Dead simple, but powerful enough. https://news.ycombinator.com/item?id=31306678

za
* _object store_: KV in which K is ID and V is blob (file, binary) 🗄 `infra.md` AWS/S3
* can only create/update, not append https://stackoverflow.com/a/47524241
* sink https://ceph.io/ceph-storage/ https://github.com/minio/minio https://stackoverflow.com/questions/56627446/docker-compose-how-to-use-minio-in-and-outside-of-the-docker-network https://alexwlchan.net/2020/08/s3-keys-are-not-file-paths
* _flat file_: meant for config, no way to represent relationships or handle concurrency (e.g. prevent dirty read); some structure via delimiters, new lines https://www.prisma.io/blog/comparison-of-database-models-1iz9u29nwn37

## time series


OPTIONS
* _Timescale_: 🎯 Postgres extension https://www.tigerdata.com/ https://blog.timescale.com/blog/how-postgresql-aggregation-works-and-how-it-inspired-our-hyperfunctions-design-2/ https://softwareengineeringdaily.com/2021/06/28/timescale-time-series-databases-with-mike-freedman/ https://sarvendev.com/posts/timescale-db-to-the-rescue/
* _hypertable_: normal table split by time https://sqlfordevs.com/books+courses/timescale/01-hypertables

---

OPTIONS
* https://github.com/man-group/arctic https://github.com/man-group/ArcticDB https://www.youtube.com/watch?v=-QwbIM6lxIw
* _Influx_: https://softwareengineeringdaily.com/2019/08/21/time-series-databases-with-rob-skillington/ https://softwareengineeringdaily.com/2021/08/19/influxdata-time-series-data-with-russ-savage/
* _Husky_: event store https://www.datadoghq.com/blog/engineering/husky-deep-dive/
* _Lin_: https://github.com/lindb/lindb
* _tstorage_: embedded https://github.com/nakabonne/tstorage BYO https://nakabonne.dev/posts/write-tsdb-from-scratch/ https://news.ycombinator.com/item?id=27730854
* _Whisper_: embedded db for Graphite https://github.com/graphite-project/whisper

📙 https://www.manning.com/books/time-series-forecasting-using-foundation-models
🗄
* `math.md` graphs / uplot
* `infra.md` analytics

todo
* https://tsfresh.readthedocs.io/en/latest/
* forecasting https://github.com/facebook/prophet
* definition of time series data https://postgres.fm/episodes/time-series-considerations
* https://github.com/TDAmeritrade/stumpy
* Postgres https://tembo.io/blog/pg-timeseries
* https://www.youtube.com/watch?v=nT6UsVgJ0xw
* https://www.youtube.com/watch?v=Z6pghPlZ1vQ
* time-weighted average https://blog.timescale.com/blog/what-time-weighted-averages-are-and-why-you-should-care/?
* https://www.honeycomb.io/blog/time-series-database/
* https://news.ycombinator.com/item?id=28901063
* https://www.influxdata.com/blog/start-python-influxdb
* Homebrew analytics https://docs.brew.sh/Analytics

basics
* _time series_: KV in which K is time https://en.wikipedia.org/wiki/Time_series_database
* used for monitoring 🗄 `system.md` https://github.com/VictoriaMetrics/VictoriaMetrics
* _panel data_: timeseries for individuals https://en.wikipedia.org/wiki/Panel_data

libs
* _darts_: https://github.com/unit8co/darts/
* _kats_: https://github.com/facebookresearch/kats
* _sktime_: https://github.com/alan-turing-institute/sktime

# 🕸️ RELATIONAL

🗄️ `sql.md` schema / approaches
📚
* Hao grokking relational design https://www.manning.com/books/grokking-relational-database-design
* Karwin sql antipatterns https://pragprog.com/cms/errata/bksqla-errata/
* Sadalage refactoring databases https://www.youtube.com/watch?v=oMbrrYKYDvU

COMPONENTS 📙 Beaulieu [1.6]
* _entity_: thing you're trying to describe e.g. customer, order, et al. 📙 Beaulieu [8]
* _column_: aka attribute 📙 Hao grokking
* _row_: aka record, tuple (more academic)
* _value_: aka cell, field

## Codd

🗄️
* `dataframes.md`
* `sql.md`

---

RELATIONS
* _relationship_: what ties tables together https://twobithistory.org/2017/12/29/codd-relational-model.html
* _relational model_: Codd 📙 Kent data/reality [155] Beaulieu [5]
* _relational algebra_: https://news.ycombinator.com/item?id=39753749 https://www.scattered-thoughts.net/writing/unexplanations-relational-algebra-is-math/ https://www.scattered-thoughts.net/writing/unexplanations-sql-is-syntactic-sugar-for-relational-algebra/
> when embedding would result in duplication of data but would not provide sufficient read performance advantages to outweigh the implications of the duplication.
> to represent more complex many-to-many relationships
> to model large hierarchical data sets
> In the database community it has been conventional wisdom for nearly half a century now (basically since the invention of the relational model) that in designing your database schema you should be careful to avoid any kind of redundancy. That's what database normalization theory is all about. https://www.cell-lang.net/relations.html
* _denormalization_: when speed more of a concern 📙 Conery imposter [320] Kleppmann [491] Manga [62]
* _denormalized query engine_: subset of data for search https://speakerdeck.com/simon/the-denormalized-query-engine-design-pattern https://simonwillison.net/2020/Dec/19/dogsheep-beta/
* _locality_: proximity of data relevant to an entity 📙 Kleppmann [32] 🗄 `db.md` document
* _embeded_: NoSQL https://www.mongodb.com/docs/manual/core/data-model-design/
> you have "contains" relationships between entities
> you have one-to-many relationships between entities, in these relationships the "many" or child documents always appear with or are viewed in the context of the "one" or parent documents.
> embedding provides better performance for read operations, as well as the ability to request and retrieve related data in a single database operation.

CMU
* https://news.ycombinator.com/item?id=35599118
* Stonebraker https://dsf.berkeley.edu/papers/ERL-M85-95.pdf https://drewdevault.com/2021/08/05/In-praise-of-Postgres.html
* Pavlo https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf

> the creation of SQL at IBM Research by Don Chamberlain and Ray Boyce (RIP). Originally known as SEQUEL (Structured English QUEry Language) https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html
> Don Chamberlin details his early work with Ray Boyce designing the relational language SQL. After meeting E.F. (Ted) Codd at a symposium at the IBM T.J. Watson Research Center in Yorktown Heights, New York, in 1972, Boyce and Chamberlin believed that it should be possible to design a relational language that would be accessible to users without formal training in mathematics or computer programming. https://ieeexplore.ieee.org/document/6359709

> This past year saw the latest incarnation of the ISO/IEC 9075 specification, better known as SQL:2023. The update includes many "nice to haves" that deal with frustrations and inconsistencies in various SQL dialects (e.g., ANY_VALUE). Two enhancements to SQL that further erode the need for alternative data models and query languages are worth mentioning here. Remember that just because the SQL specification includes something does not mean that your favorite relational DBMS will immediately support these new features. https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html
> SQL is not perfect, of course, and it is not truly portable since every DBMS has its quirks, proprietary features, and non-standard extensions. https://www.cs.cmu.edu/~pavlo/blog/2024/01/2023-databases-retrospective.html

REPLACEMENTS
* Ibis
* https://medium.com/schkn/sql-is-dead-hail-to-flux-8e8498756049
* _Convex_: queries are code https://www.hytradboi.com/2025/f99f35fa-6b26-45a3-a4b2-37801fdefeff-database-ideas-in-convex https://www.convex.dev/
* _PSQL_: https://news.ycombinator.com/item?id=44942936
* _PRQL_: pipelined SQL alternative, all new syntax https://news.ycombinator.com/item?id=36866861 https://news.ycombinator.com/item?id=42231325 https://www.hytradboi.com/2025/deafce13-67ac-40fd-ac4b-175d53318a78-prql-a-modern-pipelined-sql-replacement
* _Malloy_: all new syntax, semantic focus https://news.ycombinator.com/item?id=30053860 https://news.ycombinator.com/item?id=42231325
* _preql_: much more ambitious, all new syntax https://news.ycombinator.com/item?id=26447070 https://news.ycombinator.com/item?id=42231325
* _Trilogy_: dimension tables https://news.ycombinator.com/item?id=42231325
* _Zillion_: semantic layer https://github.com/totalhack/zillion https://news.ycombinator.com/item?id=42231325 https://github.com/cube-js/cube

* boring and durable https://josephg.com/blog/databases-have-failed-the-web
* outdated and awkward https://news.ycombinator.com/item?id=33034351 https://news.ycombinator.com/item?id=39539252 https://news.ycombinator.com/item?id=41347188 https://buttondown.com/hillelwayne/archive/queryability-and-the-sublime-mediocrity-of-sql/
> The relational data model enables those things. None of them require the language to be SQL...LINQ, spark, flink, kafka streams, pandas, dataframes are all widely used examples of an expression-based language-embedded approach to relational queries. https://www.scattered-thoughts.net/writing/against-sql
> SQL is the most popular to communicate with databases but isn't always the easiest to write. I've been writing SQL statements since the 1990s and even in 2024, I can find myself needing to refer to documentation and spending 30 minutes or more getting more complex statements to run as I wish. https://tech.marksblogg.com/heavyiq-faa-ai-llm-gpu-database.html
* attempts at rewrite https://news.ycombinator.com/item?id=42231325 https://github.com/totalhack/zillion
* ISO, ANSI standard 📙 Beaulieu [86-87]
* SQL92 📙 Beaulieu [91]
* SQL2023 http://peter.eisentraut.org/blog/2023/04/04/sql-2023-is-finished-here-is-whats-new
* testing and business logic https://news.ycombinator.com/item?id=42828883

## 1-1

* = sole ownership
* impl: attr, separate table https://support.airtable.com/hc/en-us/articles/218734758#onetoone
* example: person-SSN, country-capital https://stackoverflow.com/a/15037461
* less common than you'd think https://www.b-list.org/weblog/2024/aug/27/highlander-problem/

## 1-M

aka fanout https://jmduke.com/posts/post/django-extract-epoch/
> The "fan-out" happens because a single post can be associated with multiple events, creating a "many" side for every "one" post.
> This pattern is common in systems where activities or logs are recorded for a parent entity (e.g., likes/comments on posts, purchases related to a user, etc.), allowing detailed tracking and aggregation of related data.

* = ownership
```sql
CREATE TABLE team(
    team_id INTEGER PRIMARY KEY,
);

CREATE TABLE player(
    player_id INTEGER PRIMARY KEY,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES team(team_id)
);
```

## M-M

* = collaboration
* aka join table, junction table https://stackoverflow.com/a/3419868
```sql
CREATE TABLE band(
    band_id INTEGER PRIMARY KEY,
);

CREATE TABLE musician(
    musician_id INTEGER PRIMARY KEY,
);

CREATE TABLE band_musician(
    bm_id INTEGER PRIMARY KEY,
    band INTEGER,
    musician INTEGER,
    FOREIGN KEY (band) REFERENCES band(band_id)
    FOREIGN KEY (musician) REFERENCES band(musician_id)
);
```

## name spaces

> on a file system, you can nest folders arbitrarily deep. in a database, all tables are in same directory (so to speak). so you get ugliness like: sales, sales_monthly, sales_report. surely i'm not the only one that finds this offensive?
> The reason you don't get arbitrary nesting in databases is partly philosophical: tables are meant to be logical entities, not files, and relationships between them (via foreign keys, etc.) are supposed to define structure. File systems prioritize storage hierarchy; databases prioritize queryable relationships. But I get it - it still feels wrong when you're staring at a mess of table names.

VIEW-BASED
* = raw data in big dumb tables and views for namespaces
* con: views non-materialized by default i.e. slower queries
* con: materialized views need to be manually refreshed
* con: views read-only by default
* con: direct table queries better for indexing

SCHEMAS
* _schema_: namespace for objs like tables, views, functions https://www.postgresql.org/docs/current/ddl-schemas.html
* akin to spans in Great Tables https://posit-dev.github.io/great-tables/get-started/basic-column-labels.html
* simulate in Pandas using multindex columns (but not in Polars)
> doesn't seem like a way to simulate in SQL
* maybe someday in Turso? https://github.com/tursodatabase/limbo/issues/1078
* only in Postgres, Snowflake
```sql
CREATE SCHEMA foo;
CREATE TABLE foo.tbl (
    col1 text,
    col2 integer
);
```

QUERYING ACROSS DATABASES
* SQLite: FKs don't work
```sql
ATTACH DATABASE 'other.db' AS other_db;
SELECT * FROM main.sales INNER JOIN other_db.customers ON sales.customer_id = customers.id;
```
* Postgres: foreign data wrappers
```sql
CREATE EXTENSION postgres_fdw;
CREATE SERVER other_db FOREIGN DATA WRAPPER postgres_fdw OPTIONS (dbname 'otherdb');
SELECT * FROM other_db.public.some_table;
```

ZA
* 🎯 BYO table groupings in SQLite
```sql
CREATE TABLE table_groups (
    table_name TEXT PRIMARY KEY,
    group_name TEXT
);

INSERT INTO table_groups (table_name, group_name) VALUES
    ('sales', 'Sales'),
    ('sales_monthly', 'Sales'),
    ('inventory', 'Operations');

SELECT tm.name, tg.group_name FROM sqlite_master tm LEFT JOIN table_groups tg ON tm.name = tg.table_name WHERE tm.type = 'table';
```
* partition: good fit only for temporal/spacial vs. logical taxonomy?
```sql
CREATE TABLE sales_2024 PARTITION OF sales FOR VALUES FROM ('2024-01-01') TO ('2024-12-31');
```
* _table prefixing_: sales_orders, sales_reports, sales_accounts_receivable

## normalization

* _normalization_: process of extracting entities from other entities https://en.wikipedia.org/wiki/Database_normalization#Normal_forms

ANOMOLIES
* _delete_: delete causes loss of other important info e.g. if employee and project_id in same table, rm employee also removes project

FORMS
* _form_: step in normalization
* avoids redundancy (no `author` in `book` bc you'd repeat Jane Austen for each novel)
* saves space (no dupes) 📙 Kleppmann [33]
* howto: one big mess and decompose from there, think of example queries
* _1NF_: 1 value for each attr
* aka atomic 📙 Takahashi [58] Winand [6]
```sql
-- pre-1NF: n values for each record
insert into danzi(item) values ('quesidilla, churro');

-- 1NF: 1 value for each record
insert into danzi(item) values ('quesidilla');
insert into danzi(item) values ('churro');
```
* _2NF_: non-PK must be related to PK 📙 Conery imposter 316 Takahashi 3.63 https://stackoverflow.com/a/724032
* symptom is redundancy (value repeats across records w/out reference to FK) and therefore anomaly (value could be mispelled) 📙 Karwin [289]
```sql
-- TITLE dependent on COURSE_ID but unrelated to SEMESTER_ID
CourseID | SemesterID | #Places  | Title        |
------------------------------------------------|
IT101    |   2009-1   | 100      | Programming  |
IT101    |   2009-2   | 100      | Programming  |
IT102    |   2009-1   | 200      | Databases    |
IT102    |   2010-1   | 150      | Databases    |
IT103    |   2009-2   | 120      | Web Design   |
```
* _3NF_: don't get difference from 2NF 📙 Conery imposter 318 Karwin 291
* the generally accepted level of normalization 📙 Winand 1.4
* https://stackoverflow.com/a/724013/6813490 https://www.mikealche.com/software-development/a-humble-guide-to-database-schema-design
```sql
-- todo
```
* _5NF (Boyce-Codd)_: when you're going too far 📙 Winand [5]

# 🖼️ REPR

## ERD (d2)

🗄️ `architecture.md` d2

---

https://whodb.clidey.com/docs/usage-basics/using-the-graph-visualizer
https://www.drawdb.app/
* Jonathan Edwards schema exploration https://www.hytradboi.com/2025/3b6de0f0-c61c-4e70-9bae-cca5a0e5bb7b-db-usability-as-if
🗄 `analytics.md` tooling / GUI 🧠 https://chatgpt.com/c/673ce0d8-543c-8004-93c3-90df2d298ecf
> can use d2 https://github.com/zekenie/d2-erd-from-postgres https://terrastruct.com/blog/post/generate-diagrams-programmatically/
* symbols 📙 Karwin [7]
* SQLite https://github.com/Dicklesworthstone/sqlalchemy_data_model_visualizer https://gitlab.com/Screwtapello/sqlite-schema-diagram
* Django https://github.com/pikhovkin/django-schema-viewer
* _databasediagram_: https://databasediagram.com/
* _dbdocs_: 🎯 https://dbdocs.io/
* _drawdb_: https://drawdb.vercel.app/
* _DrawSQL_: https://drawsql.app/me-195/diagrams/testing123
* _erd_: https://github.com/BurntSushi/erd
* _excalidraw_: https://excalidraw.com/ https://gist.github.com/zachvalenta/f4c2226b991b69d129fe7d1d40119f43
* _GraphViz_: w/ pydantic + dataclasses https://pythonbytes.fm/episodes/show/403/a-machine-learning-algorithm-walks-into-a-bar
* wrapper https://news.ycombinator.com/item?id=42044771
* _quickdatabasediagrams_: https://app.quickdatabasediagrams.com/#/
* _sketchviz_: uses GraphViz https://sketchviz.com/graphviz-examples

## UML

> can use d2 https://d2lang.com/tour/uml-classes
* https://www.amazon.com/UML-Distilled-Standard-Modeling-Language/dp/0321193687 https://yuml.me/diagram/scruffy/class/draw
* aka class diagram
* PlantUML
* alternative syntax 📙 Evans domain-driven [42]
* can be used for ERD in Mongo https://stackoverflow.com/q/11323841 https://stackoverflow.com/q/6010408
