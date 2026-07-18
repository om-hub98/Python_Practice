class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_linked_list(head: Node):
    if head is None:
        return

    print_linked_list(head.next)
    print(head.data, end=" -> ")


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    print_linked_list(n1)

if __name__ == "__main__":
    main()