# ⛩️

## 参考

## 进步

* _20_: Flask-SQLAlchemy (pagination, 1-m w/ backrefs, Marshmallow for nested serializers)
* _19_: Flask-SQLAlchemy (FK, through table, raw SQL) SQLAlchemy (core, parameterized queries)

# 🟥 SQLAlchemy

📜 https://www.sqlalchemy.org/ http://aosabook.org/en/sqlalchemy.html

* sessions
> This is not at all how SQLAlchemy's ORM component works. In SQLAlchemy you have an object called the “session”. It basically encapsulates a transaction. However it does more. Each object is tracked by primary key in this session. As such each object only exists once by primary key. As such you can safely make a lot of queries and you never have things out of sync. When you commit the session it will send all changes at once to the database in correct order, if you rollback the session nothing happens instead. https://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
* _parameterized query_: `select foo from bar where baz = :bazid` https://docs.sqlalchemy.org/en/13/core/tutorial.html#using-textual-sql https://stackoverflow.com/a/18808942/6813490 apparently should use a session https://stackoverflow.com/a/22084672/6813490

----

* https://us.pycon.org/2024/schedule/presentation/57/index.html
* tutorial https://www.youtube.com/watch?v=5SSC6nU314c
* migrations: Alembic https://news.ycombinator.com/item?id=34549578
* https://realpython.com/python-sqlite-sqlalchemy/
* create table `create_all` https://docs.sqlalchemy.org/en/14/core/metadata.html#creating-and-dropping-database-tables
* _JSONField_: https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/
* `bulk_save_objects` doesn't seem to work when it comes to backrefs https://github.com/zachvalenta/flask-skeleton/commit/548c36088dfe595fccabeb67fa11c7254e847948#diff-c61c1bc5b0486cc6e721bee29c28fe33R17
* search expressions w/ engine https://stackoverflow.com/questions/3325467/sqlalchemy-equivalent-to-sql-like-statement

## alternatives

🗄️ `django.md` db https://github.com/GothenburgBitFactory/tasklib/

* pydantic as validation before handing over to sqlite3 https://github.com/Zaloog/kanban-tui/blob/main/src/kanban_tui/database.py
* _dataset_: 🎯 sqlite3 wrapper, good taste, not an ORM https://github.com/pudo/dataset https://dataset.readthedocs.io/en/latest/index.html 
* _encode_: 💀 https://github.com/encode/orm
* _Gino_: 💀 https://github.com/python-gino/gino
* _orator_: 💀 Active Record impl, from the guy who did Poetry https://github.com/sdispater/orator
* _Peewee_: 🎯 https://github.com/coleifer/peewee not for async https://fastapi.tiangolo.com/advanced/sql-databases-peewee/
* _piccolo_: 🎯 async, active, admin https://github.com/piccolo-orm/piccolo
* _Pony_: 🎯 https://github.com/ponyorm/pony
* _SQLmodel_: 🎯 SQLAlchemy wrapper, big enough you have to give a try https://github.com/tiangolo/sqlmodel https://pybit.es/articles/from-sql-to-sqlmodel-a-cleaner-way-to-work-with-databases-in-python/
* _sqlc_: 🎯 Golang https://github.com/sqlc-dev/sqlc https://www.youtube.com/watch?v=A_3MP_V-kB4
> You write queries in SQL. You run sqlc to generate code with type-safe interfaces to those queries. You write application code that calls the generated code.
* _Tortoise_: async, bad docs, CLI https://github.com/tortoise/tortoise-orm https://github.com/tortoise/tortoise-cli
```csv
Repository,Stars
pudo/dataset,4780
encode/orm,1781
python-gino/gino,2678
sdispater/orator,1428
coleifer/peewee,11209
piccolo-orm/piccolo,1451
ponyorm/pony,3700
tiangolo/sqlmodel,14606
sqlc-dev/sqlc,13503
tortoise/tortoise-orm,4683
```

## design

---

* https://blog.appsignal.com/2025/02/26/an-introduction-to-flask-sqlalchemy-in-python.html
* https://talkpython.fm/episodes/show/344/sqlalchemy-2.0
* https://blog.miguelgrinberg.com/post/what-s-new-in-sqlalchemy-2-0
* use something else https://danluu.com/simple-architectures/e
> SQLAlchemy...makes it hard for developers to understand what database queries their code is going to emit, leading to various situations that are hard to debug and involve unnecessary operational pain
* https://talkpython.fm/episodes/show/344/sqlalchemy-2.0
* overly complex https://news.ycombinator.com/item?id=34541452
* people hate the docs https://news.ycombinator.com/item?id=34540251 https://news.ycombinator.com/item?id=34542075 https://news.ycombinator.com/item?id=34578772 https://news.ycombinator.com/item?id=34540960
* _core_: manages connection pool and dialects (diff dbms); fine to just use core https://news.ycombinator.com/item?id=10270605
* _core - components_: engine, connection, session https://stackoverflow.com/a/42772654/6813490 event system https://www.sqlalchemy.org/features.html
* _ORM_: niceties on top of core https://www.sqlalchemy.org/features.html
* _row object_: record https://stackoverflow.com/q/1958219
* _unit of work_: writes changes all at once, similar to how Hibernate does it https://www.sqlalchemy.org/features.html
* built on PEP249 (DBAPI) https://www.python.org/dev/peps/pep-0249/
* build queries from functions https://www.sqlalchemy.org/features.html
* _not async_: even if your app framework if
* compared to Django https://apirobot.me/posts/introduction-to-sqlalchemy-orm-for-django-developers

