"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if there is no root
        # we can check this by checking if self is None
        if self is None:
            # if not insert here
            self = BSTNode(value)
        # else there is a root check
        # THE ABOVE CODE IS NOT NECESSARY
        else:
            # if the value < root's value, go left
            if value < self.value:
                # if true, go left
                if self.left:
                    self.left.insert(value)
                else:
                    # if no self.left put value here
                    self.left = BSTNode(value)
            # if value >= root's value, go right
            else:
                # if true, go right
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target is less than the current value, go left
        if target < self.value:
            # if target equals self.left
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True

    # Return the maximum value found in the tree

    def get_max(self):
        # if self.right:
        #     return self.right.get_max()
        # else:
        #     return self.value
        return self.right and self.right.get_max() or self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call the function
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iter_depth_first_for_each(self, fn):
        # with depth first traversal, there is acertain order to when we visit nodes: LIFO
        # initialize a stack, to keep track of nodes visited
        stack = []
        # add the first node to our stack
        stack.append(self)
        # continue traversing until our stack is empty
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            # add its children to the stack
            # add the right child first and left child second (to ensure the left is popped off the stack first)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            # call the fn function on self.value
            fn(self.value)

    def iter_breadth_first_search(self, fn):
        # breadth first traversal follows FIFO ordering of its nodes
        # init a deque
        q = deque()
        # add first node to q
        q.append(self)
        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            # how am I goig to get all the way left
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        q = []
        q.append(node)
        while len(q) > 0:
            current_node = q.pop(0)
            print(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
