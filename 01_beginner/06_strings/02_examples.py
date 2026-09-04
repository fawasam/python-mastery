"""
Topic: String Transformation & Parsing Examples
File: 02_examples.py
"""

def parse_csv_line_example() -> None:
    # Simulating parsing a CSV string record
    csv_line = "101, Alice Johnson, Senior Engineer, 125000"

    # Splitting into individual field tokens
    tokens = csv_line.split(",")
    # Cleaning whitespace from tokens
    clean_tokens = [t.strip() for t in tokens]

    emp_id, name, role, salary = clean_tokens
    print(f"ID: {emp_id} | Name: {name} | Role: {role} | Salary: ${int(salary):,}")

    # Joining tokens back into a formatted CSV line
    reconstructed = " | ".join(clean_tokens)
    print("Reconstructed:", reconstructed)


if __name__ == "__main__":
    parse_csv_line_example()
