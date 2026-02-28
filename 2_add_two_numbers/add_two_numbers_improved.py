from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # ダミーの先頭ノード（番兵ノード）を用意する。これにより最初のノード生成の条件分岐をなくせる
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0  # 繰り上がりを保持する変数

    # l1 または l2 がまだノードを持っているか、もしくは最終の繰り上がりが残っていればループを続ける
    while l1 is not None or l2 is not None or carry > 0:
        # 現在のノードが存在すればその値を、存在しなければ 0 とする
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        # 足し算と繰り上がりの計算
        total = val1 + val2 + carry
        carry = total // 10

        # 新しいノードを作成して次に繋げる
        current.next = ListNode(total % 10)

        # currentを新しいノードへ移動、l1とl2も次に進める（Noneでなければ）
        current = current.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    # ダミーノードの「次」からが実際の答えのリスト
    return dummy_head.next


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
