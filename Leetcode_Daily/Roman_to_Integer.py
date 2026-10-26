class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translation = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        container_Translated: list = []
        
        for letter in s:
            if len(container_Translated) == 0:
                container_Translated.append(translation[letter])
            else:
                if translation[letter] > container_Translated[-1]:
                    result = translation[letter] - container_Translated[-1]
                    container_Translated.pop()
                    container_Translated.append(result)
                     
                else:
                    container_Translated.append(translation[letter])
        return sum(container_Translated)
            


# Test Case
Testing = Solution()
print("Test 1: ", Testing.romanToInt("III") )
# Expected Output: 3 

print("Test 2: ", Testing.romanToInt("LVIII") )
# Expected Output: 58

print("Test 3: ", Testing.romanToInt("MCMXCIV") )
# Expected Output: 1994

print("Test 4: ", Testing.romanToInt("VI") )
# Expected Output: 6

print("Test 5: ", Testing.romanToInt("IV") )
# Expected Output: 4

