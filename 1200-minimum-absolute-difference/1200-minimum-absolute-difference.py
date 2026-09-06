class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        k=sorted(arr)
        mini=k[1]-k[0]
        for i in range(1,len(k)-1):
            diff=k[i+1]-k[i]
            if diff<mini:
                mini=diff
        l=[]
        for i in range(len(k)-1):
            if k[i+1]-k[i]==mini:
                l.append((k[i],k[i+1]))
        return l

            

