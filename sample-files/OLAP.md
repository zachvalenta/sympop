# ⛩️

## 参考

🔍 
* https://dba.stackexchange.com
* https://roadmap.sh/postgresql-dba
* https://github.com/DataExpert-io/data-engineer-handbook
📚
* ⭐️ https://dedp.online/
* Kleppmann data intensive applications
* Reis fundamentals of data eng

## 进步

https://www.ssp.sh/brain/data-engineering/
https://www.ssp.sh/blog/practical-data-modeling-clickhouse/

https://news.ycombinator.com/item?id=42078067
> We love Postgres for its simplicity, power, and rich ecosystem. But engineers have to still get bogged down with heavyweight and expensive OLAP systems when connecting an analytics data stack.
> Postgres is amazing at OLTP queries, but not for OLAP queries (large data scans and aggregations). Even in this case, we’ve still heard from countless scaling startups that they still try to use only a read replica to run analytics workloads since they don’t want to deal with the data engineering complexity of the alternative. This actually works surprising well initially, but starts to break for them as they scale or when integrating multiple data sources. Adding lots of indexes to support analytics also slows down their transactional write performance.
> When growing out of “just use Postgres”, companies have to understand and wrangle complex ETL pipelines, CDC processes, and data warehouses — adding layers of complexity that defeat the simplicity that undermines their initial choice for Postgres as their data storage in the first place.
> We thought there had to be a better way, so we’re building BemiDB. It’s designed to handle complex analytical queries at scale without the usual overhead. It’s a single binary that automatically syncs with Postgres data and is Postgres-compatible, so it’s like querying standard Postgres and works with all existing tools.
> Under the hood, we use Apache Iceberg (with Parquet data files) stored in S3. This allows for bottomless inexpensive storage, compressed data in columnar files, and an open format that guarantees compatibility with other data tools.
> We embed DuckDB as the query engine for in-memory analytics that work for complex queries. With efficient columnar storage and vectorized execution, we’re aiming for faster results without heavy infra. BemiDB communicates over the Postgres wire protocol to make all querying Postgres-compatible.
> We want to simplify data stacks for companies that use Postgres by reducing complexity (single binary and S3), using non-proprietary data formats (Iceberg open tables), and removing vendor lock-in (open source). We'd love to hear your feedback! What do you think?

JOB MARKET
JOB MARKET
JOB MARKET
https://news.ycombinator.com/item?id=44505165
https://www.dedp.online/
* database design and perf https://posetteconf.com/2025/talks/best-practices-for-tuning-slow-postgres-queries/ https://posetteconf.com/2025/talks/designing-for-document-databases-in-postgresql/
```sh
# https://data.reelgood.com/job/data-analyst/
Proven ability to identify and solve problems using analytical methods.
Proven experience with SQL in handling large amounts of data.
Familiarity with statistical computing languages such as R to extract insights from large data sets.
Experience in data collection, cleaning, and normalization from various sources for statistical analysis.
Familiarity with statistical techniques and concepts such as regression, statistical tests, and data distributions, as well as their proper application.
Effective in communicating technical and complex information in a clear and simple manner.
Expertise in presenting data visually to effectively communicate project results.
Experience in developing interactive dashboards and visualizations using tools such as Power BI, QuickSight, or Tableau to effectively communicate insights to other business units.
```
* data eng
```txt
Data workflows: Design, build, and maintain scalable data pipelines using ETL/ELT processes to collect, process, and transform data from various sources
Customer engagement: Work with customers to understand key metrics needed and analyze data to provide solutions
Data modeling: Develop and optimize database schemas, data models, and data warehousing solutions
Data quality: Implement data validation and quality checks to ensure data integrity throughout the pipeline
Documentation: Create and maintain documentation for data processes, pipelines, and architectures
Engineering Support: Monitor, troubleshoot, and optimize data systems for performance, reliability, and cost-efficiency
Data automation: Automate routine data operations and establish monitoring systems for data flows
Requirements
3+ years of experience in data engineering or similar role
Strong programming skills in Python, SQL, and shell scripting
Experience with data processing and transformation frameworks (e.g., Apache Spark, Airflow, Kafka, DBT)
Proficiency in designing and optimizing database schemas (relational and NoSQL)
Knowledge of data warehousing solutions
Familiarity with cloud platforms (AWS, GCP, or Azure) and their data services
```

https://dataegret.com/2025/05/data-archiving-and-retention-in-postgresql-best-practices-for-large-datasets/

https://query.farm/
* relational algebra, metrics layer, datafold https://www.dataengineeringpodcast.com
entity resolution at Capp = New Product Mgmt process (Ben runs, part of product workflow)
AI in pipelines https://news.ycombinator.com/item?id=42990036

