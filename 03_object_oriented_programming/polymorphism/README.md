# Topic: Polymorphism & Duck Typing

## What You Will Learn
- Polymorphism concept: Treating different classes implementing the same interface identically.
- Python's **Duck Typing** philosophy: *"If it walks like a duck and quacks like a duck, it's a duck."*
- Decoupling callers from concrete implementations.

## Syntax
```python
class PDFExporter:
    def export(self, data): return "Exporting PDF"

class CSVExporter:
    def export(self, data): return "Exporting CSV"

# Polymorphic processor
def run_exporter(exporter, data):
    return exporter.export(data)  # Works with any object having .export()
```

## Next Topic
Next: `encapsulation` — Access modifiers (`_protected`, `__private`), name mangling, and getter/setter methods.
