class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = {}
        for char in s1:
            if char in target_dict:
                target_dict[char] += 1
            else:
                target_dict[char] = 1

        len_target = len(s1)
        current_window_dict = {}
        if len(s2) < len_target:
            return False
        left = 0
        right = len_target - 1
        for i in range(left, len_target):
            if s2[i] not in current_window_dict:
                current_window_dict[s2[i]] = 1
            else:
                current_window_dict[s2[i]] += 1
        while right < len(s2) - 1:
            if current_window_dict == target_dict:
                return True
            else:
                left_element = s2[left]
                right_element = s2[right + 1]
                current_window_dict[left_element] -= 1
                if current_window_dict[left_element] == 0:
                    del current_window_dict[left_element]

                if right_element in current_window_dict:
                    current_window_dict[right_element] += 1
                else:
                    current_window_dict[right_element]  = 1
            right += 1
            left += 1
        if current_window_dict == target_dict:
            return True
        else:
            return False
        


