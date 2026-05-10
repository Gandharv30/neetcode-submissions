class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i,0) + 1

        indx = 0
        for color in range(3):
            freq = hash_map.get(color,0)
            nums[indx:indx+freq] = [color] *  freq
            indx +=  freq
        