"""
Solutions for Defensive Programming Exercises.
"""


def calculate_shipping_cost(weight: float, distance: float, destination_country: str) -> float:
    if weight <= 0:
        raise ValueError(f"Weight must be > 0, got {weight}")
    if distance <= 0:
        raise ValueError(f"Distance must be > 0, got {distance}")
    if not destination_country or not destination_country.strip():
        raise ValueError("Destination country must be a non-empty string")

    base_rate = 5.0
    weight_factor = weight * 1.5
    distance_factor = distance * 0.05
    multiplier = 2.0 if destination_country.strip().upper() != "US" else 1.0

    return (base_rate + weight_factor + distance_factor) * multiplier


if __name__ == "__main__":
    cost = calculate_shipping_cost(10.0, 100.0, "US")
    print(f"Calculated Shipping Cost: ${cost:.2f}")
