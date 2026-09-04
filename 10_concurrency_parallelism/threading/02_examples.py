"""
Daemon Threads vs Standard Threads.
"""

import threading
import time


def background_heartbeat() -> None:
    while True:
        print("[DAEMON] Heartbeat ping...")
        time.sleep(0.05)


def main() -> None:
    # Daemon thread exits automatically when non-daemon main thread terminates!
    daemon_thread = threading.Thread(target=background_heartbeat, daemon=True)
    daemon_thread.start()

    print("[MAIN] Main thread doing work...")
    time.sleep(0.12)
    print("[MAIN] Main thread exiting. Daemon thread will terminate cleanly.")


if __name__ == "__main__":
    main()
