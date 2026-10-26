class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        og = x
        calculateNumbers = 0
        
        
        while x > 0:
            TakingLastNumber: int = x % 10
            x = x //10
            calculateNumbers = (calculateNumbers * 10) + TakingLastNumber
        return calculateNumbers == og
    
            
            
                
#testCase
testCase = Solution()

print("TEST1: ", testCase.isPalindrome(121))
print("TEST2: ", testCase.isPalindrome(-121))
print("TEST3: ", testCase.isPalindrome(-10))