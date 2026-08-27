class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    c+=1
        return c

        