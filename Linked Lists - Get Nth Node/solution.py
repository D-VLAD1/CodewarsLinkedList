class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if node is None or index < 0:
        raise Exception

    curr_node, i = node, 0
    while i < index:
        curr_node = curr_node.next
        i += 1

    if i != index or curr_node is None:
        raise Exception

    return curr_node


