class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occupied = set() # can't use list cuz TLE
        for num in nums:
            if num in occupied:
                return True
            occupied.add(num)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
