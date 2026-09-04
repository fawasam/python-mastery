# Topic: Regular Expressions & `re` Module

## What You Will Learn
- Pattern matching using Python's built-in `re` module.
- Functions: `re.search()`, `re.match()`, `re.findall()`, `re.finditer()`, `re.sub()`.
- Metacharacters: `\d` (digit), `\w` (word character), `\s` (whitespace), `^` (start), `$` (end).
- Quantifiers: `*` (0+), `+` (1+), `?` (0 or 1), `{n,m}` (range).
- Capturing groups `()` and named groups `(?P<name>pattern)`.

## Syntax
```python
import re

pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
email = "user@domain.com"
is_valid = bool(re.match(pattern, email))
```

## Next Topic
Next: `datetime` — Parsing, formatting, and arithmetic with dates and timestamps.
