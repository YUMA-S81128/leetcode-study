def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    m = len(nums1)
    n = len(nums2)

    if m >= n:
        long_list = nums1
        short_list = nums2
    else:
        long_list = nums2
        short_list = nums1

    # 全体の左半分の要素数kを計算する
    k = (m + n + 1) // 2

    # short_listに対する探索範囲を定義する
    left = 0
    right = min(m, n)

    while left <= right:
        # 中間点を計算する
        i = (left + right) // 2

        # short_listの左半分の最大要素と右半分の最小要素
        ls = short_list[i - 1] if i != 0 else float("-inf")
        rs = short_list[i] if i != min(m, n) else float("inf")
        # long_listの左半分の最小要素と右半分の最大要素
        ll = long_list[k - i - 1] if k - i != 0 else float("-inf")
        rl = long_list[k - i] if k - i != max(m, n) else float("inf")

        if ls <= rl and ll <= rs:
            # 正しい分割位置になったのでループを抜ける
            break
        elif ls > rl:
            # iが大きすぎるので、rightを減らす
            right = i - 1
        elif ll > rs:
            # iが小さすぎるので、leftを増やす
            left = i + 1

    if (m + n) % 2 == 1:
        return max(ls, ll)
    else:
        return (max(ls, ll) + min(rs, rl)) / 2
