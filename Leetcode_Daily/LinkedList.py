class Node:
    def __init__(self, value ):
        self.val = value 
        self.next = None
        
    def LinkedListLoop():
        node1 = Node("Cloud")
        node2 = Node("Computing")
        node3 = Node("Rocks")

        # Now we link the chain together!
        node1.next = node2
        node2.next = node3
        # node3.next is empty (None), which means it is the end of the line.
        
        current_node = node1
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next
    print(LinkedListLoop())
            