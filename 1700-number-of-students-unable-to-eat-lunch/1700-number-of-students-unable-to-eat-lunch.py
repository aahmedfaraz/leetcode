class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        found = True
        s = 0

        while found:
            found = False
            for i in range(n):
                if students[i] == sandwiches[s]:
                    print(i, s)
                    students[i] = -1
                    found = True
                    s += 1
                    if s == n:
                        return 0
        
        count = 0
        for num in students:
            if num != -1:
                count += 1

        return count


