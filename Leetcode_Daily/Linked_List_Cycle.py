class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        breadCrumb: set = set()
        while node != None:
            if node not in breadCrumb:
                breadCrumb.add(node)
                node = node.next
            else:
                return True
        return False
                
        



# Test Case
Testing = Solution()
print("Test 1: ", Testing.hasCycle([3,2,0,-4]))
# Expected Output: true 

print("Test 2: ", Testing.hasCycle([1,2]))
# Expected Output: true

print("Test 3: ", Testing.hasCycle([1]))
# Expected Output: false