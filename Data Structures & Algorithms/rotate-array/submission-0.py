class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the array to the right by k steps in-place.
        """
        n = len(nums)
        k %= n  # handle cases where k > n

        # Step 1: Reverse the whole array
        nums.reverse()

        # Step 2: Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the rest (n - k) elements
        nums[k:] = reversed(nums[k:])