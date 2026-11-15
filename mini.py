
# DAA Mini Project: String Matching Algorithms

def naive_search(text, pattern):
    positions = []
    n = len(text)
    m = len(pattern)

    if m == 0:
        return positions

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            positions.append(i)

    return positions


def rabin_karp(text, pattern):
    positions = []
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return positions

    d = 256
    q = 101
    h = pow(d, m - 1, q)

    pattern_hash = 0
    text_hash = 0

    # Calculate initial hashes
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    # Search for the pattern
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                positions.append(i)

        # Calculate the next window hash
        if i < n - m:
            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

    return positions


# Input from user
text = input("Enter the main text: ")
pattern = input("Enter the pattern to search: ")

# Execute both algorithms
naive_result = naive_search(text, pattern)
rabin_result = rabin_karp(text, pattern)

# Display results
print("\n--- Naive String Matching ---")
print("Pattern found at indices:", naive_result)

print("\n--- Rabin-Karp Algorithm ---")
print("Pattern found at indices:", rabin_result)

# Compare results
if naive_result == rabin_result:
    print("\nBoth algorithms produced the same result.")
else:
    print("\nResults do not match.")
