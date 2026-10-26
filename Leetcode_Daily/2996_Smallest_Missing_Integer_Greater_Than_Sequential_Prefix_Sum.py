class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the sum of the longest sequential prefix (starting at nums[0])
        
        for i in range[nums]:
            return None
        
        # Step 2: Check if that sum is in the list. If True, add 1 until False.
        
        pass

# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.missingInteger([1,2,3,2,5])) 
# Expected: 6

print("Test 2:", my_tester.missingInteger([3,4,5,1,12,14,13])) 
# Expected: 15