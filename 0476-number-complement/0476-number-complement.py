class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=bin(num)
        k=str(s)
        result=""
        for i in s:
            if i=="1":
                result+="0"
            elif i=="0":
                result+="1"
            else:
                result+=str(i)
        m=int(result[2:],2)
        return m


        