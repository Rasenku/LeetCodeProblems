# Given an array of integers, return indices of the two numbers such that they add up to a specific target


# 1. Restate the problem
#   So you have a list and you want to return the value of two numbers so they add up to a target
# 2. Ask Clarifying Questions
    # Can I use 2 arrays? Will the output be an integer?
# 3. State Assumptions
#   Can I assume that eahc input would have exactly one solution? Can I sue the same element twice?
# 4. Think Out Loud
# 4a. Brainstorm Solutions
#   I could use an hash Table to reduce the time complexity and make a class to make a function to find the target value
# 4b. Explain Your Rationale
#   Just trying to find the sum in the index so could do a for loop
# 4c. Discuss Tradeoffs
# 4d.Suggest Improvements


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index,value in enumerate(nums):
            if target-value in h:
                return[index,h[target-value]]
            h[value] = index
