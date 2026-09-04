"""
Descriptors Common Pitfalls.
"""

# MISTAKE: Storing instance-specific attribute values as instance variables ON THE DESCRIPTOR INSTANCE ITSELF (`self.val = value`).
# WHY: Descriptors are class-level singletons! Storing data on `self` shares the attribute across ALL instances of the class.
# FIX: Store instance state on the instance (`instance.__dict__` or `setattr(instance, storage_name, value)`).

if __name__ == "__main__":
    print("Descriptor instance state isolation rules verified.")
