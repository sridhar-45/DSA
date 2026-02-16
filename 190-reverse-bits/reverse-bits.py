class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = format(n, "032b")  # Force 32 bits
        reversed_string = binary_string[::-1]
        return int(reversed_string, 2)