https://tower.dev/blog/building-an-open-multi-engine-data-lakehouse-with-s3-and-python
> If you haven't heard of lakehouses before, think of a data warehouse where tables are stored across many files in public cloud storage services (e.g., Amazon's S3), with the crucial metadata about these tables (for example, which files contain the table's data) stored near the data in the same cloud bucket.
> use Spark and Snowflake simultaneously but for different workloads (the typical split is Spark for ML workloads and Snowflake for everyone who prefers SQL).

* _24_: try harlequin, lots of rf
* _22_: basic xsv/miller/Pandas
* _21_: put together basic data eng notes
* _18_: find visidata

> taxonomy: backup/replicate part of pipelines?
* streaming, backups https://github.com/shayonj/pg_flo
* https://www.cs.cmu.edu/~pavlo/blog/index.html
* https://github.com/bytebase/bytebase
* https://ngrok.com/blog-post/how-we-built-ngroks-data-platform https://github.com/amalshaji/portr
* https://www.youtube.com/@jayzern/videos
* Arrow partitioning https://r4ds.hadley.nz/arrow#partitioning
* NYC taxi dataset, Parquet https://duckdb.org/2021/12/03/duck-arrow.html https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page https://tech.marksblogg.com/billion-nyc-taxi-rides-redshift.html https://iceberg.apache.org/spark-quickstart/#creating-a-table https://mattpo.pe/posts/sql-llvm/
* 📻 Macey https://softwareengineeringdaily.com/2019/07/23/data-engineering-with-tobias-macey/ https://www.dataengineeringpodcast.com/six-year-retrospective-episode-361
* course https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb https://r4ds.hadley.nz/
* start with data eng https://uwekorn.com/2019/10/19/taking-duckdb-for-a-spin.html https://adamdrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html facets https://datasette.io/for/exploratory-analysis plugins https://datasette.io/tools https://datasette.io/plugins Timescale https://aliramadhan.me/2024/03/31/trillion-rows.html https://www.freecodecamp.org/learn/data-analysis-with-python/#data-analysis-with-python-course https://www.youtube.com/watch?v=v65n9yQWfVs https://www.youtube.com/watch?v=qowFCmaNFp4
* https://www.thenile.dev/blog/things-dbs-dont-do
* Conery + query sandbox https://tedconbeer.com/ https://github.com/ankane/blazer
* https://news.ycombinator.com/item?id=40488844&utm_term=comment
* datagolf https://datagolf.com/tour-standings https://datagolf.com/field-updates https://datagolf.com/datagolf-rankings https://datagolf.com/api-access
> https://www.linkedin.com/in/matthew-courchene-2a19587b/ https://www.globalgolfpost.com/featured/data-gold/ https://www.sloansportsconference.com/people/matthew-courchene https://golf.com/news/features/data-golf-analytics-new-level-pay-attention-gamblers/ https://twitter.com/DataGolf/status/1779890636537094231
> read on sports better, stats
* steampipe https://news.ycombinator.com/item?id=40343131 OS metrics queryable from SQL https://github.com/osquery/osquery
* https://news.ycombinator.com/item?id=39338626
* https://news.ycombinator.com/item?id=37222191
* https://news.ycombinator.com/item?id=35478240
* https://www.ssp.sh/brain/data-engineering/

ROLES
* _data scientist_: analytics
> data scientist's job is to launder management's intuition using quantitative methods https://news.ycombinator.com/item?id=34694926
* _data engineer_: shepard (ETL) librarian (catalog) https://www.youtube.com/watch?v=qqlbYDfqeI4 1:45
> But if data analytics usually means extracting insights from existing data, data engineering means the process of building infrastructure to deliver, store and process the data. https://khashtamov.com/en/how-to-become-a-data-engineer/
* vs. web dev https://tech.marksblogg.com/is-hadoop-dead.html
> The above projects often aren't advertised in a way that web developers would be exposed to them. This is why someone could spend years working on new projects that are at the bottom of their S-curve in terms of both growth and data accumulated and largely never see a need for data processing outside of what could fit in RAM on a single machine.
> Web Development was a big driver in the population growth of coders over the past 25 years. Most people that call themselves a coder are most often building web applications. I think a lot of the skillsets they possess overlap well with those needed in data engineering but often distributed computing, statistics and storytelling are lacking.
> Websites often don't produce much load with any one user and often the aim is to keep the load on servers supporting a large number of users below the maximum hardware thresholds. The data world is made up of workloads where a single query is trying its best to maximize a large number of machines in order to finish as quickly as possible while keeping the infrastructure costs down.
> Companies producing PBs of data often have a queue of experienced consultants and solutions providers at their door. I've rarely seen anyone plucked out of web development by their employer and brought into the data platform engineering space; it's almost always a lengthy, self-retraining exercise.

# 🦆 DUCKDB

📜 https://duckdb.org/docs/
📚
* Needham https://www.manning.com/books/duckdb-in-action
* https://realpython.com/python-duckdb/ https://www.amazon.com/DuckDB-Running-Fast-Analytics-Reporting-ebook/dp/B0DPNMF2ZX

result set hot reload https://motherduck.com/blog/introducing-instant-sql/ https://news.ycombinator.com/item?id=43782406
motherduck https://news.ycombinator.com/item?id=43705991

SETUP
* install: Homebrew
* config fs: `$HOME/.duckdbrc`
* extensions
```sh
INSTALL sqlite;  # $HOME/.duckdb/extensions
```

## CLI

ZA
* from-first syntax https://duckdb.org/docs/sql/query_syntax/from.html#from-first-syntax
* commands https://duckdb.org/docs/api/cli/overview.html
* ❌ no Vim support https://github.com/duckdb/duckdb/issues/4811 https://github.com/antirez/linenoise/pull/92

EDA
```sh
.tables
.databases
.schema $TABLE
```

LOAD https://duckdb.org/docs/data/csv/overview.html
```sh
# create db
duckdb stat-explore.db

# create table in db
CREATE TABLE signups AS SELECT * FROM 'signups.csv'
.import $CSV $TABLE

# set as default db
.open path/to/stat-explore.db

# https://github.com/duckdb/duckdb?tab=readme-ov-file#data-import
SELECT * FROM 'myfile.csv';
SELECT * FROM 'myfile.parquet';
```

---

> was this not working on my work machine due to my user config re: default db?

```sh
duckdb mydb.duckdb

-- Create a table named 'table1' from file1.csv
CREATE TABLE table1 AS SELECT * FROM read_csv_auto('path/to/file1.csv');

-- Create a table named 'table2' from file2.csv
CREATE TABLE table2 AS SELECT * FROM read_csv_auto('path/to/file2.csv');

SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;
```

## design

alternative https://github.com/BemiHQ/BemiDB
https://labs.quansight.org/blog/duckdb-when-used-to-frames_part2
https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html

* design: columnar
* data sources: CSV, Excel, Google Sheets, Parquet, S3, Postgres, SQLite, Iceberg https://duckdb.org/docs/data/data_sources.html https://duckdb.org/community_extensions/extensions/gsheets.html

---

* C++ devs https://news.ycombinator.com/item?id=43342712
> DuckDB is a single file SQL database. https://csvbase.com/blog/6
> DuckDB is a new analytical data management system that is designed to run complex SQL queries within other processes. DuckDB has bindings for R and Python, among others. DuckDB can query Arrow datasets directly and stream query results back to Arrow. This integration allows users to query Arrow data using DuckDB's SQL Interface and API, while taking advantage of DuckDB's parallel vectorized execution engine, without requiring any extra data copying. Additionally, this integration takes full advantage of Arrow's predicate and filter pushdown while scanning datasets. https://duckdb.org/2021/12/03/duck-arrow.html
* interop btw other databases https://duckdb.org/2024/01/26/multi-database-support-in-duckdb.html
* role in ecosystem https://wesmckinney.com/blog/looking-back-15-years/
* for analytics https://news.ycombinator.com/item?id=24531085 https://news.ycombinator.com/item?id=23287278
* own flavor of SQL https://duckdb.org/2022/05/04/friendlier-sql.html
* BigFrame = BigQuery for dataframes https://www.youtube.com/watch?v=R6RYEKC0gW0 https://github.com/googleapis/python-bigquery-dataframes
* https://news.ycombinator.com/item?id=39141652
* https://www.nikolasgoebel.com/2024/05/28/duckdb-doesnt-need-data.html
* https://www.youtube.com/watch?v=yi2zgenIZm4
* https://pycon-archive.python.org/2024/schedule/presentation/130/index.html
* https://changelog.com/news/big-data-is-dead-analytics-is-alive-LGl0
* https://softwareengineeringdaily.com/2024/08/08/duckdb-with-hannes-muhleisen/
* https://www.youtube.com/watch?v=MCa0fAyfiRM
* https://www.youtube.com/watch?v=JoVHITW_WeE
* https://tech.marksblogg.com/duckdb-1b-taxi-rides.html
* https://softwareengineeringdaily.com/2022/03/18/duckdb-with-hannes-muleisen/
* https://softwaredaily.wpenginepowered.com/wp-content/uploads/2022/03/SED1439-DuckDB-with-Hannes-Muhleisen.pdf
* https://kadekillary.work/note/duckdb/
* https://tech.marksblogg.com/popular-airline-passenger-routes-2023.html

## lib

* query dataframes
```python
import duckdb
import pandas as pd
df = pd.DataFrame(pd.read_csv($FILE))  # create df
con = duckdb.connect()  # connect to DuckDB
con.register("my_df", df)  # register df with DuckDB
my_query = """ SELECT * FROM my_df """  # use registered df in query
query_res = con.execute(my_query).df()  # exec query
query_res.to_parquet('file/path.parquet')  # save
```

## ✰ Spark

= distributed compute, back when big data was a buzzword and before Polars and DuckDB made it tenable to do stuff on a single node

---

```txt
Query Engine:
* Focused on SQL parsing, planning, and execution
* Input: SQL or similar declarative query language
* Output: Query results
* Example: When you write "SELECT * FROM table WHERE x > 10", it figures out how to get those records efficiently

Compute Engine:
* Lower-level framework for distributed data processing
* Input: Custom program logic (like MapReduce jobs, data transformations)
* Output: Transformed datasets
* Example: When you write custom functions to process each record, orchestrate shuffles between nodes, etc.
```

Spark/Dask: Built to process data across many machines
Pandas/DuckDB: Run on single machine

Dask dataframe https://www.youtube.com/watch?v=bbtK3aCQ3C0 Ray https://github.com/ray-project/ray

alternative https://github.com/marsupialtail/quokka 
https://www.amazon.com/gp/product/1098103653
https://www.amazon.com/gp/product/1617297208
https://www.amazon.com/gp/product/1492045527

BASICS
* _Spark_: Pandas + distributed
* RDD = collection of obj https://www.youtube.com/watch?v=XrpSRCwISdk [3:30]
* dataframe = table https://www.youtube.com/watch?v=XrpSRCwISdk [3:30]
* similar interface as Pandas https://www.youtube.com/watch?v=XrpSRCwISdk [10:20]
* architecture: driver/lib -> executor -> operates on data https://www.youtube.com/watch?v=XrpSRCwISdk [5:10]
* used for ML https://tech.marksblogg.com/is-hadoop-dead.html
* _pyspark_: Python API to Spark https://www.youtube.com/watch?v=XrpSRCwISdk https://spark.apache.org/docs/latest/api/python/index.html

# ⭕️ FACTORS

🗄️ `data/modeling.md` factors
📚
* Kleppmann [90-95]
* Serra https://www.amazon.com/Deciphering-Data-Architectures-Warehouse-Lakehouse/dp/1098150767

```txt
Query Engines:
Don't own storage - read from external sources (S3, HDFS, etc)
Optimize for: Query planning, distributed execution, reading different formats
Examples: Presto, Trino, DataFusion

Data Warehouses:
Own the storage layer
Optimize for: Data layout, indexing, compression
Deeply integrate storage and compute layers
Examples: Snowflake, BigQuery, Redshift

Real-world impact:

Data loading
* Warehouse: Must load data first, but then very fast
* Query engine: Can query data in place, but performance depends on source format/location

Cost model
* Warehouse: Pay for storage + compute
* Query engine: Pay for compute only (storage cost is elsewhere)

Query optimization
* Warehouse: Can optimize storage layout for query patterns
* Query engine: Limited to optimizing the query itself
```

https://dbdb.io/ https://nchammas.com/writing/database-access-patterns
* data structures e.g. relational, document
* scale e.g. single node, distributed
* storage e.g. relational, column store
* consistency guarantee
* transaction isolation 🗄 `system.md` transactions
* _temporality_: real-time vs. historical 📻 Macey 8:30
* _embedded_: https://en.wikipedia.org/wiki/List_of_in-memory_databases https://www.openmymind.net/2011/2/10/Do-Relational-Database-Vendors-Care-About-Devs/
* _client-server_: when you have multiple clients (vs. multithreaded) or need thousands of writes/second https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html

> Every company I worked at prior to Stripe built huge walls around their data warehouse. This resulted in a severely limited flow of information through the organization, forcing teams to use their intuition more than data analysis, since the data team would always have a miles-long backlog of requests to fulfill. Stripe is the fist place I've worked where the data warehouse is open to everyone to query and extract information that is relevant to their job. Of course, there are still strict access controls and auditing around company data, but access to relevant datasets are granted by default to team members. https://steinkamp.us/posts/2022-11-10-what-i-learned-at-stripe

## storage

* _data source_: where you're getting the data https://dataschool.com/data-governance
* _hot storage_: in-mem
* _cold storage_: analytics, archives https://github.com/tembo-io/pg_tier
* _data tiering_: moving cold data to (cheaper) cold storage https://github.com/tembo-io/pg_tier

## schemas

💻
* `data/modeling.md` factors, name spaces
* `sql.md` canonical

* _fact table_: transactions w/ many FK to other dimensions 📙 Kleppmann [93,95]
* _dimension_: non-transactional tables 📙 Kleppmann [94] https://tech.marksblogg.com/data-fluent-for-postgresql.html
* _star schema_: fact table at center
* _snowflake schema_: like star schema but more normalized, less popular bc harder to query 📙 Kleppmann [95]

## size

* MB = Excel, nGB-1TB = Postgres, >5TB = Hadoop https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html
* typical dbms can fit 100M records in single table https://news.ycombinator.com/item?id=36038321
* _big data_: can't fit into normal dbms
* _small data_: can fit on a phone (so, half a terabyte) https://simonwillison.net/2021/Jul/22/small-data/
* complete works of Shakespeare only 5.5 MB 📙 Conery [345]
* ways of thinking about data sizes: 1MB vs. 1M seconds (12 days) 1GB vs. 1B seconds (31 years) 1TB vs. 1T seconds (317 centuries) 📙 Conery [345]
> the term Big Data is so over-used and under-defined that it is not useful in a serious engineering discussion. 📙 Kleppmann 1.9
> There are diminishing returns to the amount of information you can extract from data. The tenth gigabyte is worth much less than the second gigabyte. https://www.evanmiller.org/small-data.html

## OLTP

> If you have a transactional need for your dataset it's best to keep this workload isolated with a transactional data store. This is why I expect MySQL, PostgreSQL, Oracle and MSSQL to be around for a very long time to come. https://tech.marksblogg.com/is-hadoop-dead.html
* data: application
* access pattern: writes 📙 Kleppmann [90]
* schema: DIY
* model: relational
* consumers: users

## OLAP

> But would you like to see a 4-hour outage at Uber because one of their Presto queries produced unexpected behaviour? Would you like to be told your company needs to produce invoices for the month so the website will need to be switched off for a week so there are enough resources available for the task? Analytical workloads don't need to be coupled with transactional workloads. You can lower operational risks and pick better-suited hardware by running them on separate infrastructure. https://tech.marksblogg.com/is-hadoop-dead.html
* data: from n data sources (application, analytics) 📙 Kleppmann [92]
* access pattern: reads (aggregates) 📙 Kleppmann [90-92] 🗄 `sql.md` tables/views
* schema: star
* model: maybe non-relational 📙 Kleppmann [93,101]
* consumers: DBA, BI, ML https://softwareengineeringdaily.com/2021/07/14/data-science-on-aws-implementing-ai-and-ml-pipelines-on-aws-with-chris-fregly/

# 🌊 PIPELINE

📙 Cayla https://www.manning.com/books/data-preparation-handbook
🗄
* `data/sql.md` migrations
*️ `sql.md` schema / approaches
* `infra.md` task queue, workflow engine

---

* https://2025.djangocon.us/talks/what-would-the-django-of-data-pipelines-look-like/
* Linq https://github.com/EntilZha/PyFunctional
* Bruin, Cue https://news.ycombinator.com/item?id=42442812
* https://www.youtube.com/watch?v=kGT4PcTEPP8
* https://sre.google/sre-book/table-of-contents/ chapter 26
* clean up https://news.ycombinator.com/item?id=34578324 https://en.wikipedia.org/wiki/Instruction_pipelining https://joblib.readthedocs.io/en/latest/index.html https://news.ycombinator.com/item?id=34578324 https://arpit.substack.com/p/how-grab-stores-and-processes-millions https://news.ycombinator.com/item?id=34483402 visidata https://www.visidata.org/blog/2020/ten/
* mv/copy from one db to another https://news.ycombinator.com/item?id=39525071 https://github.com/bruin-data/ingestr
* _transform_: 名 step that remodels data to dimensionsal https://www.youtube.com/watch?v=M8oi7nSaWps 3:30 https://news.ycombinator.com/item?id=34578324
* e.g. head/tail, add/rm col, type conversion, join https://www.youtube.com/watch?v=llRLh8cM7QI 15:50
* _ETL_: mv fact tables to dimensionsal 📙 Conery 323
* howto https://www.youtube.com/watch?v=v65n9yQWfVs
* _ELT_: cp facts tables, then mv to dimensionsal https://www.youtube.com/watch?v=voC0ewDeltA 4:00 https://dlthub.com/
* howto https://docs.meltano.com/getting-started/meltano-at-a-glance
* allows analysts to do the transformations they need vs. having to figure it out up front https://www.youtube.com/watch?v=qqlbYDfqeI4 7:00

## clean

🗄️
* `languages.md` R / tidyverse
* `python/core.md` pydantic

* _Autolabel_: https://github.com/refuel-ai/autolabel https://www.youtube.com/watch?v=TjzeaHjmiGM
* _Cleanlab_: https://github.com/cleanlab/cleanlab https://www.youtube.com/watch?v=QHaT_AiUljw

---

https://www.crunchydata.com/blog/validating-data-types-from-semi-structured-data-loads-in-postgres-with-pg_input_is_valid
* _OpenRefine_: https://openrefine.org/ https://www.youtube.com/watch?v=yjLIRNpc2RQ

* https://blog.codepen.io/2023/02/01/399-data-munging/
* unstructured https://news.ycombinator.com/item?id=41236273
* anonymize/differential privacy https://www.youtube.com/watch?v=PC0bF5tstvI

SANITIZATION https://codex.wordpress.org/Validating_Sanitizing_and_Escaping_User_Data
* https://developer.wordpress.org/apis/security/sanitizing/ https://developer.wordpress.org/apis/security/data-validation/ https://developer.wordpress.org/apis/security/escaping/
* https://github.com/pyjanitor-devs/pyjanitor
* URL: urllib, urlparse https://github.com/gruns/furl
* _validation_: compare against rules (email, IP address) https://martinheinz.dev/blog/96
* _filter_: rm validation violations
* _escape_: convert validation violations
* _sanitize_: validate + filter/escape
* _parameterize_: sanitization for SQL https://security.stackexchange.com/a/143925

## CDC

* _CDC (change data capture)_: realtime detect changes in src system (rather than re-reading whole table on a schedule)
* traditional ETL for OLAP = run a nightly job to query the whole src table and copy it to a warehouse
* CDC = only stream diff what changed = lower latency/load

---

* impl: Postgres -> Kafka -> Snowflake

## 🐠 DBT

📜 https://github.com/dbt-labs/dbt-core

= tool for transforms https://www.youtube.com/watch?v=l48zwwRSGeA [6:15]

---

* Piperider https://github.com/InfuseAI/piperider https://www.youtube.com/watch?v=03MyOkIo8Hg https://www.youtube.com/watch?v=O-tyUOQccSs
* workflow https://www.youtube.com/watch?v=qqlbYDfqeI4 11:00-11:15
* for unstructured https://news.ycombinator.com/item?id=42043948
* plain text vs. crappy GUI tools for analysts https://www.youtube.com/watch?v=M8oi7nSaWps 5:45 https://www.youtube.com/watch?v=qqlbYDfqeI4 9:40
* https://www.youtube.com/watch?v=UVI30Vxzd6c https://www.youtube.com/watch?v=4eCouvVOJUw https://www.youtube.com/watch?v=iMxh6s_wL4Q
* why: schema introspection, testing https://highgrowthengineering.substack.com/p/why-is-dbt-so-important- https://news.ycombinator.com/item?id=33846087
> modern data stack of Fivetran + dbt + Snowflake https://luttig.substack.com/p/dont-forget-microsoft
* create views via ETL in Snowflake (at UM)
* data ingestion from Snowflake using Snowpipe https://docs.snowflake.com/en/user-guide/data-load-snowpipe-intro.html
* util https://github.com/dbt-labs/dbt-utils
* metrics https://news.ycombinator.com/item?id=30938109

ALTERNATIVES
* _Amphi_: https://github.com/amphi-ai/amphi-etl
* _Airbyte_: pull from data source https://www.youtube.com/watch?v=l48zwwRSGeA https://www.youtube.com/watch?v=bXql-XSwD_s
* _bonobo_: 💀 https://github.com/python-bonobo/bonobo https://www.pythonpodcast.com/bonobo-with-romain-dorgueil-episode-143/
* _amphi_: https://github.com/amphi-ai/amphi-etl https://news.ycombinator.com/item?id=40723356
* _Bytebase_: https://github.com/bytebase/bytebase
* _bruin_: ⭐️ https://github.com/bruin-data/bruin
* _DLT_: https://github.com/dlt-hub/dlt https://www.youtube.com/watch?v=eMbhyOECpcE
* _petl_: transforms https://petl.readthedocs.io/en/stable/
* if petl can only handle thousands of records, why not just use Pandas? https://www.youtube.com/watch?v=llRLh8cM7QI 9:30 25:00
* _Prefect_: https://www.youtube.com/watch?v=W-rMz_2GwqQ https://www.youtube.com/playlist?list=PL3MmuxUbc_hKqamJqQ7Ew8HxptJYnXqQM https://www.youtube.com/watch?v=ISLV9JyqF1w
* _Tobiko_: https://tobikodata.com/ https://tobikodata.com/tobiko-acquires-quary.html

## 🍞 miller

🗄️ `os/tools.md` string processing
📜 https://miller.readthedocs.io/en/latest/glossary https://miller.readthedocs.io/en/latest/reference-verbs/

PIPELINES
```sh
cat $CSV | mlr --csv put '$col = int($col)' > $CSV  # cast type from int to float
filter 'is_null($col)' $CSV                         # filter nulls https://miller.readthedocs.io/en/latest/reference-dsl-builtin-functions/
filter '$header != ""' $CSV                         # filter out nulls
mlr --csv filter '$col != ""' $CSV                  # filter out empty strings
mlr --csv filter '$price_list != ""' final.csv
mlr --csv filter '$price_list != ""' final.csv
mlr --csv filter '$price_source != ""' then filter '$mpn_score == 100' $CSV  # chained
```

CONFIG https://miller.readthedocs.io/en/latest/customization/
* `$HOME/.mlrrc`
```sh
--list-color-names # view colors https://miller.readthedocs.io/en/latest/output-colorization/
c2p  # --c2p
allow-ragged-csv-input  # if data line fields > header line, insert empty val instead of err (CSV header/data length mismatch)

# IO
--icsv    # input csv
--tsv     # input tsv
--opprint # output pprint
--c2p     # combine --icsv and --opprint https://miller.readthedocs.io/en/latest/keystroke-savers/#short-format-specifiers-including-c2p
--csv     # IO csv
```

---

```sh
# BASICS
cat $FILE # select *
head -n 5 $FILE # limit
sort -f $COL $FILE  # sort on col
cut -o -f "col1","col2" $FILE # select col = -o -f col
cut -x -f "col1","col2" $FILE # ignore col = -x -f co l
put '$COL1 = "foo"' then put '$COL2 = "bar"' $FILE_CURRENT > $FILE_UPDATED  # add col
head -n 20 then cut -o -f "id","artist" then sort -f "artist" $FILE # chaining

# PREDICATES, GROUPING
uniq -g <header> <csv> | wc -l # uniq for header
most-frequent -f col -n 1000 example.csv # most frequent value by header
most-frequent -f col -n 1000 example.csv | mlr --opprint sort -f col # most frequent value by header + group by header
--c2p cut -o -f "21.08","21.09" then put '${total} = ${21.08} + ${21.09}' <csv> # put = computed fields; ${field} for fields w/ spaces
filter '$header == "value"' $CSV # select * where header = val
filter '$header1 == "value-foo"' && '$header2 == "value-bar"' example.csv
filter 'is_null($header)' example.csv # https://miller.readthedocs.io/en/latest/reference-dsl-builtin-functions/
filter '$earnings > 0.0' example.csv
```

## test

---

https://www.youtube.com/watch?v=DhognqFaRow
https://github.com/akmalsoliev/Validoopsie
https://www.milesmcbain.com/posts/assertive-programming-for-pipelines/
* _data contract_: https://github.com/benrutter/wimsey
* https://pycon-archive.python.org/2024/schedule/presentation/46/index.html
* compare data across tables https://github.com/datafold/data-diff https://github.com/paulfitz/daff 
* _Pandera_: type checking for dataframes https://endjin.com/blog/2023/03/a-look-into-pandera-and-great-expectations-for-data-validation https://www.peterbaumgartner.com/blog/testing-for-data-science/ https://www.union.ai/blog-post/pandera-joins-union-ai https://www.youtube.com/watch?v=Ax4pWz6kUDw
* for Polars https://tech.quantco.com/blog/dataframely
> From there, I create v2 of the schema, which adds Checks to the columns. Checks are information we gain after exploring the data - for example, whether a column should always be positive, whether the column name should be formatted a certain way, or whether a column should only contain certain values (e.g. a bool represented as a 0/1 int). https://www.peterbaumgartner.com/blog/testing-for-data-science/
* _GX (Great Expectations)_: assert against schema https://github.com/great-expectations/great_expectations https://softwareengineeringdaily.com/2020/02/17/great-expectations-data-pipeline-testing-with-abe-gong/ https://www.youtube.com/watch?v=8K6bU_AlUb8
> If we're expecting to repetedly read in new data, I would recommend exploring Great Expectations. The killer feature of Great Expectations is that it will generate a template of tests for the data based on a sample set of data we give it, like pandera's `infer_schema` on steroids. Again, this is only a starting point for adding in future tests (or expectations), but can be really helpful in generating basic things to test. https://www.peterbaumgartner.com/blog/testing-for-data-science/
* alternatives https://github.com/socialpoint-labs/sqlbucket https://github.com/sodadata/soda-core
```python
validator.expect_column_values_to_not_be_null(column="passenger_count")
validator.expect_column_values_to_be_between(column="congestion_surcharge", min_value=0, max_value=1000)
```

## reconciliation

🗄️ `ml.md` entity recognition

* _Zingg_: entity resolution i.e. fix data integrity problems https://github.com/zinggAI/zingg

# 🔍 QUERY ENGINES

🗄️
* `aws.md` compute > Athena
*️ `data/dbms.md` query engine
* `telemetry.md` Clickhouse

* _CrateDB_: https://github.com/crate/crate https://www.youtube.com/watch?v=mGxm1WPR3O8
> Modest CrateDB clusters can ingest tens of thousands of records per second without breaking a sweat. You can run ad-hoc queries using standard SQL. CrateDB's blazing-fast distributed query execution engine parallelizes query workloads across the whole cluster.

---

= Query engines typically don't store data permanently; they pull from other sources

Focused on SQL parsing, planning, and execution
Input: SQL or similar declarative query language
Output: Query results
Example: When you write "SELECT * FROM table WHERE x > 10", it figures out how to get those records efficiently

start here https://pycon-archive.python.org/2024/schedule/presentation/109/index.html https://www.scattered-thoughts.net/writing/the-missing-tier-for-query-compilers/

SEMANTICS
> https://github.com/pola-rs/polars
> Ibis is a dataframe frontend to query engines https://ibis-project.org/
> read all his posts https://maximilianmichels.com/page/4/ https://apache.org/index.html#projects-list
> is Spark a query engine? seems like query engine + streaming + a bunch other stuff i.e. a congeries https://ibis-project.org/install
> Spark: data manipulation for ML model training https://www.reddit.com/r/apachespark/comments/16zzabh/distributed_sql_query_engine_apache_spark_vs/?rdt=45095

ALTERNATIVES
* cloud: petabytes in single query and comes back in seconds/minutes e.g. Snowflake 📻 Macey 32:20
* just use CLIs https://news.ycombinator.com/item?id=39136472
* _BigQuery_: really fast https://tech.marksblogg.com/billion-nyc-taxi-rides-bigquery.html https://dataschool.com/sql-optimization/bigquery-optimization
* _Hydra_: use Postgres https://github.com/hydradatabase/hydra
* _Postgres_: https://news.ycombinator.com/item?id=39263760 https://brandur.org/warehouse https://tech.marksblogg.com/billion-nyc-taxi-rides-postgresql.html https://news.ycombinator.com/item?id=27109960
> I've also heard arguments that row-oriented systems like MySQL and PostgreSQL can fit the needs of analytical workloads as well as their traditional transactional workloads. Both of these offerings can do analytics and if you're looking at less than 20 GB of data it's probably not worth the effort of having multiple pieces of software running your data platform. https://tech.marksblogg.com/is-hadoop-dead.html

## ☢️ DataFusion

📜 https://datafusion.apache.org/ https://github.com/apache/datafusion

* used by Logfire, no indexes https://talkpython.fm/episodes/transcript/487/building-rust-extensions-for-python

## Graft

https://simonwillison.net/2025/Apr/8/stop-syncing-everything/

## ⦊ Presto

just a way to query Iceberg https://www.youtube.com/watch?v=TsmhRZElPvM [11:45]

---

> That’s now rapidly changing; on the back-end, most modern enterprise software (e.g. Salesforce, Jira, etc.) now have good APIs for exporting data. ETL + data lakes are on the rise: Presto, for example, facilitates cross-database joins that weren’t possible just a few years ago. https://retool.com/blog/erp-for-engineers

* _Presto_: distributed query engine https://tech.marksblogg.com/presto-parquet-airpal.html https://tech.marksblogg.com/billion-nyc-taxi-rides-hive-presto.html Kafka https://tech.marksblogg.com/presto-connectors-kafka-mongodb-mysql-postgresql-redis.html
* beat out Apache Drill https://news.ycombinator.com/item?id=23250314 📙 Beaulieu [303] https://news.ycombinator.com/item?id=29063090

## 🐰 Trino

* _Trino_: https://github.com/trinodb/trino https://ibis-project.org/ https://trino.io/blog/2022/08/24/data-pipelines-production-ready-great-expectations.html

# 🏭 WAREHOUSE

BASICS
* = structured for analytics e.g. Redshift
* own the storage layer and optimize it for their query patterns
* howto: DuckDB Postgres extension https://motherduck.com/blog/postgres-duckdb-options/
> Reaching out to your PostgreSQL database and pulling in the data it needs for analysis. DuckDB essentially "scans" your PostgreSQL data remotely.
> Instead, we use the rarely-used binary transfer mode of the Postgres client-server protocol. This format is quite similar to the on-disk representation of Postgres data files and avoids some of the otherwise expensive to-string and from-string conversions. Querying Postgres Tables Directly from DuckDB https://duckdb.org/2022/09/30/postgres-scanner.html
The key insight here is that while most PostgreSQL clients use the text-based transfer mode (where data gets converted to strings and back), DuckDB uses the binary transfer mode. This is much more efficient because:

No string conversions: Data stays in its native binary format
Minimal processing: For example, to read a normal int32 from the protocol message, all we need to do is to swap byte order (ntohl) Querying Postgres Tables Directly from DuckDB – DuckDB
Format similarity: This format is quite similar to the on-disk representation of Postgres data files Querying Postgres Tables Directly from DuckDB – DuckDB

So while DuckDB is using the standard PostgreSQL wire protocol that any PostgreSQL client would use, it's specifically utilizing the binary transfer capabilities within that protocol - a feature that most database tools don't take advantage of, but which provides significant performance benefits for analytical workloads.
* _mart_: subset of warehouse; uses star schema 📙 Conery [324]

DATA MESH
* = domain teams maintain warehouse https://www.thoughtworks.com/radar/techniques/data-mesh
* 📙 https://www.manning.com/books/data-mesh-in-action https://www.amazon.com/Data-Mesh-Delivering-Data-Driven-Value/dp/1492092398
> It really feels like data mesh is a fairly half baked concept born out of short term consulting gigs and a desire to become a technical thought leader. https://news.ycombinator.com/item?id=30721198

---

* CDO https://news.ycombinator.com/item?id=37146532
* family https://news.ycombinator.com/item?id=37520374
> interesting at UM that they had an insights db, essentially a db for warehouse workloads but for the product vs. analysis
> Circa 2010, there was only one full-time analyst at the company working on data, and his laptop was effectively the company’s data warehouse. https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70
* typically different dbms from OLAP e.g. Redshift, BigQuery, Hive, Presto 📙 Kleppmann 93
* keeps more data in memory 📻 Macey 24:30
* more expensive bc optimizing for large volume and speed of access 📻 Macey 31:30

https://www.smalldatasf.com/2024
https://karenjex.blogspot.com/2024/09/optimising-your-database-for-analytics.html

> Some high level context for those less familiar with the Lakehouse storage system space. For various reasons, several companies moved from data warehouses to data lakes starting around 7-10 years ago. Data lakes are better for ML / AI workloads, cheaper, more flexible, and separate compute from storage. With a data warehouse, you need to share compute with other users. With data lakes you can attach an arbitrary number of computational clusters to the data. Data lakes were limited in many regards. They were easily corrupted (no schema enforcement), required slow file listings when reading data, and didn't support ACID transactions. https://news.ycombinator.com/item?id=34345408
* https://news.ycombinator.com/item?id=34342190
* export https://news.ycombinator.com/item?id=44758281

## Bauplan

🗄️ `OLTP.md` version control

https://news.ycombinator.com/item?id=43705991
https://www.bauplanlabs.com/

## 🔵 Bemi

built on Postgres https://bemidb.com/

## 🐿️ Crunchy

https://www.crunchydata.com/blog/incremental-archival-from-postgres-to-parquet-for-analytics

## 🌕 Clickhouse

🗄️ `eng.md` query engines
📜 https://clickhouse.com/ https://github.com/ClickHouse/ClickHouse

* design: columnar
* _chdb_: Python library (in-process) https://github.com/chdb-io/chdb

---

https://clickhouse.com/blog/postgres-to-clickhouse-data-modeling-tips-v2
https://rtabench.com/
```txt
Leaving the embedded database sphere, but sticking with the analytics theme, we come to ClickHouse. If I had to only pick two databases to deal with, I’d be quite happy with just Postgres and ClickHouse - the former for OLTP, the latter for OLAP.

ClickHouse specialises in analytics workloads, and can support very high ingest rates through horizontal scaling and sharded storage. It also supports tiered storage, allowing you to split “hot” and “cold” data - GitLab have a pretty thorough doc on this.

Where ClickHouse comes into its own is when you have analytics queries to run on a dataset too big for something like DuckDB, or you need “real-time” analytics. There is a lot of “benchmarketing” around these datasets, so I’m not going to repeat them here.

Another reason I suggest checking out ClickHouse is that it is a joy to operate - deployment, scaling, backups and so on are well documented - even down to setting the right CPU governor is covered.

Spend a week exploring some larger analytics datasets, or converting some of the DuckDB analytics from above into a ClickHouse deployment. ClickHouse also has an embedded version - chDB - that can offer a more direct comparison.
```
* https://news.ycombinator.com/item?id=42146782
* https://tech.marksblogg.com/install-clickhouse-faster.html https://tech.marksblogg.com/faster-clickhouse-imports-csv-parquet-mysql.html https://tech.marksblogg.com/billion-nyc-taxi-rides-clickhouse-cluster.html https://github.com/azat/chdig https://posthog.com/handbook/engineering/clickhouse https://clickhouse.com/docs/en/operations/utilities/clickhouse-local/ https://news.ycombinator.com/item?id=34071918 https://clickhouse.com/blog/extracting-converting-querying-local-files-with-sql-clickhouse-local https://news.ycombinator.com/item?id=24696149 https://softwareengineeringdaily.com/2021/05/17/clickhouse-data-warehousing-with-robert-hodges/ https://softwareengineeringdaily.com/2022/09/12/serverless-clickhouse-for-developers/ https://tech.marksblogg.com/billion-taxi-rides-doublecloud-clickhouse.html https://tech.marksblogg.com/install-clickhouse-faster.html https://tech.marksblogg.com/faster-clickhouse-imports-csv-parquet-mysql.html

## 🧱 Databricks

---

* _Databricks_: Spark aaS from creators of Spark; lakehouse, autoscaling, model training, interactive notebooks
* vs. Snowflake https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html
* https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html

## ❄️ Snowflake

📙 Ferle https://www.manning.com/books/snowflake-data-engineering

* _Snowflake_: users/investors like them https://news.ycombinator.com/item?id=24265041 https://dataschool.com/sql-optimization/snowflake/ https://www.youtube.com/watch?v=xojAXXRo_S0 OSS https://news.ycombinator.com/item?id=38038239
* apparently a lot faster and easier to manage than a Hadoop installation https://news.ycombinator.com/item?id=24641481 
* can build dashboards off queries
* connect locally https://www.youtube.com/watch?v=8un_rsg7l84

# ⛵️ LAKE

* = structured + unstructed for analytics 类似 file system e.g. Redshift
* what you might store in a lake: CloudWatch Logs https://www.crunchydata.com/blog/reducing-cloud-spend-migrating-logs-from-cloudwatch-to-iceberg-with-postgres

---

* https://codecut.ai/from-pandas-to-production-delta-rs/
* https://www.youtube.com/watch?v=PpGivTOyawY
* https://www.youtube.com/watch?v=V0GvZ_KAI70 https://news.ycombinator.com/item?id=32336977
* slower to access, has metadata (when was it produced, who owns it), batch writes, most reads will be humans doing analysis or exploration
* less expensive bc optimizing for large volume i.e. can use slower object storage 📻 Macey 31:30
* https://softwareengineeringdaily.com/2022/08/25/lakehouse-data-stack-with-raj-bains-2/
* _HCatalog_: https://www.cs.cmu.edu/~pavlo/blog/2025/01/2024-databases-retrospective.html
* _Deltalake_: lakehouse https://news.ycombinator.com/item?id=34345408 https://rushter.com/blog/python-code-exec/ https://delta.io/ https://github.com/delta-io/delta
* _Redshift_: warehouse https://aws.amazon.com/redshift/

## DuckLake

https://ducklake.select/
https://news.ycombinator.com/item?id=44109548

## Hadoop

---

first datalake https://www.youtube.com/watch?v=TsmhRZElPvM [1:15]

* _Hadoop_: parallelization for large data 🗄 `infra.md` EMR https://aosabook.org/en/v1/hdfs.html
* kinda part of Spark, kinda not
> At some point, the Spark community tried to distance itself from the Hadoop ecosystem. They didn't want to be seen as built on legacy software nor as some sort of "add-on" for Hadoop. Given the level of integration Spark has with the rest of the Hadoop ecosystem and given the 100s of libraries from other Hadoop projects being used by Spark I don't subscribe to the belief that Spark is its own thing. https://tech.marksblogg.com/is-hadoop-dead.html
* no one uses anymore? https://news.ycombinator.com/item?id=30595026 https://tech.marksblogg.com/architecting-modern-data-platforms-book-review.html https://tech.marksblogg.com/is-hadoop-dead.html
> Whereas Hadoop and big data targeted analytics applications, often in the data warehousing space, the low latency nature of Kafka makes it applicable for the kind of core applications that directly power a business 📙 Narkhede kafka 
* setup https://tech.marksblogg.com/hadoop-up-and-running.html
* you probably don't need it https://www.benkuhn.net/hard/
* relationship to other projects like Presto, Clickhouse https://tech.marksblogg.com/is-hadoop-dead.html
* _HDFS_: distributed file system http://aosabook.org/en/hdfs.html https://news.ycombinator.com/item?id=43716058
* pools all disks from cluster
* files replicated across nodes (not all nodes; two additional copies)
* _MapReduce_: map (split query into chunks, execute in parallel) reduce (merge results) 📙 Kleppmann 46
* map (match) reduce (group) https://www.practical-mongodb-aggregations.com/intro/history.html
* also a query language 📙 Kleppmann 46
* PRQL = alternative query language https://news.ycombinator.com/item?id=30060784

## Hudi

* _Hudi_: lakehouse https://news.ycombinator.com/item?id=34345408

## 🧊 Iceberg

🔍 email

= table format + you can run it on SQLite https://www.youtube.com/watch?v=TsmhRZElPvM [11:30]

---

DuckDB https://news.ycombinator.com/item?id=44028616 https://airport.query.farm/ https://github.com/spiceai/spiceai
https://www.youtube.com/watch?v=gUvEwBUKizo
can use as the underlying fmt for a warehouse [like Iceberg] https://www.youtube.com/watch?v=yqU0ClVuGn4
https://github.com/lakekeeper/lakekeeper
https://duckdb.org/2025/03/14/preview-amazon-s3-tables.html https://news.ycombinator.com/item?id=43401421
https://www.robinlinacre.com/recommend_duckdb/
https://grok.com/chat/ae668999-e495-430c-8f69-26182fc12746
https://tower.dev/blog/building-an-open-multi-engine-data-lakehouse-with-s3-and-python

* _table format_:
* table format = structure of files (Parquet) that make up lake https://trino.io/blog/2022/08/24/data-pipelines-production-ready-great-expectations.html
> Table formats have slowly been stealing the spotlight across the big data space as projects like Apache Hudi, Delta Lake and Apache Iceberg mature and disrupt the tried-and-tested legacy data lake technologies in use at most companies worldwide.

```txt
Let me break this down taxonomically:

Data Storage Patterns:
Data Lake: Raw storage of files (CSVs, JSONs, Parquet, etc.) in object storage like S3
Table Format: Abstraction layer on top of data lakes that adds table-like features

Key insight: Iceberg/Hudi aren't alternatives to data lakes - they're built on top of them. They solve problems that raw data lakes have:
* ACID transactions (raw data lakes can't atomically update multiple files)
* Time travel/versioning (data lakes just have files)
* Schema evolution (data lakes don't track schema changes)
* Performance optimizations like file pruning (data lakes require full scans)

Think of it like:
* Data Lake = Filesystem
* Table Format = Database-like features implemented on top of that filesystem

The pattern you probably want:
* Store raw files in your data lake
* Use Iceberg/Hudi to create curated tables from those raw files
* Query those tables using Spark/Trino/etc.
```
```txt
Let me think about this from the angle of where lake formats fit in your current stack.

Your stack is well-suited for:
* OLTP (Postgres)
* Interactive analytics (DuckDB)
* Data processing (Polars)

Lake formats like Iceberg and Hudi become relevant when you need:

Schema evolution at scale
* Your current setup requires coordinated migrations across Postgres
* Lake formats let you add/remove columns without blocking reads

Time travel / audit
* Postgres point-in-time recovery works but is heavy
* Lake formats give you this almost for free

Multi-table consistency
* If you need to ensure multiple tables are consistent at a point in time
* Lake formats handle this via atomic commits across files

Key insight: Lake formats solve problems that emerge when you outgrow a single database, especially around:
* Schema changes
* Audit requirements
* Cross-system consistency

Given your current scale (10M records), I'd say you likely don't need these yet. The overhead of managing a lake format would outweigh the benefits unless you have specific requirements around schema evolution or audit.
```
```txt
Here's the key distinction in data storage patterns:

Data Warehouse (e.g. Snowflake):
* Schema-on-write (rigid structure enforced when data is loaded)
* Optimized for SQL analytics
* Data is transformed and cleaned before storage
* Typically more expensive per TB
* Better query performance out of the box

Data Lake (e.g. S3 + Iceberg):
* Schema-on-read (flexible structure, can store raw data)
* Supports multiple access patterns (SQL, streaming, ML)
* Stores raw data, transformations happen on read
* Much cheaper per TB
* Requires more engineering to get good query performance

The patterns are converging though:

Lakehouses (Delta Lake, Iceberg) add warehouse-like features to lakes:
* ACID transactions
* Schema enforcement
* Time travel
* Optimized query performance

Modern warehouses (Snowflake, BigQuery) add lake-like features:
* External tables
* Semi-structured data support
* ML integrations

Core tradeoff: Warehouses optimize for immediate analytical value but with higher cost and rigidity. Lakes optimize for flexibility and cost but require more engineering investment.
```


built on top of Parquet
https://news.ycombinator.com/item?id=34345408
https://www.youtube.com/watch?v=cI9zu5Rk_bQ
https://www.youtube.com/watch?v=PkBApqCfNqA
https://www.youtube.com/playlist?list=PLM15UEjiveml7UnWEqqrLqbWKXSaClR2Z
https://www.youtube.com/playlist?list=PL-gIUf9e9CCtGr_zYdWieJhiqBG_5qSPa
https://www.youtube.com/watch?v=Hh1MkMBAqqI
https://www.youtube.com/watch?v=6tjSVXpHrE8
https://www.youtube.com/watch?v=nWwQMlrjhy0
https://www.youtube.com/watch?v=ifXpOn0NJWk
https://medium.com/expedia-group-tech/a-short-introduction-to-apache-iceberg-d34f628b6799
* _Iceberg_: SQL for table formats https://iceberg.apache.org/ https://www.thoughtworks.com/radar/platforms?blipid=202203012 https://news.ycombinator.com/item?id=34342190
* AWS S3 tables https://meltware.com/2024/12/04/s3-tables.html
* https://medium.com/expedia-group-tech/a-short-introduction-to-apache-iceberg-d34f628b6799
> The project [Iceberg] was originally developed at Netflix to solve long-standing issues with their usage of huge, petabyte-scale tables. It was open-sourced in 2018 as an Apache Incubator project and graduated from the incubator on the 19th of May 2020.

## mesh

https://www.manning.com/books/data-mesh-in-action

```sh
Data Management Architectures
├── Centralized
│   ├── Data Warehouse (1970s+)
│   │   └── Cloud Data Warehouse (2010s+)
│   └── Data Lakehouse (2020s+)
└── Distributed
    └── Data Mesh (2019+)
```

# 🟨 ZA

## metadata (Datahub)

🗄️ `analytics.md` TUI
📙 https://www.amazon.com/gp/product/1098138864

SEMANTICS
* _definition_: what is this data?
* _flow_: data flow through system incl storage locations
* _provenance/source/lineage_: how do we get this data?, who created + when/how
* _usage_: what is this data used for?
* _audit trail_: who reads/writes + when/how

DATAHUB 📜 https://github.com/datahub-project/datahub https://datahubproject.io/
> data lineage from source to processing to consumption. https://www.thoughtworks.com/radar/platforms/summary/datahub
* features: perms/ACL, lineage, search, notes https://chatgpt.com/share/66e4a4fd-83c4-8004-b112-7935b341365d
* fka OpenMetadata https://github.com/open-metadata/OpenMetadata

---

```txt
platform that creates a unified catalog of your data assets and their relationships. Think of it as "Google for your company's data."

Where it fits in:
* Above: Data discovery platforms (broader category)
* Alongside: Apache Atlas, Amundsen, OpenMetadata
* Below: Individual data sources (databases, warehouses, BI tools, etc.)

Key scenarios where it shines:
* Data discovery across multiple systems (finding relevant tables/dashboards)
* Data lineage tracking (understanding dependencies)
* Data governance (ownership, classifications, tags)
* Schema evolution tracking
* Usage analytics

Might be overkill if:
* Small team/data footprint
* Single data source
* No complex data lineage
```

> promising! https://github.com/zillow/intake-nested-yaml-catalog

ZA
* _catalog_: manifest (desc, location) 📻 Macey 5:15 https://data.world/solutions/product-overview/ https://softwareengineeringdaily.com/2022/12/14/the-enterprise-data-catalog/
* Collibra https://www.thoughtworks.com/radar/platforms?blipid=202203049
* OpenMetadata https://www.youtube.com/watch?v=mtUBhreZ70k

OPTIONS https://chatgpt.com/c/670d2ddc-9e9c-8004-a9a5-1852da15b853
* _Amundsen_: https://github.com/amundsen-io/amundsen
* _Atlas_: https://atlas.apache.org/
* _Marquez_: https://github.com/MarquezProject/marquez
* _OpenLineage_: https://github.com/OpenLineage/OpenLineage
