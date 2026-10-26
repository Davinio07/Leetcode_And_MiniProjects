def reverseString(s):
    # Your logic goes here
    left = 0
    right = len(s) -1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1

# --- Test Cases ---
# Notice we don't print the function itself. 
# We run the function to modify the list, then print the list!

word1 = ["h","e","l","l","o"]

reverseString(word1)
print(word1) 
# Expected Output: ['o', 'l', 'l', 'e', 'h']

word2 = ["C","l","o","u","d"]
reverseString(word2)
print(word2) 
# Expected Output: ['d', 'u', 'o', 'l', 'C']

'''
#test
blockA: [] = [1,2,3,4,5]
blockB: [] = ["a","b","c","d","e"]
print(blockA)

blockA[1], blockB[4] = blockB[4], blockA[1]
print(f'this is the final printfor BlockA',blockA )
print(f'this is the final printfor BlockB',blockB )
'''