class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []

        for i in range(n + 1):
            c = 0
            while i > 0:
                c += i % 2
                i = i // 2
            l.append(c)

        return l
        