# Topic: JSON Parsing & Custom Serialization

## What You Will Learn
- Serialization: `json.dumps()` (to string) and `json.dump()` (to file).
- Deserialization: `json.loads()` (from string) and `json.load()` (from file).
- Custom JSON encoders subclassing `json.JSONEncoder` (handling `datetime`, `UUID`, set objects).
- Controlling indentation, key sorting, and UTF-8 encoding.

## Syntax
```python
import json

data = {"user": "Alice", "active": True}
json_string = json.dumps(data, indent=2)
parsed = json.loads(json_string)
```

## Next Topic
Next: `csv` — Reading and writing CSV data using `csv.reader`, `csv.writer`, `DictReader`, `DictWriter`.
