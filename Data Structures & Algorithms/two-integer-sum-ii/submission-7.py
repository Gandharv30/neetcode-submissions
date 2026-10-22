class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for n in range(len(numbers)):
            diff = target - numbers[n]

            if diff in hashmap:
                return [hashmap[diff],n + 1]
            hashmap[numbers[n]] = n + 1

        