Pascal's Triangle Generator
Introduction

This repository contains a Python script that generates the first n rows of Pascal's triangle as a list of lists of integers.
Requirements

    Python 3.6 or higher

Installation

    Clone the repository: git clone https://github.com/ALVINdimpos/alx-interview.git
    Navigate to the repository directory: cd repo
    Navigate to the pascal_triangle directory: cd 0x00-pascal_triangle
    Run the script: python pascal_triangle.py

Usage

python

from pascal_triangle import pascal_triangle

# Generate the first 5 rows of Pascal's triangle
triangle = pascal_triangle(5)

# Print the resulting triangle
for row in triangle:
    print(row)

This will output:

csharp

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

Contributing

Contributions are welcome! If you find a bug or would like to suggest an improvement, please open an issue or submit a pull request.
License

This code is released under the MIT License.