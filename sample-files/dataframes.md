# ⛩️

## 参考

📚
* McKinney https://wesmckinney.com/book/
* VanderPlas https://jakevdp.github.io/PythonDataScienceHandbook/

## 进步

Ibis, Narwhals, DuckDb https://labs.quansight.org/blog/duckdb-when-used-to-frames https://duckdb.org/docs/stable/sql/dialect/friendly_sql.html

# ⚙️ DESIGN

TOOLING
* _datacompy_: compare, underwhelming docs https://github.com/capitalone/datacompy https://www.thoughtworks.com/radar/languages-and-frameworks/datacompy 🗄️ `plt.md` R > SAS

ZA
* BYO https://github.com/go-gota/gota/blob/master/dataframe/dataframe.go

---

https://news.ycombinator.com/item?id=42193043
https://www.youtube.com/watch?v=cgWHPTx0wjw
https://calpaterson.com/bank-python.html
https://tibble.tidyverse.org/
https://dplyr.tidyverse.org/ https://calmcode.io/course/dplyr-verbs/introduction

TOOLING
* diff https://www.youtube.com/watch?v=5Rc9xkeHth0 https://eshsoft.com/blog/how-reladiff-works https://github.com/erezsh/reladiff
* GPU acceleration https://www.youtube.com/watch?v=86nMARKN7ho https://www.youtube.com/watch?v=Aumh3evLSKc https://www.youtube.com/watch?v=PH7ExhXYkxQ

ZA
* Dataframe Interchange Protocol, Dataframe API Standard https://ponder.io/how-the-python-dataframe-interchange-protocol-makes-life-better/ https://ponder.io/why-are-there-so-many-python-dataframes/ https://pythonspeed.com/articles/polars-pandas-interopability/

## 🦢 Ibis

📜 https://ibis-project.org/

to Jack 24.12.10 https://www.youtube.com/watch?v=8MJE3wLuFXU
> different semantics/interface than Pandas though so would assume - maybe even for simple stuff - you're not porting from Pandas but rather rewriting
> one way around the pandas/polars interop problem (and others like it) https://ibis-project.org/
> relatively new-ish but from the guy who wrote Pandas (Wes McKinney)
> SQL is the longest lasting thing that still gets used for new projects (sorry, C) but it's kinda like Bash in that it's ugly/verbose to read and harder to write than ORM/dataframe code. tons of SQL out in the world so great use case for LLMs (like regex) but Ibis a great compromise, SQL becomes akin to compiler output, you can always dig into the assembly if need be [yes, compilers output bytecode, IR, etc.] but in most cases you're can happily plug away in a much better DSL. https://www.scattered-thoughts.net/writing/against-sql

* dataframe API
* https://calmcode.io/course/ibis/introduction
* transpiles to SQL i.e. works with SQL-based query engines (BigQuery, Clickhouse, Postgres, Snowflake) https://realpython.com/podcasts/rpp/201/
* compiles to Python i. e https://talkpython.fm/episodes/transcript/462/pandas-and-beyond-with-wes-mckinney
* dataframe API that can use Polars/Pandas query engine or transpile to SQL and run against relational dbms https://talkpython.fm/episodes/show/462/pandas-and-beyond-with-wes-mckinney
* https://www.youtube.com/watch?v=C4aUG9poN6E https://us.pycon.org/2024/schedule/presentation/55/index.html

## 🐋 Narwhals

* _Narwhals_: API for dataframes https://pythonbytes.fm/episodes/show/402/how-to-monetize-your-blog https://realpython.com/podcasts/rpp/224/ https://github.com/benrutter/wimsey
> Chances are, you’ve never heard of Narwhals. That’s because it’s a tool targeted at tool builders, rather than at end users. Specifically, it allows library maintainers to support multiple dataframe libraries as inputs, without having to make any of them required. https://pola.rs/posts/lightweight_plotting/
> First up: we are completely rewriting how our Plotly.py library talks to dataframes in the 6.0 release. Instead of relying on the Pandas API, we are using Narwhals which provides an abstraction layer over several kinds of tabular data. This means faster, more efficient handling of tabular data and serious performance gains for data apps at scale. You'll notice with this change that Plotly.py no longer has to do in-memory copying when you hand it something like a Polars dataframe. https://plotly.com/blog/plotly-dash-major-release/
* imple
> Narwhals aims to be as close to zero-overhead as possible. The translation layer is designed to be so thin that it doesn't meaningfully impact performance. - Claude
```python
# simplified version backend detection
if hasattr(df, 'lazy'):  # Polars df
    return PolarsLazyFrameNamespace(df)
elif hasattr(df, 'iloc'):  # Pandas df
    return PandasDataFrameNamespace(df)
```
* projects that use: Altair, Bokeh, Plotly
* way for library authors to accomodate multiple user preferences
```python
# in some data processing library...
import narwhals as nw

def my_data_function(df):
    df = nw.from_native(df)
    result = (
        df
        .filter(nw.col('value') > 0)
        .group_by('category')
        .agg(nw.col('value').mean())
    )
    return nw.to_native(result)
```

