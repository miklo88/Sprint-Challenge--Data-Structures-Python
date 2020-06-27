#straight from the binary_search_tree.py file in my data structures

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    # another base case
    def insert(self, value):
#         # new_node = BSTNode(value)
# #if empty
#         if self.value is None:
#             self.value = value
        # take the current value of our node (self.value)
        #compare to the new value we want to insert
        if value < self.value:
            #set the left to the new node with the new value if left is empty
            if self.left is None:
                self.left = new_node
            else:
                # self.left.insert(value)
                self.left.BSTNode(value)
#set the right child to the new node with the new value
        # if value >= self.value:
        else:  
            if self.right is None:
                self.right = new_node
            else:
                # self.right.insert(value)
                self.right.BSTNode(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if the target is equal to the base node or root node
        if self.value == target:
            return True
        #compar the target to the current value
        # if current value < target
        found = False
        if self.value > target:
            #check the left subtree self.left.contains(target)
            if self.left is None:
                return False
            found = self.left.contains(target)
#if current value >= target
        if self.value < target:
        #check if right subtree contains target
        #if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found