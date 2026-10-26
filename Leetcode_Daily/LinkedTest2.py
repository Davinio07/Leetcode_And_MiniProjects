# 1. Define the LeetCode ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Helper to build a linked list from a standard Python array
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# --- YOUR TURN ---
def print_smallest(list1, list2):
    # Your goal: Keep looping as long as BOTH list1 and list2 have nodes.
    # Compare their values, print the smaller one, and step forward on the winner.
    
    # Write your logic here!
    dummy = ListNode()
    current = dummy
    while list1 and list2:

            # Check which number is smaller
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
            if list1:
                current.next = list1
            else:
                current.next = list2
            
        


# --- Run the Test ---
# Belt 1: 1 -> 4 -> 8
l1 = build_list([1, 4, 8])

# Belt 2: 2 -> 3 -> 9
l2 = build_list([2, 3, 9])

print("Expected output: 1, 2, 3, 4 (and then it stops because we hit the end of the belts)")
print("--- Your output below ---")
print_smallest(l1, l2)