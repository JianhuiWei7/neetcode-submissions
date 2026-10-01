class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        window = {}
        formed = 0
        required = len(target)

        left = 0
        best_start = 0
        best_len = float("inf")

        for right, char in enumerate(s):
            if char in target:
                window[char] = window.get(char, 0) + 1

                # 从“不够”变成“刚好够”，才增加满足的种类数
                if window[char] == target[char]:
                    formed += 1

            while formed == required:
                length = right - left + 1
                if length < best_len:
                    best_start = left
                    best_len = length

                removed = s[left]
                if removed in target:
                    # 移除前刚好够，移除后就不够了
                    if window[removed] == target[removed]:
                        formed -= 1
                    window[removed] -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]