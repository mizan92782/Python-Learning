# Python Class Decorators (Complete Guide)

This document explains Python class decorators with:

- Why they are used
- Simple explanation
- Full working examples

---

## 📌 Summary Table

| Decorator           | Why it is used                | Simple Explanation           |
| ------------------- | ----------------------------- | ---------------------------- |
| `@staticmethod`     | Utility function inside class | No self/cls needed           |
| `@classmethod`      | Works with class data         | Uses cls instead of object   |
| `@property`         | Access method like attribute  | Getter method                |
| `@property.setter`  | Control value assignment      | Adds validation              |
| `@property.deleter` | Control deletion              | Safe deletion                |
| `@abstractmethod`   | Force child implementation    | Enforces required method     |
| `@dataclass`        | Reduce boilerplate code       | Auto-generates class methods |
| `@cached_property`  | Cache expensive result        | Compute once, reuse          |

---

# 1. @staticmethod

## Why it is used

Used when a method does NOT need:

- `self`
- `cls`

It is just a utility function inside a class.

## Example

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Math.add(10, 5))
print(Math.multiply(3, 4))
```
