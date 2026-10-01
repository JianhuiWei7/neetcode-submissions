from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # 最大值候选人的下标
        result = []

        for right in range(len(nums)):
            left = right - k + 1

            # 1. 离开窗口的候选人，出队
            while q and q[0] < left:
                q.popleft()

            # 2. 新人更大或相等，淘汰队尾的旧候选人
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # 3. 新人加入队尾
            q.append(right)

            # 4. 窗口满了，队首就是最大值
            if left >= 0:
                result.append(nums[q[0]])

        return result