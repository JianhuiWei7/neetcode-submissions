class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def string2list(s):
            return_list = [0] * 26
            for char in s:
                return_list[ord(char) - ord("a")] += 1
            return return_list
        list1 = string2list(s)
        list2 = string2list(t)
        return list1 == list2
