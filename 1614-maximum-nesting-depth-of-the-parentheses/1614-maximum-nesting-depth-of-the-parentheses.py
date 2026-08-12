class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        maximum=0
        for i in s:
            if i=='(':
                c+=1
                if c>maximum:
                    maximum=c
            elif i==')':
                c-=1
        return maximum



        