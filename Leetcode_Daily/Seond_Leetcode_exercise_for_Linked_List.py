class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Challenge 1: Traverse and Print
def print_list(head: ListNode):
    # TODO: Start at the 'head' node.
    # While your current node is not None:
    #   1. Print its value
    #   2. Move to the next node (current = current.next)
    current = head
    while head != None:
        print(current.val)
        current.next

# Challenge 2: Append a New Node
def append_node(head: ListNode, val: int) -> ListNode:
    # TODO: Create a new ListNode with the given 'val'.
    # If the list is entirely empty (head is None), just return the new node.
    # Otherwise, traverse to the very last node (where next is None),
    # and set its 'next' pointer to your new node. Return the head.
    pass

# --- Testing your code ---
# Create the first node
my_list = ListNode(10)

# Add more values
my_list = append_node(my_list, 20)
my_list = append_node(my_list, 30)

# Print the list: This should output 10, then 20, then 30
print_list(my_list)