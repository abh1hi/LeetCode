#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1[0:] + nums2[0:])
        length = len(nums)
        if length %2  == 0.00:
            median  = (nums[int(length/2 -1)] + nums[int(length/2)])/2
            return median
        else :
            median  = nums[int(len(nums)/2)]
            return median
