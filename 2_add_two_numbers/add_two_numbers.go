package main

import (
	"fmt"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummyHead := &ListNode{Val: 0}

	current := dummyHead
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		val1, val2 := 0, 0
		if l1 != nil {
			val1 = l1.Val
		}
		if l2 != nil {
			val2 = l2.Val
		}

		total := val1 + val2 + carry
		carry = total / 10

		current.Next = &ListNode{Val: total % 10}

		current = current.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}

	return dummyHead.Next
}

// --- ここからテスト用コード ---
func createLinkedList(arr []int) *ListNode {
	if len(arr) == 0 {
		return nil
	}
	head := &ListNode{Val: arr[0]}
	current := head
	for i := 1; i < len(arr); i++ {
		current.Next = &ListNode{Val: arr[i]}
		current = current.Next
	}
	return head
}

func printLinkedList(node *ListNode) {
	var values []string
	current := node
	for current != nil {
		values = append(values, fmt.Sprintf("%d", current.Val))
		current = current.Next
	}
	fmt.Printf("Output: [%s]\n", strings.Join(values, ","))
}

func main() {
	// --- テストケース1 ---
	fmt.Println("Test Case 1:")
	fmt.Println("Input: l1 = [2,4,3], l2 = [5,6,4]")
	l1_head := createLinkedList([]int{2, 4, 3})
	l2_head := createLinkedList([]int{5, 6, 4})
	result1 := addTwoNumbers(l1_head, l2_head)
	printLinkedList(result1)
	fmt.Println()

	// --- テストケース2 ---
	fmt.Println("Test Case 2:")
	fmt.Println("Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
	l3_head := createLinkedList([]int{9, 9, 9, 9, 9, 9, 9})
	l4_head := createLinkedList([]int{9, 9, 9, 9})
	result2 := addTwoNumbers(l3_head, l4_head)
	printLinkedList(result2)
}
