"""
Topic: Common Mistakes with CSV Files
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_newline_param() -> None:
    # ❌ WRONG: open("file.csv", "w") without newline=""
    # On Windows and some platforms, this causes extra blank lines between rows!

    # ✅ CORRECT: Always pass newline="" when opening files for csv.writer or csv.DictWriter
    print("Always use open('file.csv', 'w', newline='', encoding='utf-8') for CSV output.")


if __name__ == "__main__":
    mistake_1_forgetting_newline_param()
