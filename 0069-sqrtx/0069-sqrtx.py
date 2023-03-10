class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        l = 0
        r = x
        while l <= r:
            mid = (r + l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid