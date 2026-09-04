"""
Topic: Frozen (Immutable) Dataclasses as Hashable Dict Keys
File: 02_examples.py
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float


if __name__ == "__main__":
    coord1 = Coordinate(37.7749, -122.4194)
    coord2 = Coordinate(37.7749, -122.4194)

    # Immutable frozen dataclasses can be stored in sets and dict keys because they generate __hash__()!
    geo_cache: dict[Coordinate, str] = {
        coord1: "San Francisco City Center"
    }

    print(f"Lookup by identical frozen coord object: {geo_cache[coord2]}")
