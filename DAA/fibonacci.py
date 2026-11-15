
import time

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def non_recursive_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    start = time.perf_counter()
    print("\nNon-Recursive Fibonacci:")
    non_recursive_fibonacci(n)
    end = time.perf_counter()

    print("\nExecution Time:", end - start, "seconds")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")

    start = time.perf_counter()
    print("\nRecursive Fibonacci:")
    for i in range(n):
        print(recursive_fibonacci(i), end=" ")
    end = time.perf_counter()

    print("\nExecution Time:", end - start, "seconds")
    print("Time Complexity: O(2^n)")
    print("Space Complexity: O(n)")
