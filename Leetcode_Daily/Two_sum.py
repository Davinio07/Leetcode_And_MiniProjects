class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Your logic goes here
        numberDic = {}
        
        for index, number in enumerate(nums):
            neededNum = target - number
            if  neededNum in numberDic:
                return [numberDic[neededNum], index]
            else:
                numberDic[number] = index
                

# --- How to test a Class in VS Code ---
# 1. Create a "Solution" object (Think of it like hiring a worker)
my_tester = Solution()

# 2. Hand the mock data to your worker
print("Test 1:", my_tester.twoSum([2, 7, 11, 15], 9)) 
# Expected: [0, 1]

print("Test 2:", my_tester.twoSum([3, 2, 4], 6)) 
# Expected: [1, 2]

print("Test 3:", my_tester.twoSum([3, 3], 6)) 
# Expected: [0, 1]