class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        n1 = length//2
        if((length % 2 ) == 0):
            out = (nums1[n1] + nums1[n1-1]) / 2
        else:
            out = (nums1[n1])

        return out

        