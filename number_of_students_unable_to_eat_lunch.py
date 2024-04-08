class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        c = 0
        while len(sandwiches) > 0:
            size = len(students)
            for x in students:
                if x == sandwiches[0]:
                    students.remove(x)
                    sandwiches.remove(x)
            if len(students) == size:
                break
        return len(students)