---

* https://www.youtube.com/watch?v=r2PxJlO7_QA
* https://codecut.ai/unified-dataframe-functions-pandas-polars-pyspark/

## 🖥️ TLV

🗄️ `analytics.md` EDA
💻 https://github.com/zachvalenta/df-tlv
🧠
* https://grok.com/chat/a3efd4af-1027-4065-ba82-d0ef04c58439

* VSC Code inline values for notebooks
* w/ Rich 💻️ https://github.com/zachvalenta/capp-dataload/blob/main/load.py#L28
* https://github.com/dannywade/textual-pandas
* _Buckaroo_: https://github.com/paddymul/buckaroo
* _Data Wrangler_: ✅ https://code.visualstudio.com/docs/datascience/data-wrangler alternative https://github.com/mljar/variable-inspector
* _Dataspell_: Data Wrangler Jet Brains version https://www.jetbrains.com/dataspell/
* _dtale_: render in browser https://github.com/man-group/dtale

ways I know of visualizing a dataframe (not in a BI, "here's a pretty chart" sort of way, but just literally "let me view/scroll the data current in this dataframe"):

* dtale https://github.com/man-group/dtale
* VS Code Data Wrangler https://code.visualstudio.com/docs/datascience/data-wrangler
* BYO https://github.com/zachvalenta/capp-dataload/blob/main/load.py#L28
```python
def schema_inspect(df):
    """
    pretty print schema in a more readable fmt than df.schema
    """
    console = Console()
    table = Table(title='SCHEMA', show_header=True, header_style='bold magenta')
    table.add_column('col', style='cyan', no_wrap=True)
    table.add_column('dtype', style='green')
    for col, dtype in df.schema.items():
        table.add_row(col, str(dtype))
    console.print(table)
```

All this seems suboptimal. VS Code, eh, whatever. Seems like a more clever way would be to just have a live view on the dataframe in another terminal pane using Visidata. Visidata is Python, Polars is Python, why can't this happen?

# 🐼 PANDAS

📜 https://pandas.pydata.org/docs/
📙 McKinney data analysis https://wesmckinney.com/book/
🔍
* https://github.com/jvns/pandas-cookbook
* https://github.com/kxzk/an-embarrassment-of-pandas
* https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
* https://web.archive.org/web/20230127194856/https://scribe.citizen4.eu/pandas-illustrated-the-definitive-visual-guide-to-pandas-c31fa921a43

SEMANTICS
* _series_: rows from a single column https://www.youtube.com/watch?v=zmdjNSmRXF4 [10:00] https://pandas.pydata.org/docs/user_guide/10min.html#getting
* `name`: series header
* _index_: row number https://realpython.com/pandas-reset-index/

DESIGN
> Pandas was originally written to replace Excel in financial/econometric modeling, not as a replacement for SQL. https://news.ycombinator.com/item?id=35429555
* impl: built on NumPy arrays i.e. core operations carried out in C https://en.wikipedia.org/wiki/Pandas_(software) https://realpython.com/fast-flexible-pandas/#but-i-heard-that-pandas-is-slow
* style: method chaining https://github.com/pyjanitor-devs/pyjanitor

---

* new syntax https://labs.quansight.org/blog/pandas_expressions

PERF
* https://hakibenita.com/sql-for-data-analysis#sql-vs-pandas-performance
* https://pythonspeed.com/memory
* https://realpython.com/fast-flexible-pandas

## DML

```python
col in df.columns  # existence
df[df['id'] == 42]  # subset based on equality i.e. all rows where ID = 42
```

---

