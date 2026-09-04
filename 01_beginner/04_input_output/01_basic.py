"""
Topic: User Input & Advanced String Formatting
File: 01_basic.py
"""

def demonstrate_input_and_formatting() -> None:
    # Note: When running headlessly in non-interactive terminals,
    # input() reads from standard input or mock streams.
    print("--- User Registration Example ---")
    
    # Simulating values (or reading if interactive)
    user_name = "Alex"
    user_age_str = "28"
    salary_str = "95450.50"

    # Always cast input strings when expecting numeric calculations!
    user_age = int(user_age_str)
    salary = float(salary_str)

    # Professional f-string formatting
    print(f"Name: {user_name}")
    print(f"Age:  {user_age} years")
    print(f"Annual Compensation: ${salary:,.2f}")


if __name__ == "__main__":
    demonstrate_input_and_formatting()
