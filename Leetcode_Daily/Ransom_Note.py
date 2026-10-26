def canConstruct(ransomNote, magazine):
    # Your logic goes here
    inventory = {}
    
    for letter in magazine:
        if letter in inventory:
            inventory[letter] += 1
        else:
            inventory[letter] = 1
    # return inventory

    for letter in ransomNote:
        if letter not in inventory or inventory[letter] == 0:
            return False
        else:
            inventory[letter] -= 1
    return True
# --- Test Cases ---
print("Test 1:", canConstruct("a", "b")) 
# Expected: False (Magazine doesn't have an 'a')

print("Test 2:", canConstruct("aa", "ab")) 
# Expected: False (Magazine has an 'a', but we need two!)

print("Test 3:", canConstruct("aa", "aab")) 
# Expected: True (Magazine has two 'a's and a 'b')