class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x [0])
        print(intervals)
        left, right = intervals[0][0],intervals[0][1]
        result = [] 
        for interval in intervals:
            left_new, right_new = interval[0], interval[1]
            if right >= left_new and right_new > right:
                right = right_new
            else:
                if right_new > right:
                    result.append([left, right])
                    left = left_new
                    right = right_new
        if result==[] or result[-1]!=[left, right]:
            result.append([left, right])
        return result