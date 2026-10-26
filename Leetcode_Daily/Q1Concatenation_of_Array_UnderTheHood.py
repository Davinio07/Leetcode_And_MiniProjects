class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # logic
        storage = []
        for i in nums:
            storage.append(i)
        for i in nums:
            storage.append(i)
        return storage
        
            

# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.getConcatenation([1, 2, 1])) 
# Expected: [1, 2, 1, 1, 2, 1]

print("Test 2:", my_tester.getConcatenation([1, 3, 2, 1])) 
# Expected: [1, 3, 2, 1, 1, 3, 2, 1]