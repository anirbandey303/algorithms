"""Evaluate Reverse Polish Notation
Solved 
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100]."""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            # print(stack)
            if (i == "+" or i == "-" or i == "*" or i == "/"):
                A = int(stack.pop())
                B = int(stack.pop())
                if (i == "+"):
                    stack.append(B + A)
                elif (i == "-"):
                    stack.append(B - A)
                elif (i == "*"):
                    stack.append(B * A)
                else:
                    stack.append(int(B/A))
            else:
                stack.append(int(i))
        return stack[-1]