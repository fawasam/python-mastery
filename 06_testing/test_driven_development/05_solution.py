"""
Solutions for TDD Exercises.
"""


def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def test_fizzbuzz() -> None:
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(20) == "Buzz"
    assert fizzbuzz(7) == "7"
    print("TDD FizzBuzz suite passed successfully!")


if __name__ == "__main__":
    test_fizzbuzz()
