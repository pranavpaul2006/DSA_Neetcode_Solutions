class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elem =set(nums)

        return len(nums) != len(unique_elem)
