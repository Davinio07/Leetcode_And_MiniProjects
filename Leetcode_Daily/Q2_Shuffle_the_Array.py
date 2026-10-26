class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # logic
        shuffled_deck = []
        
        for i in range(n):
            shuffled_deck.append(nums[i])
            shuffled_deck.append(nums[i + n])
        return shuffled_deck
            

# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.shuffle([2, 5, 1, 3, 4, 7], 3)) 
# Expected: [2, 3, 5, 4, 1, 7]

print("Test 2:", my_tester.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)) 
# Expected: [1, 4, 2, 3, 3, 2, 4, 1]

print("Test 3:", my_tester.shuffle([1, 1, 2, 2], 2)) 
# Expected: [1, 2, 1, 2]