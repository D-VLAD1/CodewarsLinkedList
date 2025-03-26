class Node:
    def __init__(self, name, next=None):
        self.next = next
        self.name = name


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    prev, curr = head, head.next
    head = curr

    while True:
        next = curr.next
        curr.next = prev

        if next is None or next.next is None:
            prev.next = next
            break

        prev.next = next.next
        prev = next
        curr = prev.next

    return head
