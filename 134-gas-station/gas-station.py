class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        sgas=0
        scost=0
        index=0
        for i in range(0,len(gas)):
            sgas+=gas[i]
            scost+=cost[i]
            if sgas<scost:
                sgas=0
                scost=0
                index=i+1
        return index    