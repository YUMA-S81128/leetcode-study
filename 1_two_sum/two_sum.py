# プログラミングや数学の文脈において「add up to [target]」という表現は、
# 合計が「正確にtargetと一致する」ことを指す。「target以下」という意味は含まれない。


def twoSum(nums: list[int], target: int) -> list[int]:
    # numsの要素を降順にソートしたsorted_numsを作成する
    sorted_nums = sorted(nums, reverse=True)

    # large_number_indexを0で初期化する
    # small_number_indexをsorted_numsの末尾の要素のインデックスで初期化する
    large_number_index = 0
    small_number_index = len(sorted_nums) - 1

    # large_number_indexがsmall_number_indexより小さい間、以下のループを繰り返す
    while large_number_index < small_number_index:
        current_sum = sorted_nums[large_number_index] + sorted_nums[small_number_index]

        # current_sumがtargetと等しければ、ループを終了する
        if current_sum == target:
            break
        # current_sumがtargetより大きければ、large_number_indexを1増やす
        elif current_sum > target:
            large_number_index += 1
        # current_sumがtarget未満であれば、small_number_indexを1減らす
        else:
            small_number_index -= 1

    large_number = sorted_nums[large_number_index]
    small_number = sorted_nums[small_number_index]

    nums_idx1 = nums.index(large_number)
    # large_numberとsmall_numberが同じ値の場合、nums.index()は常に最初の出現位置を返すため、
    # nums_idx1と同じインデックスが返されてしまう。これを避けるため、検索開始位置をnums_idx1 + 1にずらす。
    nums_idx2 = (
        nums.index(small_number, nums_idx1 + 1)
        if large_number == small_number
        else nums.index(small_number)
    )

    return [nums_idx1, nums_idx2]


# example1
nums1 = [2, 7, 11, 15]
target1 = 9

print(twoSum(nums1, target1))

# example2
nums2 = [3, 2, 4]
target2 = 6

print(twoSum(nums2, target2))

# example3
nums3 = [3, 3]
target3 = 6

print(twoSum(nums3, target3))
