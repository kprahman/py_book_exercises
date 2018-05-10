from node_class import Node

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

class ImprovedQ:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None ## this will be used in insert/remove methods

    def is_empty(self):
        return self.length == 0

    def insert(self,cargo):
        node = Node(cargo) ## creates a Node with cargo, no .next
        if self.length == 0: ## if this is the first item
            self.head = self.last = node ## the node is the first AND last item
        else:
            last = self.last ## find the last node
            last.next = node ## append the new node
            self.last = node ## the node is now the last in the Q
        self.length += 1

class PriorityQ:
    def __init__(self):
        """list veneer"""
        self.items = []

    def is_empty(self):
        """list veneer"""
        return not self.items ## self.items still exists, but is empty works as a boolean??

    def insert(self,item):
        """list veneer"""
        self.items.append(item)

    def remove(self):
        priority_index = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[priority_index]: ##if type is not primitive, define __gt__
                priority_index = i
        priority_value = self.items[priority_index]
        del self.items[priority_index] ## same as pri_value
        return priority_value

class Golfer:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score #lower score is better!






