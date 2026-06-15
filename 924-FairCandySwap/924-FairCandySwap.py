# Last updated: 14/06/2026, 23:02:49
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA=sum(aliceSizes)
        sumB=sum(bobSizes)

        diff=(sumA-sumB)//2
        aliceSet=set(aliceSizes)

        for b in bobSizes:
            a = b + diff
            if a in aliceSizes:
                return [a,b]



        