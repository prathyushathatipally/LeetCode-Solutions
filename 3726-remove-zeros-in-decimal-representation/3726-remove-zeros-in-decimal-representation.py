class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        k=str(n)
        for i in range(len(k)):
            if k[i]!="0":
                l.append(k[i])
        return int("".join(map(str,l)))

        