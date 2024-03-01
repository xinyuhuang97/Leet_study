"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nb=len(gas)
        if sum(gas) < sum(cost): return -1 
        for i in range(nb):
            tank=gas[i]
            if tank==0:
                continue
            now=i
            while True:
                c=cost[now%(nb)]
                if c>tank:
                    break
                else:
                    now=(now+1)%(nb)
                    tank=tank-c+gas[(now)%(nb)]
                    if now==i:
                        return i             
        return -1
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        nb=len(gas)
        if sum(gas) < sum(cost): return -1 
        tank,index=0,0
        for i in range(nb):
            tank+=gas[i]-cost[i]
            if tank<0:
                tank=0
                index=i+1
        return index
                
