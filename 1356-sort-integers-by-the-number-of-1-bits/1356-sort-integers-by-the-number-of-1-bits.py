class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(arr)):
            l.append(bin(arr[i])[2:])
        m=[]
        for i in range(len(l)):
            k=l[i].count("1")
            m.append((k,arr[i]))
        m.sort()
        s=[]
        for i in m:
            s.append(i[1])
        return s


                    