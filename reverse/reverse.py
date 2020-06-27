'''
#### Task 3. Reverse a Linked List
Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list using recursion, _not a loop._
For example,
```
1->2->3->None
```
would become...
```
3->2->1->None
```
While credit will be given for a functional solution, only optimal solutions will earn a **_3_** on this task.
UPER NOTES
Reverse the output of this singly-linked-list. 
if you can use recursion then awesome if not then just iterate muchacho.
'''

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #while loop through and point the pointer to the prev, declare it the next_node and set it to the head.
        while node:
            next_node = node.get_next()
            node.next_node = prev
            prev = node
            node = next_node
        self.head = prev

# sprint_list = LinkedList()
# sprint_list.add_to_head(0)
# sprint_list.add_to_head(1)
# sprint_list.add_to_head(2)
# sprint_list.add_to_head(3)
# print(sprint_list)