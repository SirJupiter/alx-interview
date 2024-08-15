#!/usr/bin/python3

import sys
from collections import defaultdict


def print_msg(status_counts, total_file_size):
    """
    Print the total file size and the count of different HTTP status codes.

    Args:
        status_counts: Dictionary of status codes.
        total_file_size: Total size of the files processed.
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_counts.items()):
        if count:
            print(f"{code}: {count}")


def main():
    total_file_size = 0
    status_counts = defaultdict(int)
    # Initialize a default dictionary to count status codes
    line_counter = 0

    # Define the expected status codes
    valid_status_codes = {
        "200", "301", "400", "401", "403", "404", "405", "500"}

    try:
        for line in sys.stdin:
            parsed_line = line.split()
            if len(parsed_line) > 2:
                # Count the line and track the line number
                line_counter += 1

                file_size = int(parsed_line[-1])
                # Assuming file size is always the last item

                status_code = parsed_line[-2]
                # Assuming status code is always second last

                total_file_size += file_size

                # Increment count for valid status codes
                if status_code in valid_status_codes:
                    status_counts[status_code] += 1

                # Print message every 10 lines
                if line_counter == 10:
                    print_msg(status_counts, total_file_size)
                    line_counter = 0  # Reset line counter

    finally:
        print_msg(status_counts, total_file_size)  # Print any remaining counts


if __name__ == "__main__":
    main()
