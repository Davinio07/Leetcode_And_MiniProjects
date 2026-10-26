class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #logic
        MaxDupes = 0
        CurrentDupes = 0
        
        for numbers in nums:
            if numbers == 1:
                CurrentDupes +=1
            else:
                CurrentDupes = 0
            MaxDupes = max(MaxDupes, CurrentDupes)
        return MaxDupes

                
        
# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.findMaxConsecutiveOnes([1,1,0,1,1,1])) 
# Expected: 3

print("Test 2:", my_tester.findMaxConsecutiveOnes([1,0,1,1,0,1])) 
# Expected: 2
