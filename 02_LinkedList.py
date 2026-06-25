class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None          # entry point to the chain

    def prepend(self, value):     # add at FRONT — O(1), just rewire head
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):      # add at END — O(n), must walk to the tail
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def display(self):            # walk the chain, collect values
        out, cur = [], self.head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out
    
#-----------------------------------------------------------------

chain = LinkedList()
for amount in [1500, 320, 9800]:
    chain.append(amount)
chain.prepend(75)                 # newest-first arrival at the front

print("chain:", chain.display())  # [75, 1500, 320, 9800]