class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxMoney = 0
        for bank in accounts:
            total = sum(bank)
            maxMoney = max(total,maxMoney)
        return maxMoney
        

# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.maximumWealth([[1,2,3], [3,2,1]])) 
# Expected: 6

print("Test 2:", my_tester.maximumWealth([[1,5], [7,3], [3,5]])) 
# Expected: 10