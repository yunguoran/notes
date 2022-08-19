# Exceptions

## pymongo.errors.InvalidOperation: cannot set options after executing query

### example

```text
pymongo.errors.InvalidOperation: cannot set options after executing query
```

### cause & fix

- print `type(your_list)` you will notice it's not a list of dict but a pymongo.cursor.Cursor object (which is read-only).
- change `your_list = users.find({})` to `user_list = list(users.find({}))` (but be cautious it will query all record from collection users).

### reference

- [pymongo.errors.InvalidOperation: cannot set options after executing query](https://stackoverflow.com/questions/62550144/pymongo-errors-invalidoperation-cannot-set-options-after-executing-query)
