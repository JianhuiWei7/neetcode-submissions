class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        returned_res = []
        path = []

        def dfs(remaining, index):
            if remaining == 0:
                returned_res.append(path.copy())
                return

            for i in range(index, len(candidates)):
                # 同一层中，相同数字只作为起点选择一次
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                item = candidates[i]
                if item > remaining:
                    break  # 已排序，后面的数字也不可能满足

                path.append(item)
                dfs(remaining - item, i + 1)
                path.pop()

        dfs(target, 0)
        return returned_res