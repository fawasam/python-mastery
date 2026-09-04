# Topic: Datetime, Timestamps & Timezones

## What You Will Learn
- `datetime.date`, `datetime.time`, `datetime.datetime`, `datetime.timedelta`.
- Formatting dates to strings (`strftime`) and parsing strings to dates (`strptime`).
- Naive datetimes vs Timezone-aware datetimes (`timezone.utc`).
- Date arithmetic (adding/subtracting days, calculating duration between timestamps).

## Syntax
```python
from datetime import datetime, timezone, timedelta

now_utc = datetime.now(timezone.utc)
formatted = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
parsed = datetime.strptime("2026-09-04", "%Y-%m-%d")

next_week = now_utc + timedelta(days=7)
```

## Next Topic
Next: `json` — JSON parsing, serialization (`dumps`/`dump`), deserialization (`loads`/`load`), and custom encoders.
