#!/usr/bin/env python3
"""
This script is designed to set up a basic file structure for a specified day of
the Advent of Code challenge. It creates a new directory for the day, a Python
script template for solving the day's puzzle, and placeholders for input and
example data. Additionally, it integrates with the `get_input.py` script to
automatically fetch and store the day's puzzle input.

Usage:
    Run the script with a day number as an argument to set up the project for that day.
    Example: ./aoc.py 1
"""

import os
import argparse
from aoc.get_input import fetch_input  # Ensure get_input.py is in the same directory or in PYTHONPATH

def create_project(day, year):
    """
    Creates the project directory and files for a specified day of Advent of Code.

    Args:
        day (str): The day number for which to create the project structure.

    This function creates a directory named after the day, a Python script with a basic
    template, and placeholder files for the puzzle input and example. It also fetches
    the actual puzzle input for the specified day and writes it to the 'input' file.
    """
    day_dir = f"{day}"
    os.makedirs(day_dir, exist_ok=True)

    python_file = os.path.join(day_dir, f"{day}.py")
    with open(python_file, 'w', encoding='utf-8') as file:
        file_contents = [
            "#!/usr/bin/env python\n",
            "import sys\n\n",
            "def main():\n",
            "    with open(sys.argv[1], 'r', encoding='utf-8') as file:\n",
            "        for line in file:\n",
            "            line = line.strip()\n",
            "            # Your code here\n",
            "\n",
            "if __name__ == '__main__':\n",
            "    main()\n"
        ]
        file.writelines(file_contents)
    os.chmod(python_file, 0o755)

    input_text = fetch_input(year, day)  # Adjust the year if necessary
    with open(os.path.join(day_dir, "input"), 'w', encoding='utf-8') as file:
        file.write(input_text)

    with open(os.path.join(day_dir, "example"), 'a', encoding='utf-8'):
        pass

def main():
    """
    Main function to handle command-line arguments and initiate project creation.
    """
    parser = argparse.ArgumentParser(description='Set up a new Advent of Code day project.')
    parser.add_argument('day', type=int, help='Day of the event')
    parser.add_argument('-y', '--year', type=int, default=2023,\
            help='Year of the event (default: 2023)')
    args = parser.parse_args()

    create_project(args.day, args.year)
    print(f"Project for Day {args.day} of year {args.year} created successfully.")

if __name__ == "__main__":
    main()
