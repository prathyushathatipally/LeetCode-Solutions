class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l=[]
        for i in range(len(letters)):
            if letters[i]>target:
                l.append(letters[i])
                break
        if len(l)==0:
            return letters[0]
        return "".join(l)
        

        