class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        # logic
        checkedLetters = set()
        for letters in s:
            if letters in checkedLetters:
                return letters
            else:
                checkedLetters.add(letters)



# --- Test Cases ---
my_tester = Solution()

print("Test 1:", my_tester.repeatedCharacter("abccbaacz"))
# Expected: "c" (because 'c' is the first letter to appear a second time)

print("Test 2:", my_tester.repeatedCharacter("abcdd"))
# Expected: "d"

print("Test 3:", my_tester.repeatedCharacter("abcadef"))
# Expected: "a"