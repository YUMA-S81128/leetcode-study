def longestPalindrome(self, s: str) -> str:
    # 結果格納用の文字列
    result: str = ""

    for i in range(len(s)):
        # 奇数長の回文
        left: int = i
        right: int = i

        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1
            else:
                break

        # 偶数長の回文
        left: int = i
        right: int = i + 1

        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1
            else:
                break

    return result


if __name__ == "__main__":
    # selfの代わりにNoneを渡して呼び出します
    test_cases = [
        ("babad", ["bab", "aba"]),  # "bab" または "aba" のいずれかが正解
        ("cbbd", ["bb"]),  # "bb" が正解
        ("a", ["a"]),  # 1文字の場合、その文字自体が正解
        ("bb", ["bb"]),  # 2文字の回文
        ("ab", ["a", "b"]),  # 2文字の非回文（1文字のいずれかが正解）
    ]

    for s, expected in test_cases:
        actual = longestPalindrome(None, s)
        print(f"Input: {s}")
        print(f"Expected: one of {expected}")
        print(f"Actual: '{actual}'")
        print(f"Result: {'PASS' if actual in expected else 'FAIL'}")
        print("-" * 20)
