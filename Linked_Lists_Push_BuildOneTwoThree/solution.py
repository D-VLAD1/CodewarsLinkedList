class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def push(head, data):
    new_head = Node(data)
    new_head.next = head
    return new_head


def build_one_two_three():
    node = push(Node(3), 2)
    node = push(node, 1)
    return node
