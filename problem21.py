# def sortList():
#     l1 = [1,2,4]
#     l2 = [1,3,4]
#     l3 = []

#     l3.extend(l1)
#     l3.extend(l2)
#     l3.sort()

#     return l3

# print(sortList())

# create a singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # The data the node holds
        self.next = None  # Pointer to the next node in the list

# Function to print all elements of the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data)  # Print the data of the current node
        current = current.next  # Move to the next node

# Example usage
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking the nodes
node1.next = node2
node2.next = node3

# Print all elements of the linked list starting from node1 (head)
print_linked_list(node1)
