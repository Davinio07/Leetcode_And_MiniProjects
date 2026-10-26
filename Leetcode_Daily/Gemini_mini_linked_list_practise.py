class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Building our mini chain manually: [5] -> [10] -> [3] -> None
box3 = ListNode(3)
box2 = ListNode(10, box3)
head_box = ListNode(5, box2) 
# head_box is the start of the chain (like l1 in LeetCode)

def get_sum(node):
    total_sum = 0
    
    current_box = node
    
    # YOUR TURN: 
    # Write a while loop here to walk down the chain.
    # Add the value of each box to total_sum.
    # Move current_box to the next box.
    while current_box != None:
        total_sum: int = current_box.val + total_sum
        current_box = current_box.next
        

    return total_sum

# Test it!
print("Total Sum: ", get_sum(head_box)) 
# Expected Output: 18