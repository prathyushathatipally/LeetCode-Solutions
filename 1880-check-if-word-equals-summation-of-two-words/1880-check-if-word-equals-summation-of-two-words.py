class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        l=[]
        l1=[]
        l2=[]
        for i in firstWord:
            l.append(ord(i)-ord('a'))
        for i in secondWord:
            l1.append(ord(i)-ord('a'))
        for i in targetWord:
            l2.append(ord(i)-ord('a'))
        l=list(map(str,l))
        k="".join(l)
        k=int(k)
        l1=list(map(str,l1))
        s="".join(l1)
        s=int(s)
        l2=list(map(str,l2))
        t="".join(l2)
        t=int(t)
        if k+s==t:
            return True
        return False


        