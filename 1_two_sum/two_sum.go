package main

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	// numsの要素を降順にソートしたsorted_numsを作成する
	sorted_nums := make([]int, len(nums))
	copy(sorted_nums, nums)
	sort.Slice(sorted_nums, func(i, j int) bool {
		return sorted_nums[i] > sorted_nums[j]
	})

	// large_number_indexを0で初期化する
	large_number_index := 0
	// small_number_indexをsorted_numsの末尾の要素で初期化する
	small_number_index := len(sorted_nums) - 1

	// large_number_indexがsmall_number_indexより小さい間、以下のループを繰り返す
	for large_number_index < small_number_index {
		sum := sorted_nums[large_number_index] + sorted_nums[small_number_index]

		// large_number_indexとsmall_number_indexの和がtargetと等しければループを終了する
		if sum == target {
			break
		}
		// large_number_indexとsmall_number_indexの和がtargetより大きい場合は、large_number_indexを1増やす
		if sum > target {
			large_number_index++
		} else {
			// large_number_indexとsmall_number_indexの和がtarget未満の場合は、small_number_indexを1減らす
			small_number_index--
		}
	}

	// large_number_indexとsmall_number_indexのnumsにおけるインデックスを返す
	// ただし、sorted_nums[large_number_index]とsorted_nums[small_number_index]が同じ値の場合、
	// sorted_nums[large_number_index]のnumsにおけるインデックスを1増やしたところから
	// sorted_nums[small_number_index]のnumsにおけるインデックスを探索する
	val1 := sorted_nums[large_number_index]
	val2 := sorted_nums[small_number_index]

	idx1 := -1
	for i, v := range nums {
		if v == val1 {
			idx1 = i
			break
		}
	}

	idx2 := -1
	start := 0
	if val1 == val2 {
		start = idx1 + 1
	}

	for i := start; i < len(nums); i++ {
		if nums[i] == val2 {
			idx2 = i
			break
		}
	}

	return []int{idx1, idx2}
}

func main() {
	// example1
	nums1 := []int{2, 7, 11, 15}
	target1 := 9
	fmt.Println(twoSum(nums1, target1))

	// example2
	nums2 := []int{3, 2, 4}
	target2 := 6
	fmt.Println(twoSum(nums2, target2))

	// example3
	nums3 := []int{3, 3}
	target3 := 6
	fmt.Println(twoSum(nums3, target3))
}
