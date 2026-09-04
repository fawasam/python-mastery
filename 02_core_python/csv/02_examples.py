"""
Topic: Tab-Separated Values (TSV) & Custom Delimiters
File: 02_examples.py
"""
import csv
import io

def parse_custom_delimiter_tsv() -> None:
    tsv_data = "id\tname\tscore\n1\tAlice\t98.5\n2\tBob\t88.0\n"

    # Simulating file reading using StringIO
    f = io.StringIO(tsv_data)
    reader = csv.DictReader(f, delimiter="\t")

    print("Parsed TSV Records:")
    for row in reader:
        print(f"  ID: {row['id']} | Name: {row['name']} | Score: {row['score']}")


if __name__ == "__main__":
    parse_custom_delimiter_tsv()
