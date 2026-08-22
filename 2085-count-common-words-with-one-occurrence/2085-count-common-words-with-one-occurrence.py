class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        l=[]
        for i in words1:
            if words1.count(i)==1:
                l.append(i)
        l1=[]
        for i in words2:
            if words2.count(i)==1:
                l1.append(i)
        common=[]
        c=0
        for i in l:
            if i in l1:
                common.append(i)
                c+=1
        return c

        