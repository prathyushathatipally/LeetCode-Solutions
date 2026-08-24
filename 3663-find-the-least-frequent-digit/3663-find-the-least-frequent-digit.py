class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=list(map(int,str(n)))
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        minimum=min(d.values())
        for key in sorted(d):
            if d[key]==minimum:
                return key



        