SELECT
```python
df.col   # get col https://pandas.pydata.org/docs/user_guide/10min.html#getting
df[0:3]  # get row
df.col.isin(myl) # bool for each row
df.index[df.col.isin(myl)] # row index for True bool
df.drop(df.index[df.col.isin(myl)]) # drop row indexes for rows matching list el
df.columns # all col
df[["col1", "col2"]] # n col
df.iloc[3] # get row by row index
df.iloc[3, 17] # get row by row index + col index e.g. row 3 col 17
df.iloc[[3, 42]] # get n row by row index e.g. rows 3 and 42
```

FILTER
```python
df[df['entity_id'].isin(descendants['id'])]
df.query('entity_id in @descendants.id')
```
```txt
Let's break down how query() with the @ prefix works:

The query string 'entity_id in @descendants.id' is a pandas query expression
@ tells pandas to look for the variable in the Python namespace, outside the DataFrame
So @descendants.id refers to the id column/attribute of a descendants DataFrame/object that exists in your code

Without @, pandas would look for descendants.id inside the DataFrame you're querying. With @, it looks in the outer scope.
```

```python
# ITERATION https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas https://stackoverflow.com/questions/50267185/iterate-over-pandas-series don't iterate https://realpython.com/pandas-iterate-over-rows/
for series in df.iterrows():

# PREDICATE
df[df["company"] == "ABC corp"]  # equality
df[df["earnings"] > 0]  # comparison
df[(df["col1"] >= 1) & (df["col1"] <=1 )]  # uses indexing https://stackoverflow.com/a/13616382

# GROUPING 📙 McKinney [291]
for gk, grp in df.groupby("isrc"):

# CSV PER GROUP https://stackoverflow.com/a/50818244
df = pd.DataFrame(pd.read_csv("paintings.csv"))
path = os.path.join(os.getcwd(), "output_dir")
for i, (name, group) in enumerate(df.groupby("ARTIST")):
    group.to_csv("{}/{}.csv".format(path, name.replace(" ", "").lower()))

# VERIFY TOTALS PER GROUP
invalid = list()
for _, (foo, group) in enumerate(df.groupby("foo")):
    if int(group["bar"].sum()) != 100:
        invalid.append(foo)
log.info("foo count - invalid: {}".format(len(invalid)))

myl = [foo, bar]

# SHAPE https://stackoverflow.com/a/35523946
df.shape[0]  # count rows
df.shape[1]  # count col

# PERSIST FOO W/ VALID BAR
verified = df.drop(df.index[df.foo.isin(invalid)])
log.info("count - verified: {}".format(len(set(verified.foo))))
verified.to_csv(os.path.join(os.getcwd(), out_file))
```

## IO

BASIC
```python
pd.read_parquet()  # requires pyarrow https://github.com/zachvalenta/capp-denv-logs/commit/d9867cba016fea23b439687dafadf7540c35aa8a

pd.DataFrame(pd.read_csv(fpath))
pd.DataFrame(pd.read_csv(fpath), nrows=1000)  # sample on read

psub = pd.read_csv(
    'zvdata/psub_sales.csv',
    usecols=['full_ord_id', 'product_id', 'psub_id', 'unit_price', 'unit_cost'],
    dtype={'product_id': int}
)

get_sample(df, frac=0.1, random_state=42)  # reproducible 10% sample
df.to_csv(fpath, index=False)  # drop index
```

COLUMN SELECTION/CREATION
```python
# CHOOSE
pd.read_csv(fpath, usecols=['col1', 'col2', 'col3'])
# SET ORDER
df = df[['col1', 'col2', 'col3']]
# MV NAMES
df = (
    pd.read_csv()
    .rename(columns={'manufacturer': 'mfg', 'manufacturer_part_number': 'mpn'})
)
df.rename(columns={
    'old1': 'new1',
    'old2': 'new2'
}, inplace=True)
```

REASSIGN W/IN COLUMN
> ❓️ cleaner to do this with iloc?
```python
df = (
    pd.read_csv()
    .assign(csn=lambda df: 'CS' + df['id'])
)

df = df.assign(id=lambda x: x['id'].mask(x['id'] == 42, 13))

def reassign(df, condition=42):
    mask = df['id'] == condition
    transformed_values = df['id'].copy()
    transformed_values[mask] = transformed_values[mask] * 2
    return df.assign(id=transformed_values)
```

