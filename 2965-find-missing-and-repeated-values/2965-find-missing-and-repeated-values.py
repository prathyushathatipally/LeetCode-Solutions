class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                l.append(grid[i][j])
        m=[]
        for i in range(len(l)):
            if l.count(l[i])==2:
                m.append(l[i])
        s=[]
        for i in m:
            if i not in s:
                s.append(i)
        start=1
        end=len(l)
        k=[]
        for i in range(start,end+1):
            k.append(i)
        j=[]
        for i in range(len(k)):
            if k[i] not in l:
                j.append(k[i])
        return s+j





        