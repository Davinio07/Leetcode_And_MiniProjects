def containsDuplicate(nums):
    seenNumbers = set()
    num: int
    
    for num in nums:
        if num in seenNumbers:
            return True
        else: seenNumbers.add(num)
        
    return False

# --- Test Cases ---
# Run your file. If your logic is right, the output should be what is in the comments.

print(containsDuplicate([1, 2, 3, 1]))       # Expected Output: True
print(containsDuplicate([1, 2, 3, 4]))       # Expected Output: False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # Expected Output: True