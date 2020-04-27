"""
Given a list of n numbers, determine if it contains any duplicate numbers.
"""

# setup test variables
nums = [1, 23, 4, 52, 12, 4, 0, 5]

# write function
def duplicates(nums):
    """
    # description
    Vars: {nums: list}
    """
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            print("The duplicate is:" , nums[i])
            return nums[i]


# Testing...
duplicates(nums)
