class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course2pre = [0 for _ in range(numCourses)]
        pre2course = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            course2pre[course] += 1
            pre2course[pre].append(course)
        num_finish = 0
        queue = []
        for index, course in enumerate(course2pre):
            if course == 0:
                queue.append(index)
        while queue:
            course = queue.pop()
            num_finish += 1
            for item in pre2course[course]:
                course2pre[item] -= 1
                if course2pre[item] == 0:
                    queue.append(item)
        return num_finish == numCourses