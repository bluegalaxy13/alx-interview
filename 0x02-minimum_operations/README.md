# Minimum Operations

## Description
In this project, we are tasked with calculating the minimum number of operations required to achieve exactly `n` characters of `'H'` in a text file. The text editor allows only two operations:

1. **Copy All**: Copies all the characters currently in the file.
2. **Paste**: Pastes the characters from the clipboard.

Starting with a single `'H'`, the goal is to compute the fewest number of operations to end up with exactly `n` `'H'` characters.

### Example
For `n = 9`, the sequence of operations is:

1. Start with: `H`
2. **Copy All**: Copies the current `H`.
3. **Paste**: `HH`
4. **Paste**: `HHH`
5. **Copy All**: Copies `HHH`.
6. **Paste**: `HHHHHH`
7. **Paste**: `HHHHHHHHH`

Number of operations = 6.

## Prototype
```python
def minOperations(n):
    '''Computes the fewest number of operations needed to result in exactly n H characters.'''
