class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
            return
        elif index <= 0:
            self.prepend(value)
            return

        new_node = Node(value)
        leader = self._traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length += 1

    def remove(self, index):
        if index >= self.length or index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        leader = self._traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1

    def _traverse_to_index(self, index):
        current_node = self.head
        count = 0
        while count != index:
            current_node = current_node.next
            count += 1
        return current_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")
# Create a singly linked list with initial value 5
linked_list = LinkedList(5)

# Append some values to the list
linked_list.append(10)
linked_list.append(2003)

# Prepend a value to the list
linked_list.prepend(25)

# Insert a value at index 2
linked_list.insert(25, 7)

# Remove a value at index 1
linked_list.remove(1)

# Display the linked list
linked_list.display()


