# Given a 32-bit signed integer, reverse digits of an integer.



# 1. Restate the problem
#   So we have a 32 bit number and want to return it in reverse
# 2. Ask Clarifying Questions
    # Can I return 2 of the same integers? Does it have to come back signed?
# 3. State Assumptions
#   Can I assume  we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# 4. Think Out Loud
# 4a. Brainstorm Solutions
#   We can build up the reverse integer one digit at a time. While doing so, we can check beforehand whether or not appending another digit would cause overflow.
#We want to repeatedly "pop" the last digit off of xx and "push" it to the back of the \text{rev}rev. In the end, \text{rev}rev will be the reverse of the xx.
# 4b. Explain Your Rationale
#   Reversing an integer can be done similarly to reversing a string.
# To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.
# 4c. Discuss Tradeoffs
# 4d.Suggest Improvements


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0
