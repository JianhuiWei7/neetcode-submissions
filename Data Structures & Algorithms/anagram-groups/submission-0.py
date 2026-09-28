class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list2group = {}
        def string2orderstr(s):
            return "".join(sorted(s))
        for sub_str in strs:
            sublist = string2orderstr(sub_str)
            if sublist not in list2group:
                list2group[sublist] = [sub_str]
            else:
                list2group[sublist].append(sub_str)
        return list(list2group.values())