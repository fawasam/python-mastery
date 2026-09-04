"""
Topic: Generator Pipelines
File: 02_examples.py
"""

def log_lines_generator():
    logs = [
        "2026-09-04 10:00:01 INFO User login",
        "2026-09-04 10:00:02 ERROR DB connection failed",
        "2026-09-04 10:00:03 INFO Page render",
        "2026-09-04 10:00:04 ERROR Timeout on socket",
    ]
    for log in logs:
        yield log


def filter_errors(log_stream):
    for log in log_stream:
        if "ERROR" in log:
            yield log


def format_error_alert(error_stream):
    for error in error_stream:
        yield f"🚨 ALERT: {error}"


if __name__ == "__main__":
    # Pipeline composition: log_lines -> filter_errors -> format_error_alert
    pipeline = format_error_alert(filter_errors(log_lines_generator()))
    
    print("Consuming processing pipeline output:")
    for alert in pipeline:
        print(alert)
