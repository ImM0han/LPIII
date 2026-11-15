
import heapq

def huffman_encoding(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    heap = [[freq[ch], ch, None, None] for ch in freq]
    heapq.heapify(heap)

    if len(heap) == 1:
        return {heap[0][1]: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = [
            left[0] + right[0],
            left[1] + right[1],
            left,
            right
        ]

        heapq.heappush(heap, new_node)

    codes = {}

    def generate_codes(node, code):
        if node[2] is None and node[3] is None:
            codes[node[1]] = code
            return

        generate_codes(node[2], code + "0")
        generate_codes(node[3], code + "1")

    generate_codes(heap[0], "")

    return codes


text = input("Enter a string: ")

if text == "":
    print("Please enter a valid string.")
else:
    codes = huffman_encoding(text)

    print("\nHuffman Codes:")
    for ch, code in codes.items():
        print(ch, ":", code)

    encoded = "".join(codes[ch] for ch in text)

    print("\nEncoded String:", encoded)





# Enter a string: banana

# Huffman Codes:
# b : 10
# a : 0
# n : 11

# Encoded String: 100110110