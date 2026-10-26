class Solution(object):
    def findErrorNums(self, nums):
        numberContainer = set()
        missingNumber = 0
        nLenght = len(nums)
        duplicate = 0

        for number in nums:
            if number in numberContainer:
                duplicate = number
            else:
                numberContainer.add(number)
                
        for number in range(1, nLenght +1):
            if number not in numberContainer:
                missingNumber = number
        return [duplicate, missingNumber]

# Test Case
Testing = Solution()
print("TestCase:", Testing.findErrorNums([1, 2, 2, 4]))  # Output: 2