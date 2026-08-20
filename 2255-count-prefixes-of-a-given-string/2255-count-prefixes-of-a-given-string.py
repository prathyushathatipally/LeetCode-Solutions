class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(len(words)):
            if s.startswith(words[i]):
                c+=1
        return c        