class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        k=[]
        for i in s:
            if len(k)>0 and k[-1]==i:
                k.pop()
            else:
                k.append(i)
        return "".join(map(str,k))
        