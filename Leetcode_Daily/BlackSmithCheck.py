def can_craft(inventory):
    bag = {}
    # 1. Safely fetch the amount of iron you have
    for item in inventory:
        amountOfIron = inventory.get("iron", 0)
    # 2. Safely fetch the amount of leather you have
        amountOfLeather = inventory.get("leather", 0)

    # 3. Check if iron is >= 3 AND leather is >= 1
    if amountOfIron >= 3 and amountOfLeather >= 1:
        # 4. If yes, return True
        return True
    # 5. Otherwise, return False
    else: return False

# --- Test Cases ---
player1_inv = {"iron": 5, "leather": 2, "potion": 1}
print("Player 1 can craft:", can_craft(player1_inv)) 
# Expected Output: True

player2_inv = {"iron": 2, "leather": 5}
print("Player 2 can craft:", can_craft(player2_inv)) 
# Expected Output: False (Not enough iron!)

player3_inv = {"sword": 1, "potion": 3}
print("Player 3 can craft:", can_craft(player3_inv)) 
# Expected Output: False (No iron or leather at all!)