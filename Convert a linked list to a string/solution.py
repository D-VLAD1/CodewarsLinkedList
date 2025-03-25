class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def stringify(node):
    if node is None:
        return 'None'

    current_node = node
    output = []
    while current_node is not None:
        output.append(current_node.data)
        current_node = current_node.next

    return ' -> '.join(map(str, output)) + ' -> None'
