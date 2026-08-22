class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words1=s1.split()
        words2=s2.split()
        l=[]
        for i in words1:
            if i not in words2 and words1.count(i)==1:
                l.append(i)
        l2=[]
        l1=[]
        for i in words2:
            if i not in words1 and words2.count(i)==1:
                l1.append(i)
        l2=l+l1
        return l2


