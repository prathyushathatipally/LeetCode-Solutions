class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        c=0
        words=sentence.split()
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                c+=1
                if c==1:
                    return i+1
        return -1



            

        