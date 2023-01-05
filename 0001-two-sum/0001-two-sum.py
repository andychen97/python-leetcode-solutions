class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {};
        for i, element in enumerate(nums):
            possible = target - element
            if possible not in map:
                map[element] = i;
            else:
                return [map[possible], i];
