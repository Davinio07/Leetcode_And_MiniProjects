def isPalindrome(word):
    left = 0
    right = len(word) - 1
    
    while left < right:
        check: bool = word[left] == word[right]

        if check == True:
            left = left + 1
            right = right - 1
        else:
            return False        
    return True

# --- Test Cases ---
print(isPalindrome("racecar")) # Expected Output: True
print(isPalindrome("cloud"))   # Expected Output: False
print(isPalindrome("kayak"))   # Expected Output: True