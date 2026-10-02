class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        columns=len(matrix[0])
        n=set()
        m=set()
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    n.add(i)
                    m.add(j)
        for i in n:
            for j in range(columns):
                matrix[i][j]=0
        for i in m:
            for j in range(rows):
                matrix[j][i]=0
        return matrix

