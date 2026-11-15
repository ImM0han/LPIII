
import time
import random
from concurrent.futures import ThreadPoolExecutor


# Merge two sorted lists
def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)
    return result


# Normal Merge Sort
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    return merge(left, right)


# Multithreaded Merge Sort
def threaded_merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_half = numbers[:middle]
    right_half = numbers[middle:]

    # Sort both halves using separate worker threads
    with ThreadPoolExecutor(max_workers=2) as executor:
        left_task = executor.submit(merge_sort, left_half)
        right_task = executor.submit(merge_sort, right_half)

        left = left_task.result()
        right = right_task.result()

    return merge(left, right)


# Main program
print("===== MERGE SORT PROJECT =====")

numbers = list(map(int, input(
    "Enter numbers separated by spaces: "
).split()))

# Normal Merge Sort
start = time.perf_counter()
sorted_numbers = merge_sort(numbers.copy())
normal_time = time.perf_counter() - start

# Multithreaded Merge Sort
start = time.perf_counter()
threaded_numbers = threaded_merge_sort(numbers.copy())
threaded_time = time.perf_counter() - start

# Display results
print("\nOriginal numbers:", numbers)
print("Sorted numbers:", sorted_numbers)

print("\n===== PERFORMANCE COMPARISON =====")
print(f"Normal Merge Sort: {normal_time:.6f} seconds")
print(f"Multithreaded Merge Sort: {threaded_time:.6f} seconds")

if normal_time < threaded_time:
    print("Normal Merge Sort was faster.")
elif threaded_time < normal_time:
    print("Multithreaded Merge Sort was faster.")
else:
    print("Both took approximately the same time.")

print("\nBoth algorithms produced the same result:",
      sorted_numbers == threaded_numbers)
