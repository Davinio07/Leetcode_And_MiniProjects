class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        WhereWeAt: int = 0
        for index, number in enumerate(nums):
            if number != val:
                nums[index] = number
                WhereWeAt += 1
        return WhereWeAt
                    


# Test Case
Testing = Solution()
print("Test 1: ", Testing.removeElement([3,2,2,3], 3) )
# Expected Output: 2

print("Test 2: ", Testing.removeElement([0,1,2,2,3,0,4,2], 2) )
# Expected Output: 5

print("Test 3: ", Testing.removeElement([4, 4, 4, 4], 4) )
# Expected Output: 0