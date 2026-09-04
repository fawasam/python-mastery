"""
Post-Mortem Debugging Hook using sys.excepthook.
"""

import sys
import types


def custom_excepthook(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_tb: types.TracebackType | None,
) -> None:
    """
    Global unhandled exception hook that captures unhandled crashes gracefully.
    """
    print("\n================ GLOBAL UNHANDLED EXCEPTION CAUGHT ================")
    print(f"Exception Type : {exc_type.__name__}")
    print(f"Exception Message: {exc_value}")
    print("===================================================================")


def main_workflow() -> None:
    # Save original excepthook
    original_hook = sys.excepthook
    # Set custom excepthook for unhandled errors
    sys.excepthook = custom_excepthook

    try:
        items = [10, 20, 30]
        _ = items[10]
    except IndexError as err:
        # Manually invoke excepthook for demonstration
        sys.excepthook(type(err), err, err.__traceback__)
    finally:
        sys.excepthook = original_hook


if __name__ == "__main__":
    main_workflow()
