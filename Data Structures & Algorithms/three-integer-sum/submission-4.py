class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for idx, i in enumerate(nums):
            if i > 0:
                break

            if idx > 0 and i == nums[idx - 1]:
                continue
            
            L, R = idx + 1, len(nums) - 1
            while L < R:
                sum = i + nums[L] + nums[R]
                if sum > 0:
                    R -= 1
                elif sum < 0:
                    L += 1
                else:
                    res.append([i, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return res