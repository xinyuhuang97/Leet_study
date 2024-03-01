class Solution:
    def hIndex(self, citations: List[int]) -> int:
        nb=len(citations)
        max_value=max(citations)
        for value in range(max_value, 0, -1):
            nb_passed=0
            for i in range(nb):
                if citations[i]>=value:
                    nb_passed+=1
                    if nb_passed>=value:
                        return value
        return 0
        