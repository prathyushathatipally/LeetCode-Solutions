class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        l=[]
        for i in range(len(number)):
            if number[i]==digit:
                t=number[:i]+number[i+1:]
                l.append(t)
        return max(l)
        