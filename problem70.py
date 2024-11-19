'''You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step'''

class Solution:
    def climbStairs(self, noOfSteps: int) -> int:
        if noOfSteps == 1:
            return 1
        elif noOfSteps == 2:
            return 2

        prev2 = 1
        prev1 = 2
        
        for step in range(3, noOfSteps+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1

solution = Solution()
noOfSteps = 3
print(f"There are {solution.climbStairs(noOfSteps)} ways to climb the stairs.")