class Node:
    def __init__(self,cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def print_backwards(self):
        if self.next is not None:
            tail = self.next
            tail.print_backwards()
        print(self.cargo, end=" ")

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def print_backwards(self):
        """This is a wrapper for the helper in Node class.
        Node's print_backwards will be invoked when this func is called"""
        print("[", end=" ")
        if self.head is not None: ##because self.head is a Node object.
            self.head.print_backwards()

    def add_first(self,cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1




def print_list(node):
    while node is not None:
        print(node, end =" ")
        node = node.next
    print()

def print_backwards(list):
    if list is None: return ##base case. end the function if
    head = list
    tail = list.next
    print_backwards(tail)
    print(head, end=" ")

def add_brackets(list):
    print("[", end=" ")
    print_backwards(list)
    print("]")

def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    if second == None:
        return
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

node = Node("test")
node3 = Node()
node2 = Node(2, node3)
node1 = Node(1, node2)

remove_second(node3)
