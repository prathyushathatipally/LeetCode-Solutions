class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=0
        result=""
        for i in s:
            if i=='(':
                if count>0:
                    result+=i
                count+=1
            else:
                count-=1
                if count>0:
                    result+=i
        return result        