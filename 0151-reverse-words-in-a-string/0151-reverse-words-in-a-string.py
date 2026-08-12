class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        words.reverse()
        k=" ".join(map(str,words))
        return k
        