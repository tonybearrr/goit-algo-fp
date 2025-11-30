"""Singly linked list: reverse, sort, merge"""


class Node:
    """Node in singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add node to the end"""
        node_data = Node(data)
        if not self.head:
            self.head = node_data
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node_data

    def to_list(self):
        """Convert to Python list"""
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    @staticmethod
    def from_list(data_list):
        """Create list from Python list"""
        linked_list = LinkedList()
        for item in data_list:
            linked_list.append(item)
        return linked_list


def reverse_list(head):
    """Reverse singly linked list by changing links"""
    prev = None
    cur = head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


def insertion_sort_list(head):
    """Sort linked list using insertion sort"""
    if not head or not head.next:
        return head

    dummy = Node(0)
    dummy.next = head
    cur = head

    while cur and cur.next:
        if cur.data <= cur.next.data:
            cur = cur.next
        else:
            to_insert = cur.next
            cur.next, prev = to_insert.next, dummy
            while prev.next.data < to_insert.data:
                prev = prev.next
            to_insert.next, prev.next = prev.next, to_insert
    return dummy.next


def merge_sorted_lists(list1, list2):
    """Merge two sorted linked lists into one sorted list"""
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


if __name__ == "__main__":
    print("1. Реверсія:")
    linked_list1 = LinkedList.from_list([1, 2, 3, 4, 5])
    print(f"До: {linked_list1.to_list()}")
    linked_list1.head = reverse_list(linked_list1.head)
    print(f"Після: {linked_list1.to_list()}")

    print("\n2. Сортування:")
    linked_list2 = LinkedList.from_list([4, 2, 1, 3, 5])
    print(f"До: {linked_list2.to_list()}")
    linked_list2.head = insertion_sort_list(linked_list2.head)
    print(f"Після: {linked_list2.to_list()}")

    print("\n3. Об'єднання відсортованих списків:")
    linked_list3 = LinkedList.from_list([1, 3, 5])
    linked_list4 = LinkedList.from_list([2, 4, 6])
    print(f"Список 1: {linked_list3.to_list()}")
    print(f"Список 2: {linked_list4.to_list()}")
    merged = LinkedList()
    merged.head = merge_sorted_lists(linked_list3.head, linked_list4.head)
    print(f"Об'єднаний: {merged.to_list()}")
