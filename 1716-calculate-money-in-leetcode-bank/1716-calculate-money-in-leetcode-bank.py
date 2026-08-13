class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in range(n):
            week=i//7
            day=i%7
            s+=week+day+1
        return s
      

           
            
        