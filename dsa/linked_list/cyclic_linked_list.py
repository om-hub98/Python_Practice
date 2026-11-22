from node import Node

class CyclicLinkedList:
    def check_cyclic(self, head)-> bool:
        if head is None:
            return False

        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False

    def optimized_check_cyclic(self, head) -> bool:
        if head is None:
            return False

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class MainClass:
    def main(self):
        # Create a cyclic linked list
        head = Node(1)
        second = Node(2)
        third = Node(3)
        fourth = Node(4)

        head.next = second
        second.next = third
        third.next = fourth
        fourth.next = head  # Creates a cycle

        cyclic_list = CyclicLinkedList()
        if cyclic_list.check_cyclic(head):
        #if cyclic_list.optimized_check_cyclic(head):
            print("The linked list is cyclic.")
        else:
            print("The linked list is not cyclic.")


if __name__ == "__main__":
    main_class = MainClass()
    main_class.main()
