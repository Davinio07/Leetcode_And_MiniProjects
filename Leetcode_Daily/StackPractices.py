def The_Score_Tracker():
    logs = ["Alice-10", "Bob-20", "Alice-15", "Charlie-5"]
    total_score = 0

    for score in logs:
        name, points = score.split("-")
        points = int(points)
        total_score += points
    print(total_score)

    # Expected Output: 50
    
def The_Undo_Button():
    actions = ["H", "e", "l", "undo", "l", "o", "undo", "p"]
    stack = []

    for letter in actions:
        if letter == "undo":
            stack.pop()
        else:
            stack.append(letter)
    return stack
    # Expected Output: ['H', 'e', 'l', 'p']

def The_Lap_Timer():
    timestamps = [2, 7, 10, 15]
    previous_time = 0
    current_time = 0

    # Your code goes here...
    for lap in timestamps:
        current_time = lap - previous_time
        previous_time = lap
        print(current_time)
    
        
    # Expected Output: 
    # Lap took: 2
    # Lap took: 5
    # Lap took: 3
    # Lap took: 5
print(The_Lap_Timer())