# Integer Overflow Bug in Recursive Factorial

This repository demonstrates a common error in recursive functions: integer overflow.  The provided Python code attempts to calculate the factorial of a number using recursion. However, it doesn't handle the possibility of exceeding Python's maximum integer size for large inputs.  This can lead to incorrect results or program crashes.

The `bug.py` file contains the buggy code. The `bugSolution.py` file offers a solution to mitigate the issue.

The solution uses iterative approach or external library like `decimal` to support arbitrary precision integers