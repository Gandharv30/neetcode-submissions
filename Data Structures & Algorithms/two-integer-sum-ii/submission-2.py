class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l,r = i, len(numbers) - 1
            tar=target - numbers[l]

            while l <= r:
                mid = (l+r)//2
                if numbers[mid] == tar:
                    return[i+1,mid+1]
                elif numbers[mid] > tar:
                    r = mid - 1
                else:
                    l = mid + 1
        return []