"""
Topic: Hello World & Printing Basics
File: 04_exercises.py

Complete the exercises below by replacing `raise NotImplementedError` with your code.
Verify your solutions against 05_solution.py.
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Print your name and favorite programming language on separate lines.
    """
    print("My name is fawas a", "Favorite language is python", sep="\n")



def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Print the text "Python:3.12:Professional" using a single print statement
    with a custom separator (`sep`).
    """
    print("Python" ,"3.12","Professional",sep=":")
    # TODO: Use print() with three string arguments and sep=":"
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Print "Processing item 1...", "Processing item 2...", "Processing item 3..."
    all on the SAME terminal line, separated by " -> ".
    """
    # for i in range(1, 4):
    #     print(f"Processing item {i}...", end=" -> ")
    print("Processing item 1..." ,"Processing item 2..." ,"Processing item 3...", sep=" -> " , end="")
    # TODO: Use multiple print statements with `end` parameter
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Output a formatted CLI header box for an application called "DATA PIPELINE OPERATOR".
    It should look like this:
    +----------------------------------+
    |      DATA PIPELINE OPERATOR      |
    +----------------------------------+
    """
    title = "DATA PIPELINE OPERATOR"
    print("|" + "_" * (len(title) + 2) + "|")
    print("|" + " " + title + " " + "|")
    print("|" + "_" * (len(title) + 2) + "|")
    # TODO: Print the formatted ASCII banner
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    try:
        level_1_easy()
    except NotImplementedError as e:
        print(f"Level 1: {e}")

    try:
        level_2_medium()
    except NotImplementedError as e:
        print(f"Level 2: {e}")

    try:
        level_3_hard()
    except NotImplementedError as e:
        print(f"Level 3: {e}")

    try:
        level_4_real_world()
    except NotImplementedError as e:
        print(f"Level 4: {e}")
