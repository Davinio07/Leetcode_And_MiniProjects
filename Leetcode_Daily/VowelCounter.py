# Write your count_vowels function here!
def count_vowels(word):
    Total: int = 0
    vowels = ["a","e","i","o","u"]
    for letter in word:
        if letter in vowels:
            Total = Total + 1
    return Total

# --- Test Cases ---
print("Vowels in 'cloud':", count_vowels("cloud")) 
# Expected Output: 2

print("Vowels in 'python':", count_vowels("python")) 
# Expected Output: 1

print("Vowels in 'engineer':", count_vowels("engineer")) 
# Expected Output: 4