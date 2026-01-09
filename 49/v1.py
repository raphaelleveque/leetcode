class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict: [sorted str : list of strs]
        hashmap = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            hashmap[sorted_str].append(s)
        return list(hashmap.values())

        
