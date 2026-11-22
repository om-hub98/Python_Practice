from node import Node


class AddTwoNumbers:
    def add_two_numbers(self, l1: Node, l2: Node) -> Node:
        dummy = Node(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = Node(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


class MainClass:
    def main(self):
        head1 = Node(2, Node(4, Node(3)))
        head2 = Node(5, Node(6, Node(4)))

        add_two_numbers = AddTwoNumbers()

        result = add_two_numbers.add_two_numbers(head1, head2)

        # Print the complete linked list
        current = result

        while current:
            print(current.data, end=" ")
            current = current.next


if __name__ == "__main__":
    MainClass().main()