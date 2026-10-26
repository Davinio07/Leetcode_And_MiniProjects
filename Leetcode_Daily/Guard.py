def is_cursed(bag):
    # 1. Create your empty dictionary (your notepad)
    inventory = {}
    
    # 2. Loop through every item in the bag
    for item in bag:
        # 3. If the item is ALREADY in your notepad...
        if item in inventory:
            # 4. Sound the alarm! (return True)
            return True
        # 5. Otherwise, write the item into your notepad
        else: 
            inventory[item] = 1
    # 6. If the loop finishes and you never sounded the alarm, return False
    return False

# --- Test Cases ---
bag1 = ["potion", "sword", "shield", "potion"]
print("Bag 1 cursed?", is_cursed(bag1)) 
# Expected Output: True (Because of the second potion)

bag2 = ["sword", "shield", "apple", "gem"]
print("Bag 2 cursed?", is_cursed(bag2)) 
# Expected Output: False (Everything is unique)

bag3 = ["apple", "apple", "apple"]
print("Bag 3 cursed?", is_cursed(bag3)) 
# Expected Output: True