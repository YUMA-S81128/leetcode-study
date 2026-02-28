from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # 先頭を表すListNode
    head_total = l1.val + l2.val
    head_node: Optional[ListNode] = ListNode(
        head_total % 10, ListNode(head_total // 10, None)
    )

    # 現在走査中のListNodeを表す
    current_node = head_node

    while current_node.next is not None:
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

        if l1 is None and l2 is None:
            if current_node.next.val == 0:
                current_node.next = None
                continue

        if l1 is not None:
            current_node.next.val += l1.val
        if l2 is not None:
            current_node.next.val += l2.val

        current_node.next = ListNode(
            current_node.next.val % 10, ListNode(current_node.next.val // 10, None)
        )

        current_node = current_node.next

    return head_node


# --- ここからテスト用コード ---
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(node):
    print("Output: [", end="")
    current = node
    while current is not None:
        print(current.val, end="")
        current = current.next
        if current is not None:
            print(",", end="")
    print("]")


if __name__ == "__main__":
    # --- テストケース1 ---
    print("Test Case 1:")
    print("Input: l1 = [2,4,3], l2 = [5,6,4]")
    l1_head = create_linked_list([2, 4, 3])
    l2_head = create_linked_list([5, 6, 4])
    result1 = addTwoNumbers(l1_head, l2_head)
    print_linked_list(result1)
    print()

    # --- テストケース2 ---
    print("Test Case 2:")
    print("Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
    l3_head = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l4_head = create_linked_list([9, 9, 9, 9])
    result2 = addTwoNumbers(l3_head, l4_head)
    print_linked_list(result2)
