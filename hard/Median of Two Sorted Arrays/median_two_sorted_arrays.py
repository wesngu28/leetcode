class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list =  nums1 + nums2
        merged_list.sort()
        if((len(merged_list) % 2) == 0):
            first_mid = merged_list[round((len(merged_list)/2))]
            second_mid = merged_list[round(len(merged_list)/2)-1]
            return (first_mid+second_mid)/2
        return merged_list[round(((len(merged_list)-1)/2))]