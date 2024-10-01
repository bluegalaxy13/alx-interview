# Pascal's Triangle Function

This project contains a Python function that generates Pascal's Triangle up to a specified number of rows.

## Interview Question

Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
- Returns an empty list if n <= 0
- You can assume n will be always an integer

## Function Overview

The function `pascal_triangle(n)` takes an integer `n` and returns a list of lists of integers representing Pascal's Triangle with `n` rows.

### Pascal's Triangle

Pascal's Triangle is a triangular array where:
- The first and last elements of each row are 1.
- Each interior element is the sum of the two elements directly above it from the previous row.

For example, if `n = 5`, the triangle generated would be:

[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
