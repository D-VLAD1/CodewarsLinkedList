class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if head is None:
        return Node(data)

    if head.data > data:
        new_node = Node(data)
        new_node.next = head
        return new_node

    curr = head
    while True:
        if curr.next is None or curr.next.data > data:
            next_node = curr.next
            node = Node(data)
            node.next = next_node
            curr.next = node
            break

        curr = curr.next

    return head
