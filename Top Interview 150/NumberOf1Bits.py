class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)[2:]
        count = binary_string.count('1')
        return count
