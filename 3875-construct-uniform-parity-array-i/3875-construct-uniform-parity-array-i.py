class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        nums2=[]
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if j!=i:
                    x=nums1[i]-nums1[j]
                    nums2.append(x)
                    break
        return True

        


        