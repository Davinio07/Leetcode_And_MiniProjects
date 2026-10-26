class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = { ")": "(", "]": "[", "}": "{" }
        container: list = []
        for character in s:
            if character in "([{":
                container.append(character)
            else:
                if len(container) == 0:
                    return False
                
                peek = container[-1]
                if peek != matches[character]:
                    return False
                else:
                    container.pop()
        return len(container) == 0
                
                
                

# Test Case
Testing = Solution()
print("Test 1: ", Testing.isValid("()"))
# Expected Output: true 

print("Test 2: ", Testing.isValid("()[]{}"))
# Expected Output: true

print("Test 3: ", Testing.isValid("(]"))
# Expected Output: false

print("Test 4: ", Testing.isValid("["))