#!/usr/bin/env python3

"""
This module provides functionality to download the puzzle input for a specific day
of the Advent of Code event. It can be used either as a standalone script or as an
importable module in other Python scripts.

The main function of the script handles command line arguments to specify the year
and day for which the puzzle input is required. The fetch_input function can be used
to programmatically retrieve puzzle inputs within other Python code.
"""

import sys
import argparse
import requests

USER_AGENT = 'https://github.com/cmoron/aoc/ by cyril.moron at gmail.com'
# SESSION_TOKEN = 'your_session_token_here'
SESSION_TOKEN = '53616c7465645f5fbef8302b28fa68deab244f03a7ae0e0fc5f47bc85dc7194c6830b657cfa7289a415d249c5034c761429823b18c1ae6a54a162066a1244425'
TIMEOUT = 10  # seconds

def fetch_input(year, day):
    """
    Downloads the puzzle input for the specified day and year from Advent of Code.

    Args:
        year (int): The year of the event.
        day (int): The day of the event.

    Returns:
        str: The puzzle input for the specified day and year.

    Raises:
        SystemExit: If the request for fetching the input fails.
    """
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    try:
        response = requests.get(url, cookies={'session': SESSION_TOKEN}, headers={'User-Agent': USER_AGENT}, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException as requests_exception:
        print(f"Error fetching data: {requests_exception}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to execute the script as a standalone program. It parses command
    line arguments for year and day, and prints the fetched puzzle input.
    """
    parser = argparse.ArgumentParser(description='Fetch Advent of Code puzzle input.')
    parser.add_argument('-y', '--year', type=int, default=2023, help='Year of the event')
    parser.add_argument('-d', '--day', type=int, default=1, help='Day of the event')
    args = parser.parse_args()

    input_text = fetch_input(args.year, args.day)
    print(input_text, end='')

if __name__ == "__main__":
    main()
