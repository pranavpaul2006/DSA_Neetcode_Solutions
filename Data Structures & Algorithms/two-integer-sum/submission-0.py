class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map = {}
        for i,n in enumerate(nums):
            diff = target - n;
            if diff in dict_map:
                return [dict_map[diff] , i]
            dict_map[n] = i


        

        

