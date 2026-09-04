"""
Unittest Lifecycle Hooks: setUp, tearDown, setUpClass, and tearDownClass.
"""

import unittest


class StateTracker:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, item: str) -> None:
        self.items.append(item)


class TestStateTrackerLifecycle(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("\n[HOOK] setUpClass: Runs ONCE before all tests in this class.")

    def setUp(self) -> None:
        print("[HOOK] setUp: Initializing fresh StateTracker instance.")
        self.tracker = StateTracker()

    def test_add_single_item(self) -> None:
        self.tracker.add("Alpha")
        self.assertEqual(len(self.tracker.items), 1)
        self.assertIn("Alpha", self.tracker.items)

    def test_add_multiple_items(self) -> None:
        # Isolated test: tracker is fresh instance created by setUp!
        self.tracker.add("Beta")
        self.tracker.add("Gamma")
        self.assertEqual(len(self.tracker.items), 2)

    def tearDown(self) -> None:
        print("[HOOK] tearDown: Cleaning up test state.")

    @classmethod
    def tearDownClass(cls) -> None:
        print("[HOOK] tearDownClass: Runs ONCE after all tests complete.")


if __name__ == "__main__":
    unittest.main()
