class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        score=0
        v_c=0
        c_c=0
        vowels="aeiou"
        for i in s:
            if i in vowels:
                v_c+=1
            elif i.isalpha():
                c_c+=1
        if c_c==0:
            return 0
        else:
            score=v_c//c_c
        return score


        