## snippets

---

```python
###
# JOINS https://stackoverflow.com/q/19841877/6813490 https://stackoverflow.com/q/6044309/6813490
###

outer = (
    db.session.query(Artist, Song)
    .outerjoin(Song, Artist.artist_id == Song.artist_id)
    .all()
)
outer_pages = (
    db.session.query(Artist, Song)
    .outerjoin(Song, Artist.artist_id == Song.artist_id)
    .paginate()
)

inner = (
    db.session.query(Artist, Song).join(Song, Artist.artist_id == Song.artist_id).all()
)

# pull values out of result set obj https://stackoverflow.com/a/42093713/6813490
# irl you'd want to use Marshmallow for this
class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)

artists = [Artist(artist_name='Massive Attack'), Artist(artist_name='Nas')]
songs = [Song(song_name='One Love', artist_id=2), Song(song_name='One Love', artist_id=1)]

query = "select artist_name, song_name from song s inner join artist a on s.artist_id = a.artist_id where artist_name='Massive Attack'"
for x in db.engine.execute(query):
    print(x)  # ('Massive Attack', 'One Love')

@app.route("api")
def get_foo():
    query = "select col1, col2 from foo"
    rs = db.engine.execute(query).fetchall()
    marshalled_rs = [x[0, 1] for x in rs]
    return jsonify({"results": marshalled_rs})

# saving from repl https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database 'shell'
# unable to persist a record using Flask-SQLAlchemy from the Python REPL, but the same code works fine when run as a script.

# APP.PY

import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, os.getenv("DATABASE"))
db_uri = "sqlite:///" + db_path

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)

class Thing(db.Model):
    thing_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.Text)

    def __repr__(self):
        return f"id {self.thing_id} name {self.name} desc {self.description}"
    
# DB_SEED.PY

#!/usr/bin/env python
from app import db, Thing

db.drop_all()
db.create_all()
thing = Thing(name="thing1", description="thing-1-desc")
db.session.add(thing)
db.session.commit()
print(f"new thing {Thing.query.all()} \n")
```
```sh
# Running the script persists a record
$ poetry run python db_seed.py
new thing [id 1 name thing1 desc thing-1-desc]
# When I try to do the same thing from inside the Python REPL, however, the record isn't created
>>> from app import db, Thing
>>> db.drop_all()
>>> db.create_all()
>>> thing = Thing(name="thing1", description="thing-1-desc")
>>> db.session.add(thing)
>>> db.session.commit()
>>> Thing.query.all()
[]
```

## backrefs

* used for 1-M
* adds virtual column to obj from parent table that enforces constraint on child table itself https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=backref https://docs.sqlalchemy.org/en/13/orm/backref.html#linking-relationships-with-backref
```python
# PARENT
class Concert(db.Model):
    concert_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    performances = db.relationship("Performance", backref="concert")

# backref = no change to underlying table
+-----+------------+---------+---------+------------+----+
| cid | name       | type    | notnull | dflt_value | pk |
+-----+------------+---------+---------+------------+----+
| 0   | concert_id | INTEGER | 1       | <null>     | 1  |
| 1   | name       | TEXT    | 0       | <null>     | 0  |
+-----+------------+---------+---------+------------+----+

# rather, gets virtual column i.e. query run on obj creation to fetch all child obj that reference parent https://www.youtube.com/watch?v=cYWiDiIUxQc 15:20
Concert.query.get(1).performances

# CHILD
class Performance(db.Model):
    perf_id = db.Column(db.Integer, primary_key=True)
    concert_id = db.Column(db.Integer, db.ForeignKey("concert.concert_id"))

# FK = adds constraint via column on underlying table
+-----+------------+---------+---------+------------+----+
| cid | name       | type    | notnull | dflt_value | pk |
+-----+------------+---------+---------+------------+----+
| 0   | perf_id    | INTEGER | 1       | <null>     | 1  |
| 1   | concert_id | INTEGER | 0       | <null>     | 0  |
+-----+------------+---------+---------+------------+----+
# physical column reflected in ORM obj
Performance.query.get(1).concert_id  # 1
# but also gets virtual column as well
Performance.query.get(1).concert  # id 1 name Glastonbury
```

# 🟨️ ZA

## code gen

🗄️ `src.md` API

---

