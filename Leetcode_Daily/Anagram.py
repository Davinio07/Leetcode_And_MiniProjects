def isAnagram(word1, word2):
    # Your logic goes here
    Word1Dictionairy = {}
    Word2Dictionairy = {}
    
    for letter in word1:
        if letter in Word1Dictionairy:
            Word1Dictionairy[letter] += 1
        else: 
            Word1Dictionairy[letter] = 1

    for letter in word2:
        if letter in Word2Dictionairy:
            Word2Dictionairy[letter] += 1
        else: 
            Word2Dictionairy[letter] = 1
            
    if Word1Dictionairy == Word2Dictionairy:
        return True
    else: return False           
# --- Test Cases ---
print("Test 1:", isAnagram("anagram", "nagaram")) 
# Expected: True

print("Test 2:", isAnagram("rat", "car")) 
# Expected: False

print("Test 3:", isAnagram("a", "ab")) 
# Expected: False