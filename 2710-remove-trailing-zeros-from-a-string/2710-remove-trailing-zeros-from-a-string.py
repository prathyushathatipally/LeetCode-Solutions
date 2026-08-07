class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        while num[-1]=='0':
            num=num[:-1]
        if num[-1]!=0:
            return num
        return num
