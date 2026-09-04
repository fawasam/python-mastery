"""
Topic: Returning Tuples & Tuple Dictionary Keys
File: 02_examples.py
"""

def get_system_stats() -> tuple[float, float, int]:
    # Functions returning multiple comma-separated values return a tuple
    cpu = 14.2
    ram = 8.5
    processes = 142
    return cpu, ram, processes


def demonstrate_tuple_as_dict_key() -> None:
    # Lists CANNOT be dict keys because they are mutable (unhashable).
    # Tuples CAN be dict keys because they are immutable (hashable).
    spatial_index: dict[tuple[int, int], str] = {
        (0, 0): "Origin Node",
        (10, 20): "Warehouse Alpha",
        (50, 75): "Distribution Hub",
    }

    target_coord = (10, 20)
    print(f"Location at {target_coord}: {spatial_index.get(target_coord)}")


if __name__ == "__main__":
    cpu, ram, procs = get_system_stats()
    print(f"System Stats -> CPU: {cpu}%, RAM: {ram}GB, Processes: {procs}")
    
    print("\n--- Tuple as Dict Key ---")
    demonstrate_tuple_as_dict_key()
