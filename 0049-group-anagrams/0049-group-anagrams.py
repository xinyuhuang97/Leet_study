from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            memo[sorted_word].append(word)
        for key in memo:
            result.append(memo[key])
        return result
        