NULLS
* considered null: `None`, `np.nan`, empty string (depending on type)
* afaik there's no way to filter *in* nulls on file load
```python
# DROP W/IN COL
pd.read_csv(fpath).dropna(subset=['foo'])
pd.read_csv(fpath, na_filter=True, subset=['foo'])
# DROP ACROSS COLS
df = pd.read_csv(fpath).dropna()
```

TYPING
```python
# CASTING
pd.read_csv(fpath, dtype={'foo': str})
# DROP DUPES W/IN COL
drop_duplicates(subset=['foo'])
```

---

* failed attempt to get VS Code Jupyter extension stdout to be userful
```python
def rtbl(df, title="Debug Output"):
    """Render Pandas DataFrame as an HTML table using tabulate."""
    if df.empty:
        print(f"{title}: (Empty DataFrame)")
        return
    # Generate tabulate HTML table
    html_table = tabulate(df, headers="keys", tablefmt="html")
    # Wrap it inside a scrollable div for better display in Jupyter
    styled_table = f"""
    <div style="overflow-x: auto; max-width: 100%;">
        <h4 style="font-family: sans-serif;">{title}</h4>
        {html_table}
    </div>
    """
    display(HTML(styled_table))  # ✅ Ensures Jupyter renders it correctly

df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
rtbl(df, title="User Data")
```

# 🐻‍❄️ POLARS

📜 https://docs.pola.rs/ https://docs.pola.rs/api/python/stable/reference/index.html
📙 https://realpython.com/polars-python/


---

transpile to Pandas
> Bridging and Comparing Polars with Other Libraries Converting between Pandas, Dask, or other DataFrame libraries is straightforward: Polars has built-in to_pandas() and from_pandas() methods. Tools like Narwhal help you partially automate or unify code to run across multiple DataFrame frameworks. This portability lowers the barrier to switching from one library to another, letting you test Polars' speed benefits without major rewrites. https://talkpython.fm/episodes/show/510/10-polars-tools-and-techniques-to-level-up-your-data-science

dealing with nulls https://realpython.com/polars-missing-data/
https://www.emilyriederer.com/post/py-rgo-2025/

BIG PICTURE
* query engine with dataframe frontend https://pola.rs/posts/polars_birds_eye_view/ https://blog.jetbrains.com/pycharm/2024/07/polars-vs-pandas/
* compared to Pandas: query optimization, group by https://labs.quansight.org/blog/dataframe-group-by https://pola.rs/posts/benchmarks/
* https://www.youtube.com/watch?v=q3o2IdFQTOE
* https://news.ycombinator.com/item?id=35429555
* better semantics than Pandas? https://arilamstein.com/blog/2024/09/04/why-im-switching-to-polars/
* https://calmcode.io/course/polars/introduction
* https://calmcode.io/course/pandas-pipe/introduction

INTEROP
* converting Pandas to Polars https://www.youtube.com/watch?v=B2Ljp2Fb-l0
* can use some Pandas libraries https://pythonspeed.com/articles/polars-pandas-interopability/

PRO / CON
* better than Pandas: query in Python or SQL, no dependencies, sensible pip install (vs. conda) https://github.com/pola-rs/polars better perf https://pola.rs/posts/benchmarks/ less memory usage https://pythonspeed.com/articles/polars-memory-pandas/
* worse than Pandas: not meant for Excel-like operations
> Pandas was originally written to replace excel in financial/econometric modeling, not as a replacement for sql. Models written solely in the long relational style are near unmaintainable for constantly evolving models with hundreds of data sources and thousands of interactions being developed and tuned by teams of analysts and engineers. https://news.ycombinator.com/item?id=35429555

ZA
* Deltabase, DeltaDB https://github.com/uname-n/deltabase https://pythonbytes.fm/episodes/show/397/so-many-pycon-videos
* plotting https://pola.rs/posts/lightweight_plotting/ https://realpython.com/python-news-october-2024/
> couldn't get this to work; try `pipx inject`

## read

🗄️
* `architecture.md`
* `data/internals.md` query engine > query plan

