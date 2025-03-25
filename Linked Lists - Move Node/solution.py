class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if source is None and dest is None:
        raise Exception

    head = source.data
    new_dest = Node(head)
    new_dest.next = dest

    output = Context(source.next, new_dest)
    return output