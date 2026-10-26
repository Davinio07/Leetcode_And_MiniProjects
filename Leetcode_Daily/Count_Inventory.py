def count_inventory(bag):
    # 1. Create an empty dictionary
    inventory = {}
    
    # 2. Loop through the bag
    for item in bag:
    
        # 3. If the item is already in the dictionary...
        if item in inventory:
            
            # 4. Add 1 to its count
            inventory[item] += +1
            
        # 5. Else (it is not in the dictionary yet)...
        else: 
            # 6. Add it and set the count to 1
            inventory[item] = 1 

    # 7. Return the final dictionary
    return inventory

# --- Test Cases ---
bag1 = ["potion", "potion", "apple"]
print("Bag 1:", count_inventory(bag1)) 
# Expected Output: {'potion': 2, 'apple': 1}

bag2 = ["sword", "sword", "sword"]
print("Bag 2:", count_inventory(bag2)) 
# Expected Output: {'sword': 3}

bag3 = ["shield", "gem", "apple"]
print("Bag 3:", count_inventory(bag3)) 
# Expected Output: {'shield': 1, 'gem': 1, 'apple': 1}