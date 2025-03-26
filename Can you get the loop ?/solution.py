class Node:
    def __init__(self, next=None):
        self.next = next


def loop_size(node):
    slow, fast = node.next, node.next.next
    encounter = None

    while True:
        if slow == fast:
            slow = node
            while slow != fast:
                slow = slow.next
                fast = fast.next

            encounter = slow
            break

        slow = slow.next
        fast = fast.next.next


    slow = slow.next
    i = 1
    while encounter != slow:
        i += 1
        slow = slow.next

    return i

