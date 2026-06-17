# namedtuple — Quick Reference

`namedtuple` is a factory function in `collections` that creates tuple subclasses with named fields. It supports both index-based and name-based access, unlike plain dictionaries.

```python
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])
S = Student('Nandini', '19', '2541997')
```

---

## Functions / Methods

| Method / Attribute | Description | Example |
|---|---|---|
| `S.field_name` | Access value by field name | `S.name` → `'Nandini'` |
| `S[index]` | Access value by index | `S[1]` → `'19'` |
| `getattr(S, 'field')` | Access value using `getattr` | `getattr(S, 'DOB')` → `'2541997'` |
| `S._fields` | Returns tuple of all field names | `('name', 'age', 'DOB')` |
| `S._replace(**kwargs)` | Returns a **new** namedtuple with replaced values (original unchanged) | `S._replace(name='Manjeet')` |
| `S.__new__(cls, ...)` | Creates a new instance of the namedtuple | `Student.__new__(Student, 'Himesh', '19', '260')` |
| `S.__getnewargs__()` | Returns the namedtuple as a **plain tuple** | `('Nandini', '19', '2541997')` |

---

## Conversions

| Conversion | Method / Operator | Example |
|---|---|---|
| **List → namedtuple** | `._make(iterable)` | `Student._make(['Manjeet', '19', '411997'])` |
| **Dict → namedtuple** | `**` unpacking operator | `Student(**{'name': 'Nikhil', 'age': 19, 'DOB': '139'})` |
| **namedtuple → dict** | `._asdict()` | `S._asdict()` → `{'name': 'Nandini', ...}` |
| **namedtuple → tuple** | `.__getnewargs__()` | `S.__getnewargs__()` → `('Nandini', '19', '2541997')` |

---

## Use as Struct

```python
Point = namedtuple('Point', ['x', 'y'])
points = [Point(4, 3), Point(9, 4.4)]
for p in points:
    print(p.x, p.y)
```
