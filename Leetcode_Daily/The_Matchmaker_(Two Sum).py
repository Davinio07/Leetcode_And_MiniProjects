def twoSum(nums, target):
    notepad: dict = {}
    # Your logic goes here
    for index, num in enumerate(nums):
        minus = target- num
        if minus in notepad:
            return [notepad[minus], index]
        else:  notepad[num] = index
# --- Test Cases ---
print(twoSum([2, 7, 11, 15], 9)) # Expected Output: [0, 1] (because 2 + 7 = 9)
print(twoSum([3, 2, 4], 6))      # Expected Output: [1, 2] (because 2 + 4 = 6)
print(twoSum([3, 3], 6))         # Expected Output: [0, 1] (because 3 + 3 = 6)