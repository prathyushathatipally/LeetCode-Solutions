class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        for i in s:
            if i.isdigit():
                l.append(i)
        l1=[]
        for i in l:
            if i not in l1:
                l1.append(i)
        s=sorted(l1)
        k=list(map(int,s))
        if len(k)<2:
            return -1
        return k[-2]

        