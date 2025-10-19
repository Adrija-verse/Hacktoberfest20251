class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot point (min value in the nums)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1
        pivot = left 

        # search in the left/right side of pivot 
        if target > nums[-1]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid 
        return -1 
        
        
