class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        for i in range(len(arr1)):
            k=0
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    k+=1
            if k==0:
                c+=1
        return c

