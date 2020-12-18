class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for x in range(len(flowerbed)):
            bed = flowerbed[x]
            if x > 0 and flowerbed[x - 1] == 1:
                continue
            if x < (len(flowerbed) - 1) and flowerbed[x + 1] == 1:
                continue
            if bed == 0:
                flowerbed[x] = 1
                n -= 1
            if n < 1:
                return True
        return False