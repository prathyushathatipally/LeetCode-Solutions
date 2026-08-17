class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        l1=[]
        l=[]
        for i in word:
            if i.isupper():
                l.append(i)
            elif i.islower():
                l1.append(i)
        c=0
        check=[]
        for i in l:
            if i not in check:
                if i.lower() in l1:
                    c+=1
                check.append(i)
        return c
