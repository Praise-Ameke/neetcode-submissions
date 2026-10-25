class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


#i used a hash set to keep track of values i have already seen.
# Initialize an empty hash set to store seen values.
# Iterate through each number in the array.
# For each number:
# If it is already in the set, return true because a duplicate has been found.
# Otherwise, add it to the set.
# If the loop finishes without finding any duplicates, return false.