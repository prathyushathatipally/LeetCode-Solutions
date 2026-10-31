class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="aeiou"
        while len(s)>0 and s[-1] in vowels:
            s=s[:-1]
        return s

        