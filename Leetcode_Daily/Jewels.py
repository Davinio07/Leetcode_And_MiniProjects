class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # logic 
        CheckedStones = set(jewels)
        JewelCounter: int = 0
        for stone in stones:
            if stone in CheckedStones:
                JewelCounter += 1 
        return JewelCounter
                

# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.numJewelsInStones("aA", "aAAbbbb")) 
# Expected: 3 
# (You have one 'a' and two 'A's in your stones, which are all jewels)

print("Test 2:", my_tester.numJewelsInStones("z", "ZZ")) 
# Expected: 0 
# (Case matters! 'z' is a jewel, but you only have 'Z' stones)