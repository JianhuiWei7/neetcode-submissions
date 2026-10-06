class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char2index = {}
        output_res = []
        used_letter = set()
        for index, char in enumerate(s):
            if char not in char2index:
                char2index[char] = [index]
            else:
                char2index[char].append(index)
        for char in char2index:
            if char in used_letter:
                continue
            used_letter.add(char)
            left = char2index[char][0]
            right = char2index[char][-1]
            next_iteration = 1
            while next_iteration:
                next_iteration = 0
                for sub_char in s[left:right+1]:
                    if sub_char not in used_letter:
                        used_letter.add(sub_char)
                        new_left = char2index[sub_char][0]
                        new_right = char2index[sub_char][-1]
                        left = min(left,new_left)
                        right = max(right,new_right)
                        next_iteration = 1
                    else:
                        continue
            output_res.append(right-left+1)
        return output_res


            