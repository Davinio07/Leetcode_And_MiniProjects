# Write your get_evens function here!
def get_evens(numbers):
    evenNumbers = []
    unEvenNumbers = []
    for i in numbers:
        if i % 2 == 0:
            evenNumbers.append(i)
            print(i, " Is even")
        else:
            unEvenNumbers.append(i)
            print(i, " Is uneven")
            
    return print("All even numbers: ", evenNumbers)



# --- Test Cases ---
print(get_evens([1, 2, 3, 4, 5, 6])) 
# Expected Output: [2, 4, 6]

print(get_evens([10, 15, 20, 25]))   
# Expected Output: [10, 20]

print(get_evens([1, 3, 5, 7]))       
# Expected Output: []