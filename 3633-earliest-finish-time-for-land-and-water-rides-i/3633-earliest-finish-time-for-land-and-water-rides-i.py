class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        totalL = len(landStartTime)
        totalW = len(waterStartTime)

        mint = float('inf')

        # land to water
        for l in range(totalL):
            for w in range(totalW):
                time = landStartTime[l] + landDuration[l]
                if waterStartTime[w] > time:
                    time = waterStartTime[w]
                time += waterDuration[w]
                mint = min(mint, time)
        # water to land
        for w in range(totalW):
            for l in range(totalL):
                time = waterStartTime[w] + waterDuration[w]
                if landStartTime[l] > time:
                    time = landStartTime[l]
                time += landDuration[l]
                mint = min(mint, time)
        
        return mint