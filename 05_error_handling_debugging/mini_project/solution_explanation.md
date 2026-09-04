# Solution Explanation: Resilient Data Ingestion Engine

## Key Architecture Decisions

1. **Custom Exception Hierarchy (`IngestionError`, `InvalidPayloadError`)**:
   Enables high-level callers to catch ingestion domain errors without relying on generic exceptions.

2. **Exception Chaining (`raise ... from err`)**:
   Preserves underlying `json.JSONDecodeError` tracebacks while exposing clean domain error messages.

3. **Batch Fault Tolerance**:
   Individual corrupt items do not crash the entire ingestion pipeline; failures are logged with diagnostic telemetry, allowing valid payload items to complete processing cleanly.

4. **Structured Logging**:
   Uses `logging.getLogger("IngestionEngine")` with `StreamHandler` to route telemetry to standard output.