* https://github.com/directus/directus
* Postgrest https://github.com/PostgREST/postgrest https://news.ycombinator.com/item?id=30132947 https://github.com/prest/prest
* GraphQL https://www.graphile.org/postgraphile/ 
* query SQLite over HTTP https://news.ycombinator.com/item?id=30636796
* ROAPI https://github.com/roapi/roapi https://tech.marksblogg.com/roapi-rust-data-api.html
* Datasette https://www.youtube.com/watch?v=pTr1uLQTJNE https://www.hytradboi.com/2022/datasette-a-big-bag-of-tricks-for-solving-interesting-problems-using-sqlite
* DBCore https://github.com/eatonphil/dbcore https://notes.eatonphil.com/generating-a-rest-api-from-a-database.html
* Octo https://github.com/octoproject/octo-cli
* https://github.com/thevahidal/soul

## design

* _ORM (object-relational mapper)_: obj as frontend to relational data store
* why: dbms portability, terseness, getting data into obj https://monadical.com/posts/why-use-orm.html https://news.ycombinator.com/item?id=37118633
* why not: SQL is more durable, more help on SO, easier for complicated relationships https://news.ycombinator.com/item?id=21961214 https://eli.thegreenplace.net/2019/to-orm-or-not-to-orm/ https://sirupsen.com/stop-relying-on-your-orm-and-learn-sql https://news.ycombinator.com/item?id=36497613
* write thin DSL over ORM vs. modifying default ORM methods https://rtpg.co/2016/09/12/orms-are-scary.html
* _data mapper_: https://en.wikipedia.org/wiki/SQLAlchemy https://www.openmymind.net/2011/11/18/I-Just-Dont-Like-Object-Mappers/ 🗄️ `domain.md`
* _active record_: wrapper (row + DSL) https://www.martinfowler.com/eaaCatalog/activeRecord.html http://calpaterson.com/activerecord.html https://github.com/sdispater/orator
* ActiveRecord for Golang https://github.com/volatiletech/sqlboiler

## n+1, impendence


* _N+1 problem_: n queries (instead of single query) happening under the hood of the ORM
* _eager loading_: BYO query? https://news.learnenough.com/eager-loading

---

* _N+1 problem_: https://roadmap.sh/backend https://macwright.org/2020/05/10/spa-fatigue.html https://stackoverflow.com/q/97197/6813490 https://www.sqlalchemy.org/features.html https://tech.yplanapp.com/2016/09/26/introducing-django-perf-rec/ https://www.youtube.com/watch?v=uCbFMZYQbxE https://github.com/jmcarp/nplusone https://news.ycombinator.com/item?id=26151302 https://fly.io/blog/introducing-litefs/ https://github.com/superfly/litefs
> The 1+N database anti-pattern is common: fetch some rows from the database then re-fetch specific rows to get all the items. An ORM can hide this away and make you not realize it is happening. https://suor.github.io/blog/2023/03/26/ban-1-plus-n-in-django/

* _impedance mismatch_: difficulty of object-relational mapping [Kleppmann 1.33] multiple ways to aproach http://blogs.tedneward.com/post/the-vietnam-of-computer-science/
> In the database community it has been conventional wisdom for nearly half a century now (basically since the invention of the relational model) that in designing your database schema you should be careful to avoid any kind of redundancy. That's what database normalization theory is all about. For some unfathomable reason, the same kind of thinking is never (or almost never) applied to software construction, even though it would be as beneficial (possibly even more so) as it is for databases. So, before we countinue our discussion, it's a good idea to talk a bit about redundancy, and to explain what's so harmful about it. https://www.cell-lang.net/relations.html

## query builders

🗄️ `svc/design-patterns.md` creational > builder

* _pypika_: ✅ https://github.com/kayak/pypika https://github.com/zachvalenta/query-sandbox/blob/main/queries.py

---

* t-strings https://news.ycombinator.com/item?id=44004827
* https://news.ycombinator.com/item?id=42778151
* reverse query builder https://www.thoughtworks.com/radar/languages-and-frameworks?blipid=202203030 https://github.com/kyleconroy/sqlc https://preslav.me/2023/03/07/reasons-against-sqlc/
* https://github.com/danielenricocahall/pysqlscribe
* _query builder_: what it sounds like i.e. cares about physical tables, doesn't care about objects i.e. not an ORM https://github.com/stephenafamo/bob
* BYO https://death.andgravity.com/query-builder-how
* _aiosql_: https://github.com/nackjicholson/aiosql load sql file into Python and run queries as methods https://github.com/nackjicholson/aiosql
* _csql_: https://news.ycombinator.com/item?id=24866377
* _hashquery_: https://news.ycombinator.com/item?id=40132424 https://hashquery.dev/ https://github.com/hashboard-hq/hashquery
* _records_: just write SQL https://github.com/kennethreitz/records
* _spyql_: https://github.com/dcmoura/spyql https://news.ycombinator.com/item?id=30074787
