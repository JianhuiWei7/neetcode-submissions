class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        relations = [[] for _ in range(numCourses)] 
        learning_order = []
        queue = deque()
        pre_to_course = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            relations[course].append(prereq)
            pre_to_course[prereq].append(course)

        for index, course in enumerate(relations):
            if course == []:
                queue.append(index)
        while queue:
            learning_order.append(queue.popleft())
            for course_to_del in pre_to_course[learning_order[-1]]:
                relations[course_to_del].remove(learning_order[-1])
                if relations[course_to_del] == []:
                    queue.append(course_to_del)
        if len(learning_order) != numCourses:
            return []
                

        return learning_order

            