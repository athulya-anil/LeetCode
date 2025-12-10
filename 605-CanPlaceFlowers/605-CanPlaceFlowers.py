# Last updated: 10/12/2025, 07:41:29
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        length = len(flowerbed)

        while i < length and n > 0:
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    i += 2
                    continue

            i += 1

        return n == 0
