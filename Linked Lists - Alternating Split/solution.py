class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise Exception

    first, second = head, head.next
    curr_first, curr_second = first, second
    curr = head.next.next

    i = 0
    while curr is not None:
        if i % 2 == 0:
            curr_first.next = curr
            curr_first = curr_first.next

        elif i % 2 == 1:
            curr_second.next = curr
            curr_second = curr_second.next

        curr = curr.next
        i += 1

    curr_first.next, curr_second.next = None, None
    return Context(first, second)
