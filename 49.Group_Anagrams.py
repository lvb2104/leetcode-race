# sorting for transform [strings] to the [same string] and store them at the [same string] for those [strings]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list) # create a dict with default value is a list
        for str in strs:
            temp = ''.join(sorted(str))
            dict[temp].append(str)
        return list(dict.values())