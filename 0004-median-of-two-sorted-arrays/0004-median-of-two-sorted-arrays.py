class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k=nums1+nums2
        s=sorted(k)
        t=len(s)
        if t%2==1:
            return s[t//2]
        else:
            return (s[t//2-1]+s[t//2])/2.0
        