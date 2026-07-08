class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Better approach
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in nums_map or nums_map[diff] == i: 
                continue
            return [i, nums_map[diff]]
        return []
