class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return self.data


def push(head, data):
    new_head = Node(data)
    new_head.next = head
    return new_head


def build_one_two_three():
    node = push(Node(3), 2)
    node = push(node, 1)
    return node


def reverse(head):
    curr = head
    previous = None

    while curr is not None:
        next_el = curr.next

        curr.next = previous

        previous = curr
        curr = next_el

reverse(build_one_two_three())
