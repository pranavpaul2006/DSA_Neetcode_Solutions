class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set()
        for num in nums:
            set_nums.add(num)

        res, count = 1,1
        if not nums:
            return 0
        for num in nums:
            if (num-1) in set_nums:
                continue
            else:
                count = 1
                temp = num
                while (temp+1) in set_nums:
                    count +=1
                    temp +=1
                    res = max(res , count)
        return res

             

            