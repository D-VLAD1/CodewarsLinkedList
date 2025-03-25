class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    data = s.split(' -> ')[:-1]
    if not data:
        return None

    first = Node(data[0])
    curr = first

    for data_point in data[1:]:
        curr.next = Node(data_point)
        curr = curr.next

    return first

