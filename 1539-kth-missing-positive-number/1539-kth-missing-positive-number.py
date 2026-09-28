class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        i=1
        while count<k:
            if i not in arr:
                count+=1
            i=i+1
        return i-1      