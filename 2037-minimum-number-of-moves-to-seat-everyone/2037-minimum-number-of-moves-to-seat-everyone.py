class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats=sorted(seats)
        students=sorted(students)
        s=0
        for i in range(len(seats)):
            k=abs(seats[i]-students[i])
            s+=k
        return s

        
        
        