WORKING AROUND GOOFY DATA
```python
# TSV
safe_load = {
    'schema_overrides': {
        'height': pl.Utf8,
        'upc': pl.Utf8,
    },
    'ignore_errors': True,
    'truncate_ragged_lines': True,
    'quote_char': None,
    'infer_schema_length': 10000,
}
pl.read_csv(fpath, separator='\t', encoding='latin-1', skip_rows=8, **safe_load)
pl.read_csv('neuco-feed.tsv', separator='\t')

# malformatted column headers
no_whitespace_or_period_delimit = r"^[^\s.-]+$"
violations = [col for col in df.columns if bool(re.match(no_whitespace_or_period_delimit, col)) is False]
assert len(violations) > 0
```

READ / SCAN / STREAM
> Unlike traditional DataFrames, LazyFrames don’t contain data but instead store a set of instructions known as a query plan. Query plans perform operations like predicate and projection pushdown, ensuring only necessary rows and columns are processed. LazyFrames also support the parallel execution of query plans, further enhancing performance...Lazy evaluation in LazyFrames optimizes query plans before data materialization...You create a LazyFrame using functions like scan_parquet() or scan_csv(). https://realpython.com/polars-lazyframe/
```python
# READ faster when you can skip entire columns and save on overhead of setting up query plan
df = pl.read_csv(file, columns=['col1', 'col2'])
# SCAN creates lazy df = build up ops before actually loading data = can optimize query plan rather than executing ops sequentially
df = pl.scan_csv(file)
   .filter(pl.col('col1') > 0)
   .select(['col1', 'col2'])
   .groupby('col1').agg(pl.col('col2').mean())
   .collect()
# STREAM for lower memory consumption
for chunk in pl.read_csv("data.csv", rechunk=True).iter_chunks(size=10000):
    process_chunk(chunk)
```

---

type inference (for Pandas, at least) can override user-defined column data types? https://claude.ai/chat/884d6772-1fcb-44e1-ac03-243e1ca60cde

Pandas: Most filtering happens after load
Polars: Can push many operations down to the scan/read level
* NULL checks
* Column selection
* Type inference
* Predicate pushdown

CONVERSION
* strategy pattern for `.read_csv|parquet|excel` (excel requires `fastexcel`)
```python
# convert pandas
pl.from_pandas(df)
```
```python
# get value of cell (errs if more than one value)
pdr_for_brand['sku-prefix'].item()

# alias on read
pl.scan_csv('products.csv').select([
    pl.col('capp_stock_number').alias('csn'),
    pl.col('manufacturer_part_number').alias('mpn'),
]).collect()

```

## EDA

```python
# get schema w/out full table load
pl.scan_csv('data/catalog.csv', separator=',', infer_schema_length=100).collect_schema()

# PRNG for reproducible sample 🗄️ `algos.md`
pl.scan_csv('pricing.csv').collect().sample(n=10, seed=42)

# get sampling from col
first_values = df['column_name'].head(5)
```

---

* dedupe by col
```python
import polars as pl
duped = pl.read_csv('clean.csv')
deduped = duped.unique(subset=["eid"], keep="first")
deduped.write_csv('clean-deduped.csv')
```

```python
df.unique(subset=['csn', 'matched_product_id'])  # dedupe
df.columns
df.schema
df.schema.keys()
col_series = df["column_name"]
col_list = df["column_name"].to_list()

unique_values = df['column_name'].unique()

# col has empty values
series.is_null().any()
# any empty columns
null_col_df = [col for col in df.columns if df[col].null_count() == df.height]
assert bool(null_col_df) is True
# find null columns
df.filter(pl.col(COL).is_null())
# value not present in column
assert df.filter(pl.col('b_line').str.to_lowercase().str.contains(query)).height == 0
# value present in every column record
assert df.filter(pl.col('b_line').str.to_lowercase().str.contains(query)).height == lines_set.height
```

## joins

---

```txt
Pandas by default uses left joins and handles the key matching differently - it maintains the left table's row count and only brings in matched columns from the right.
```

* multi
```python
res = (prod
.join(pc, on='id')  # add mfg
.join(entity, left_on='id', right_on='product_id') # add epn
.join(mars, left_on='pn', right_on='mfr_pn')  # match epn
)
```
```sql
from product join prod_class on product.id = prod_class.id
join entity on product.id = entity.product_id
join mars on entity.pn = mars.mfr_pn
```

```txt
Polars drops the right-side join key unless explicitly retained.
Since matched_product_id was only used for joining, it was removed.
Now, product_id is correctly preserved because we selected it explicitly in catalog.select([...]).

Polars follows these rules when handling columns with the same name in joins:

If on='id' is used, Polars keeps a single id column from the left table.
If left_on='id', right_on='id' is used, Polars renames the right-side column by appending _right.
If multiple tables have id but are joined differently, only the first id from the leftmost table survives unless explicitly selected.
```

