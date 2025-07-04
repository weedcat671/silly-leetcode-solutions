'''
    Solution for "Search in Rotated Sorted Array" problem
    https://leetcode.com/problems/search-in-rotated-sorted-array
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        if l < len(nums) and nums[l] == target:
            return l
        elif r < len(nums) and nums[r] == target:
            return r
        return -1