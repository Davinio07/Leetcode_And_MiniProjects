class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Missing_Numbers: list = []
        Full_number_List = len(nums)
        
        TurnedIntoSet: set = set(nums)
        
        for i in range(1, Full_number_List + 1):
            if i not in TurnedIntoSet:
                Missing_Numbers.append(i)
        return Missing_Numbers
            
        
        
# testCase

MyTest = Solution()

print("Test1: ", MyTest.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print("Test2: ", MyTest.findDisappearedNumbers([1,1]))