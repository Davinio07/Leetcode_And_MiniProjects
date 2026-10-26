class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for currentNumber in nums:
            smallerCount = 0
            for compareNumber in nums:
                if compareNumber < currentNumber:
                    smallerCount +=1
            result.append(smallerCount)
        return result
        
        
# Test Case

my_tester = Solution()

print("Test 1: ", my_tester.smallerNumbersThanCurrent([8,1,2,2,3]))

print("Test 2: ", my_tester.smallerNumbersThanCurrent([6,5,4,8]))