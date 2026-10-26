class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_lenght = len(needle)
        for index, letter in enumerate(haystack):
            wordcheck = haystack[index : index + needle_lenght]
            if wordcheck == needle:
                return index
        return -1

# Test Case
Testing = Solution()
print("Test 1: ", Testing.strStr("sadbutsad", "sad") )
# Expected Output: 0

print("Test 2: ", Testing.strStr("leetcode", "leeto") )
# Expected Output: -1

print("Test 2: ", Testing.strStr("leetcode", "code") )
# Expected Output: 1