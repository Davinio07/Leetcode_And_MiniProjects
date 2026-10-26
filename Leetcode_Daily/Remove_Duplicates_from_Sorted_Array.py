class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory: int = 1
        for index, number in enumerate(nums):
            if index > 0:
                previous_number: int = nums[index - 1]
                if previous_number != number:
                    nums[memory] = number
                    memory +=1
        return memory
                    
        



# Test Case
Testing = Solution()
print("Test 1: ", Testing.removeDuplicates([1,1,2]) )
# Expected Output: k = 2 

print("Test 2: ", Testing.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) )
# Expected Output: k = 5

print("Test 3: ", Testing.removeDuplicates([7, 7, 7, 7, 7]) )
# Expected Output: k = 1

print("Test 4: ", Testing.removeDuplicates([-5, -1, 0, 3, 8]) )
# Expected Output: k = 5