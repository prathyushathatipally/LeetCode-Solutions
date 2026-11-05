class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        c=0
        k=[]
        s=sum(apple)
        k=sorted(capacity,reverse=True)
        for i in range(len(k)):
            s=s-k[i]
            c+=1
            if s<=0:
                break
        return c

        