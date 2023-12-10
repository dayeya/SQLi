# SQL Injection tests.
A website demonstrating an SQL Injection attack using Python 3.12 and Flask, Sqlite3.

# SQL Injection.
This website uses a simple SQLite3 database that is intentionally vulnerable to SQL Injection attacks.
That is by using the `f strings` in Python, the following code is where the breach occurs.
```python
    def get_user(self, user_name: str, password: str) -> dict:
        all_users = {}
        query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND password = '{password}'"
        # rest of the code...
```
As a result of using the `f-string`, parsing an SQL Injection payload can cause trouble.<br>
E.g parsing the `' OR 'a'='a';--` payload and a random password (abcd) can exploit the database.
```sql
SELECT * FROM users WHERE user_name = '' OR 'a'='a';-- AND password = 'abcd'
```
We've managed to make the query always True.

# Authors
Daniel Sapojnikov 2023, THIS CODE WAS WRITTEN FOR EDUCATIONAL PURPOSES ONLY.
