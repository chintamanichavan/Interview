class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(sandwiches)
        q = deque(students)

        while st and q:
            # for the cur try all students
            no_one = True
            for i in range(len(q)):
                if st[0] == q[0]:
                    q.popleft()
                    st.popleft()
                    no_one = False
                    break
                else:
                    q.append(q.popleft())
            if no_one:
                return len(q)

        return 0


