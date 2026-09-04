"""
Topic: LEGB Scope Resolution Basics
File: 01_basic.py
"""

# Global Scope Variable
app_name = "Mastery Service"

def outer_function() -> None:
    # Enclosing Scope Variable
    service_version = "v2.4.0"

    def inner_function() -> None:
        # Local Scope Variable
        request_id = "req_1009"
        
        # Demonstrating LEGB resolution:
        # request_id comes from Local
        # service_version comes from Enclosing
        # app_name comes from Global
        # print comes from Built-in
        print(f"[{app_name} | {service_version}] Processing {request_id}")

    inner_function()


if __name__ == "__main__":
    outer_function()
