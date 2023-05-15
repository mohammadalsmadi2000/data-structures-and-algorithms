# Validate Brackets

## Problem Domain
The "Validate Brackets" function takes a string as input and determines whether or not the brackets in the string are balanced. The function checks for three types of brackets: round brackets (), square brackets [], and curly brackets {}. The function returns a boolean value representing whether the brackets are balanced or not.

A string with balanced brackets contains opening brackets that are properly closed with corresponding closing brackets. For example, the string {}()[] has balanced brackets, while the string ([)] does not.

## Algorithm 
 
The algorithm used to solve the problem can be described as follows:

1. Initialize an empty stack to keep track of opening brackets encountered.
2. Iterate through each character in the input string.
3. If the character is an opening bracket ((, {, or [), push it onto the stack.
4. If the character is a closing bracket (), }, or ]), do the following:
* Check if the stack is empty. If it is, return False since there is no corresponding opening bracket for the closing bracket.
* Pop the top element from the stack and check if it matches the closing bracket. If it doesn't, return False

5. After iterating through all the characters, check if the stack is empty. If it is, return True; otherwise, return False.

## Big O Analysis

The time complexity of this algorithm is O(n), where n is the length of the input string. This is because we iterate through each character in the string exactly once.

The space complexity of the algorithm is O(n) as well. In the worst case, if all characters in the string are opening brackets, they will be stored in the stack.