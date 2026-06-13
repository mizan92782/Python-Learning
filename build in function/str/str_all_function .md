# Create a Markdown file with Python string methods cheat sheet

content = """# 📘 Python String Methods Cheat Sheet

---

## 🔤 1. Case Conversion

| Method | Example | Explanation |
|--------|--------|-------------|
| upper() | "hello".upper() -> HELLO | Converts all letters to uppercase |
| lower() | "HELLO".lower() -> hello | Converts all letters to lowercase |
| title() | "mizan rahman".title() -> Mizan Rahman | First letter of each word capital |
| capitalize() | "hello world".capitalize() -> Hello world | First letter only capital |
| swapcase() | "HeLLo".swapcase() -> hEllo | Swap uppercase <-> lowercase |

---

## 🔍 2. Search & Check

| Method | Example | Explanation |
|--------|--------|-------------|
| find() | "hello".find("e") -> 1 | Returns index, -1 if not found |
| index() | "hello".index("e") -> 1 | Returns index, error if not found |
| startswith() | "python".startswith("py") -> True | Checks beginning |
| endswith() | "file.pdf".endswith(".pdf") -> True | Checks ending |
| count() | "banana".count("a") -> 3 | Counts occurrences |

---

## ✏️ 3. Modify Strings

| Method | Example | Explanation |
|--------|--------|-------------|
| replace() | "I love Java".replace("Java","Python") | Replaces text |
| strip() | " hello ".strip() -> "hello" | Removes both side spaces |
| lstrip() | " hello".lstrip() -> "hello" | Removes left spaces |
| rstrip() | "hello ".rstrip() -> "hello" | Removes right spaces |

---

## 🔪 4. Split & Join

| Method | Example | Explanation |
|--------|--------|-------------|
| split() | "a b c".split() -> ['a','b','c'] | Splits into list |
| rsplit() | "a b c".rsplit(" ",1) | Split from right |
| splitlines() | "a\\nb\\nc".splitlines() | Splits by lines |
| join() | "-".join(["a","b"]) -> a-b | Joins list into string |

---

## ✅ 5. Validation

| Method | Example | Explanation |
|--------|--------|-------------|
| isalpha() | "abc".isalpha() -> True | Only letters |
| isdigit() | "123".isdigit() -> True | Only numbers |
| isalnum() | "abc123".isalnum() -> True | Letters + numbers |
| islower() | "abc".islower() -> True | All lowercase |
| isupper() | "ABC".isupper() -> True | All uppercase |
| isspace() | "   ".isspace() -> True | Only spaces |

---

## 📌 6. Formatting

| Method | Example | Explanation |
|--------|--------|-------------|
| format() | "{}".format("Hi") -> Hi | String formatting |
| center() | "hi".center(5) -> ' hi ' | Center align |
| ljust() | "hi".ljust(5) -> 'hi   ' | Left align |
| rjust() | "hi".rjust(5) -> '   hi' | Right align |
"""

file_path = "/mnt/data/python_string_methods_cheatsheet.md"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

file_path