#!/usr/bin/env python3

import sys

# Initialize counters
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    # Read lines from standard input
    for i, line in enumerate(sys.stdin):
        try:
            # Parse line into components
            ip_address, _, _, timestamp, _, method, resource, protocol, status_code, file_size = line.split()

            # Increment counters
            total_size += int(file_size)
            status_codes[int(status_code)] += 1

            # Print statistics every 10 lines
            if i % 10 == 9:
                print("File size: {}".format(total_size))
                for code in sorted(status_codes):
                    if status_codes[code] > 0:
                        print("{}: {}".format(code, status_codes[code]))
                print()

        except ValueError:
            # Skip lines that do not match expected format
            continue

except KeyboardInterrupt:
    # Print final statistics on interrupt
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
    sys.exit(0)
