class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        



# Test Case
Testing = Solution()

print("Test 1: ", Testing.addTwoNumbers([2,4,3], [5,6,4]))
# Expected Output: ... 

print("Test 2: ", Testing.addTwoNumbers([0], [0]))
# Expected Output: ...

print("Test 3: ", Testing.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))
# Expected Output: ...