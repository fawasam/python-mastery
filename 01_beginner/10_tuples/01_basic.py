"""
Topic: Tuple Fundamentals & Extended Unpacking
File: 01_basic.py
"""

def demonstrate_tuples() -> None:
    # 1. Tuple creation
    server_location: tuple[str, int] = ("192.168.1.1", 8080)
    print(f"Tuple: {server_location} (type: {type(server_location).__name__})")

    # 2. Tuple Unpacking
    ip, port = server_location
    print(f"Unpacked -> IP: {ip}, Port: {port}")

    # 3. Extended Unpacking using asterisk (*) operator
    scores = (98, 85, 92, 78, 90)
    highest, *middle_scores, lowest = sorted(scores, reverse=True)
    print(f"\nHighest score: {highest}")
    print(f"Middle scores:  {middle_scores}")
    print(f"Lowest score:   {lowest}")


if __name__ == "__main__":
    demonstrate_tuples()
