<h1>SQLite Query</h1>


To get started with this SQLite query assembly, you must first add it to your __init__ executable class. Next, you need to access the connection attribute and specify the path to your database. This is so that if you initialize everything at the root of your class, which will later be inherited, it will help avoid having to constantly connect to the database. This way we connect only once and maintain a connection to the database constantly.


```python
from SQLite import SQLite


class SQLite_Example:
    def __init__(self):
        self.sql = SQLite()
        self.sql.connect = sqlite3.connect(f'./base/Base.db')
```

Below are examples of the "CRUD" (CREATE, READ, UPDATE, DELETE) principle.
All queries in the database are structured so that you list as many arguments as you like in the form of a dictionary for a particular action. It seems to me that this is very convenient.


***In the following examples, I mean that you are working with classes and their methods, and you imported `SQLite()` somewhere earlier and now it is inherited.***

<h3>INSERT(CREATE)</h3>

This is what the dictionary will look like in order to insert something into your table in your database.

`{'table': 'name_table', 'name_column1': 'something_data1', 'name_column2': 'something_data2', ...}`

table = table name, value in this example is "accounts",

account_info = column name.

If your data has a list or dictionary data type, you must use json.dumps() !

the data is inserted into the "account_info" column

idx = also the name of the "idx" column and the value that needs to be filled in

```python
data = {'email': 'email@email.com', 'password': '12345qwerty!'}
data = json.dumps(data)
query = {'table': 'accounts', 'account_info': data, 'idx': 897899}
# And as many arguments as you want to fill in the columns
self.sql.insert(**query)  # if no problems return True
```

You should contact `self.sql` and call its `insert` method, i.e. the full form of `self.sql.insert` and pass it `**kwargs`

***In general, this principle remains the same for almost all methods (except for delete, I practically didn’t use it, sorry).***

***That's exactly the concept.***

<h3>SELECT</h3>

```python
query = {'table': 'accounts', 'idx': 3}
data = self.sql.select(**query)
print(data)

#  If there are more than 1 columns, then you need to put it in the list ['idx', 'shadow']
query = {'table': 'accounts', 'column': ['idx', 'shadow'], 'shadow': 1}
data = self.sql.select(**query)
print(data)  # return data from table 'accounts' according to specified parameters

query = {'table': 'accounts', 'country': 'US', 'fetchall': False}  # default fetchall=True
data = self.sql.select(**query)
print(data)  # return data from table 'accounts' according to specified parameters

#  If column is 1, then the data type is string
query = {'table': 'accounts', 'country': 'US', 'shadow': 1, 'column': 'idx'}
data = self.sql.select(**query)
print(data)  # return data from table 'accounts' according to specified parameters
```

<h3>UPDATE</h3>

In order to `update` , a `selector` is added here thanks to which we can determine exactly where exactly we need to update this or that value. (If there are many identical values in the database, everything will be updated. Be careful!)

There can be several selectors so that you can be more specific.

```python
 # selector value type str!
query = {'table': 'accounts', 'selector': {'idx': str(1), 'device_id': '12345'}, 'shadow': 0}
self.sql.update(**query)  # return None

query = {'table': 'accounts', 'selector': {'idx': str(1)}, 'shadow': 0, 'country': 'KZ', 'last_publish': time.time()}
self.sql.update(**query)

data = ['1', '2', 3]
data = json.dumps(data)  # need json.dumps() if that dict, or list
query = {'table': 'accounts',  'selector': {'idx': str(1)}, 'account_info': data}
self.sql.update(**query)

data = {'key0': 'value0', 'key1': 'value1'}
data = json.dumps(data)  # need json.dumps() if that dict, or list
query = {'table': 'accounts', 'selector': {'idx': str(1)}, 'account_info': data}
self.sql.update(**query)
```

<h3>DELETE</h3>

```python
self.sql.delete(table='accounts', columns='idx', value=0)
# sorry, im very small used delete
```

