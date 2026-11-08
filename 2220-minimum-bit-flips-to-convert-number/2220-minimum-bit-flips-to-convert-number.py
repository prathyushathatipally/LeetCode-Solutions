class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        s=bin(start)[2:]
        k=bin(goal)[2:]
        length=max(len(s),len(k))
        l=s.zfill(length)
        m=k.zfill(length)
        for i in range(len(l)):
            if l[i]!=m[i]:
                c+=1
        return c


        for i in range(len(l)):
            if l[i]!=m[i]:
                c+=1
        return c


                


