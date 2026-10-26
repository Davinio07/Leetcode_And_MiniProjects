# Standard LeetCode Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        while list1 and list2:
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
        return dummy.next
                


# --- HELPER FUNCTIONS FOR TESTING (Don't change these) ---
def build_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# --- TEST CASES ---
Testing = Solution()

# Example 1
list1_ex1 = build_linked_list([1, 2, 4])
list2_ex1 = build_linked_list([1, 3, 4])
result1 = Testing.mergeTwoLists(list1_ex1, list2_ex1)
print("Test 1:", print_linked_list(result1))  
# Expected: [1, 1, 2, 3, 4, 4]

# Example 2
list1_ex2 = build_linked_list([])
list2_ex2 = build_linked_list([])
result2 = Testing.mergeTwoLists(list1_ex2, list2_ex2)
print("Test 2:", print_linked_list(result2))  
# Expected: []

# Example 3
list1_ex3 = build_linked_list([])
list2_ex3 = build_linked_list([0])
result3 = Testing.mergeTwoLists(list1_ex3, list2_ex3)
print("Test 3:", print_linked_list(result3))  
# Expected: [0]