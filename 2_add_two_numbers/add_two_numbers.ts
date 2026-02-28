class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}


function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummyHead = new ListNode(0)
    // 現在走査中のノードを表す変数
    let current = dummyHead
    // 繰り上がりを保持する変数
    let carry: number = 0

    while (l1 !== null || l2 !== null || carry > 0) {
        const val1 = l1 !== null ? l1.val : 0
        const val2 = l2 !== null ? l2.val : 0

        // 足し算と繰り上がりの計算
        const total = val1 + val2 + carry
        carry = Math.floor(total / 10)

        // 新しいノードを作成して次に繋げる
        current.next = new ListNode(total % 10)

        // currentを新しいノードへ移動、l1とl2も次に進める（Noneでなければ）
        current = current.next
        if (l1 !== null) {
            l1 = l1.next
        }
        if (l2 !== null) {
            l2 = l2.next
        }
    }

    return dummyHead.next

};

// --- ここからテスト用コード ---
function createLinkedList(arr: number[]): ListNode | null {
    if (arr.length === 0) return null;
    const head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

function printLinkedList(node: ListNode | null): void {
    const values: number[] = [];
    let current = node;
    while (current !== null) {
        values.push(current.val);
        current = current.next;
    }
    console.log(`Output: [${values.join(",")}]`);
}

// --- テストケース1 ---
console.log("Test Case 1:");
console.log("Input: l1 = [2,4,3], l2 = [5,6,4]");
const l1_head = createLinkedList([2, 4, 3]);
const l2_head = createLinkedList([5, 6, 4]);
const result1 = addTwoNumbers(l1_head, l2_head);
printLinkedList(result1);
console.log();

// --- テストケース2 ---
console.log("Test Case 2:");
console.log("Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]");
const l3_head = createLinkedList([9, 9, 9, 9, 9, 9, 9]);
const l4_head = createLinkedList([9, 9, 9, 9]);
const result2 = addTwoNumbers(l3_head, l4_head);
printLinkedList(result2);