from dll_stack import Stack
from dll_queue import Queue
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # go left
            # is value always the root?
            if not self.left:
                # it's not here
                return False
            else:
                return self.left.contains(target)

        else:  # target is >= self.value
            # go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

        # max_value = self.value
        # current = self

        # while current:
        #     # if current is greater than max, update
        #     if current.value > max_value:
        #         max_value = current.value

        #     current = current.right

        # return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # cb(self.value)

        # if self.left:
        #     self.left.for_each(cb)

        # if self.right:
        #     self.right.for_each(cb)

        stack = []
        stack.append(self)

        while len(stack):
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node == None:
            return
        # if self.left:
        self.in_order_print(node.left)
        # else:
        print(node.value)
        # if self.right:
        self.in_order_print(node.right)
        # pass

        # while self.stack.len > 0:
        #     self.stack.value[0].pop

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    # create stack - use dll_stack
    # push start node to stack
    # while stack > 0:
    #     pop top item in stack
    #     do the thing!
    #     if left
    #         add left
    #     if right
    #          add right

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
