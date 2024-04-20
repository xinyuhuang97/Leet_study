class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intervals = sorted(points, key=lambda x: x [0])
        ans=[]
        for interval in intervals:
            if not ans or ans[-1][1]<interval[0]:
                ans.append(interval)
            else:
                ans[-1][0] = interval[0]
                ans[-1][1] = min(ans[-1][1], interval[1])
        return len(ans)