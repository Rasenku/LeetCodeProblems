# In a list, return the fifth largest problem

nums = [2, 3, 76, 1, 34, 98, 45, 2, 8]

def fifthLargest(nums):
    """
    Returns the fifth largest number in a array of n numbers
    """
    nums.sort()
    return nums[-5]

fifthLargest(nums)
