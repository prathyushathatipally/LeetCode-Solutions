class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l=[]
        for i in range(m):
            l.append(nums1[i])
        for j in range(n):
            l.append(nums2[j])
        l.sort()
        nums1[:]=l


        