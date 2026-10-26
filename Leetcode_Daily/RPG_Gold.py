def calculate_gold(bag):
    # Here is your price book (already written for you)
    price_book = {
        "potion": 10,
        "sword": 50,
        "shield": 25,
        "apple": 2,
        "gem": 100
    }
    
    # 1. Set up your total counter
    TotalGold: int = 0
    
    # 2. Write your for loop to go through the bag
    for item in bag:
        
        # 3. Inside the loop, get the price of the current item from the price_book
        price = price_book[item]
        # 4. Add that price to your total
        TotalGold = price + TotalGold

        
    # 5. Return the total
    return TotalGold

# --- Test Cases ---
loot1 = ["potion", "potion", "apple"]
print("Loot 1 value:", calculate_gold(loot1)) 
# Expected Output: 22

loot2 = ["sword", "shield", "gem", "potion"]
print("Loot 2 value:", calculate_gold(loot2)) 
# Expected Output: 185

loot3 = ["apple", "apple", "apple", "apple", "apple"]
print("Loot 3 value:", calculate_gold(loot3)) 
# Expected Output: 10