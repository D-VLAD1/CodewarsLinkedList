class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return None

    curr = head

    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next

        curr = curr.next

    return head
