class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(details)):
            k=details[i][11:13]
            if int(k)>60:
                c+=1
        return c





        