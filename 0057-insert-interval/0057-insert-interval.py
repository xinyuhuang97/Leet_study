class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]
        if newInterval == []:
            return intervals
        newlist=[]
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                if newInterval[1] >= intervals[i][0]:
                    newInterval= [newInterval[0], max(newInterval[1],intervals[i][1]) ] 
                else:
                    return newlist + [newInterval] +  intervals[i:]
            else:
                if intervals[i][1]>newInterval[1]:
                    return intervals
                elif intervals[i][1]<newInterval[0]:
                    newlist.append(intervals[i])
                else:
                    newInterval= [intervals[i][0], max(newInterval[1],intervals[i][1]) ] 
                    
        return newlist+[newInterval]
        