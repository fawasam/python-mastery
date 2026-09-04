"""
Topic: Loop Directives (break, continue, else)
File: 02_examples.py
"""

def demonstrate_for_else_search() -> None:
    server_ports = [80, 443, 8080, 3000, 5432]
    target_port = 5432

    print(f"Searching for target port {target_port}...")
    for port in server_ports:
        if port == target_port:
            print(f"✅ Found target port {port}!")
            break  # Exit loop immediately
    else:
        # Executes ONLY if the loop finishes naturally without breaking!
        print(f"❌ Target port {target_port} not found in list.")


def demonstrate_continue_statement() -> None:
    print("\nProcessing odd numbers only:")
    for num in range(1, 10):
        if num % 2 == 0:
            continue  # Skip even numbers
        print(f"Odd number: {num}")


if __name__ == "__main__":
    demonstrate_for_else_search()
    demonstrate_continue_statement()
