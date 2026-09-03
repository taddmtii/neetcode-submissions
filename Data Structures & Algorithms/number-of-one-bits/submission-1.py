class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # integers are represented with 32 bits.
        for i in range(32):
            # Create mask with only ith bit set. Check to see if its set and if it is add to count
            if (1 << i) & n:
                res += 1
        return res