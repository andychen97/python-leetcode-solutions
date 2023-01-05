class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {};
        for i, n in enumerate(nums):
            possible = target - n
            if possible not in map:
                map[n] = i;
            else:
                return [map[possible], i];