how=left for left join

```python
# basic
foo.join(bar, left_on='id', right_on='mpn')

# predicate
foo.join(bar, left_on='id', right_on='mpn').filter(pl.col('foo_price') != pl.col('bar_price'))
foo.join(bar, left_on='id', right_on='mpn').filter(pl.col('manufacturer').is_in(['apple', 'motorola']))

# relative complement
bar.join(foo, left_on='mpn', right_on='id', how='anti')
```

---

🗄️ startup.py https://github.com/zachvalenta/capp-crud
```python
def smart_join(dt, tt, did, tid):
    """
    Some annoyances with Polars joins that this solves for me:
    * output doesn't locate with the join keys next to each other
    * output doesn't locate with the join keys next to each other

    :param dt: drive table
    :param tt: through table
    :param did: drive table ID
    :param tid: through table ID
    """
    joined = dt.join(tt.with_columns(pl.col(tid).alias('tid')), left_on=did, right_on=tid)
    joined.select(joined.columns[0], joined.columns[-1], *joined.columns[1:-1])
```
```python
import polars as pl
cat = pl.read_csv('catalog.csv')
res = pl.read_csv('results.csv', ignore_errors=True)
def smart_join(dt, tt, did, tid):
    """join Polars df with join keys as first columns output"""
    joined = dt.join(tt, left_on=did, right_on=tid)
    other_cols = [c for c in joined.columns if c != did]
    return (joined.with_columns(pl.col(did).alias(tid)).select([did, tid, *other_cols]))
def print_schema(schema, indent=2):
    for name, dtype in schema.items():
        print(" " * indent + f"├─ {name:<30} {dtype}")

cat.join(res, left_on='SKU', right_on='sku')
res.join(cat, left_on='sku', right_on='SKU')
smart_join(cat, res, 'SKU', 'sku')

cat.join(res, left_on='Manufacturer', right_on='Manufacturer Name')
smart_join(cat, res, 'Manufacturer', 'Manufacturer Name')
```


```python
foo.join(bar.with_columns(pl.col("upc").alias("bar_upc")), left_on="sku", right_on="upc")
foo.join(bar.with_columns(pl.col("upc").alias("bar_upc")), left_on="sku", right_on="upc").select(["sku", "bar_upc", "foo_price", "bar_price"])

joined = foo.join(bar.with_columns(pl.col("upc").alias("bar_upc")), left_on="sku", right_on="upc")
joined.select(joined.columns[0], joined.columns[-1], *joined.columns[1:-1])

select([
    "name",  # specify your desired column order
    "age",
    "id"
])

foo.join(df2, on="id").filter(pl.col("price") != pl.col("Sell Price"))
```

JOINS
```python
# BASIC
joined = capp.join(neuco, on="id", how="left")  # JK same name
joined = df1.join(df2, left_on="Part_ID", right_on="part_id")  # JK dif name

# RECONCILIATION
# 📍 update this to show what the price is
df1 = pl.DataFrame({"id": [1, 2, 3], "price": [100.0, 200.0, 300.0]})
df2 = pl.DataFrame({"id": [1, 2, 3], "price": [100.0, 250.0, 300.0]})
df1.join(df2, on="id").filter(pl.col("price") != pl.col("Sell Price"))

missing_records = capp.join(
    neuco,
    left_on=["Part_ID", "Product Item"],  # Join on both keys
    right_on=["part_id", "product_item"],
    how="left"
)

# only keeps join key from the driving table (as least in output)
df1 = pl.DataFrame({"Part_ID": [1, 2, 3], "name": ["a", "b", "c"]})
df2 = pl.DataFrame({"part_id": [1, 2, 4], "value": [10, 20, 30]})
joined = df1.join(df2, left_on="Part_ID", right_on="part_id")
# need to alias join key from through table to see it in output
joined = df1.join(df2.with_columns(pl.col("part_id").alias("df2_part_id")), left_on="Part_ID", right_on="part_id")

# trying to make it more clear in a join which attr belong to which table
df1_tagged = df1.select([pl.all().prefix("table1_")])
df2_tagged = df2.select([pl.all().prefix("table2_")])
joined = df1_tagged.join(df2_tagged, left_on="table1_Part_ID", right_on="table2_Part_ID") # adjust join key names to match prefixed names
```

## predicates

📍  membership, equality
```python
foo.join(bar, left_on='id', right_on='mpn').filter(pl.col('foo_price') != pl.col('bar_price'))
foo.join(bar, left_on='id', right_on='mpn').filter(pl.col('manufacturer').is_in(['apple', 'motorola']))

df = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"]
})
result = df.filter(pl.col("name").is_in(["Bob", "Eve"]))
df.filter(pl.col("name") == "Bob")
```

📍  CHAINING
* `~`: not
* `&`: and
* `|`: or
* `^`: xor
```python
ecl.filter(
    (pl.col('mfg') == 'Trerice') &
    (pl.col('buyline') != pl.col('priceline'))
)

df.filter(
    # filter out nulls
    (pl.col('price_line').is_not_null()) &
    # filter out numeric
    (~pl.col('price_line').str.contains(r'[0-9\.\-]')) &
    # filter out values starting with zz
    (~pl.col('price_line').str.contains(r'^ZZ'))
)

df.filter(
    (pl.col("mpn_match_score") == 100) &
    (pl.col("catalog_price").is_not_null() | pl.col("sale_price").is_not_null())
)
```

NULLS
```python
# drop null col
pl.read_csv('catalog.csv').drop(['', 'Unnamed: 0'])

# drop nulls from col
df.drop_nulls(subset=['col1', 'col2'])
pl.read_csv('fpath').filter(
    pl.col('id').is_not_null()
)
```

REGEX
```python
# keyword
bar.filter(pl.col('mfg').str.contains('foo').alias('regex'))

# case insensitive
df.filter(pl.col('description').str.contains(fr'(?i){brand}')) # newer version of Polars has `flags` kwarg

# get alphabetic values
df.filter(pl.col('price_line').str.contains(r'[^0-9\.\-]'))
```

COMPARE
```python
# EQUALITY
bar.filter(pl.col('mfg') == 'samsung')
bar.filter(pl.col('mfg').str.to_lowercase() == brand.lower())  # case insensitive

# INEQUALITY
ecl.filter(pl.col('buyline') != pl.col('priceline'))

# COMPARISON
bar.filter(pl.col('price') > 300)
```

## select

WITH_COLUMNS
* add|modify col
* lazy eval = builds query plan but only executed when computation triggered 类似 `collect()`
* 类似 SQL select on steroids i.e. chainable vs. SQL requiring CTEs|subqueries
```python
df.with_columns(
    pl.when(pl.col("catalog_price") != "")
    .then(pl.col("catalog_price"))
    .otherwise(pl.col("sale_price"))
    .alias("final_price")
)
```

SORT
```python
df.sort(
    ['col1', 'col2']
    descending=[False, True],
    nulls_last=True
)
```

ON|POST LOAD
```python
# on load
pl.read_csv(
    'fpath',
    columns=['id', 'bill_to_id', 'parent_id'],
    schema_overrides={'bill_to_id': pl.Utf8, 'parent_id': pl.Utf8}
).filter(pl.col('id').is_not_null())

# post load
Loader.load('fpath').with_columns(
        pl.col('bill_to_id').cast(pl.Utf8),
        pl.col('parent_id').cast(pl.Utf8)
    ).select(
        'id', 'bill_to_id', 'parent_id'
    ).filter(
        pl.col('id').is_not_null()
    )
```

## write

---

* operations are immutable i.e. capture updates with assignment (`df = df.operations()`)
```python
# literal
df.with_columns(pl.lit('ALCO').alias('buyline'))

# interpolated and concatenated
df.with_columns((f'{prefix}' + pl.col('mpn').cast(str)).alias('sku'))

# interpolated - predicate
df.with_columns(
    pl.when(pl.col('sku').is_null())
    .then(f'{prefix}' + pl.col('mpn').cast(str))
    .otherwise(pl.col('sku'))
    .alias('sku')
)
```

* more type casting / coercion / interpolation
```python
# Polars cast() is equivalent to pandas astype()
# Int64 matches the target schema's type
# Safer than pl.col('id').str.to_int() which can fail on non-numeric strings

# String parsing
str.to_int(), str.to_float()
# Numeric casting
cast(pl.Int32), cast(pl.Float64)
#Type coercion
coalesce(), fill_null()
```
