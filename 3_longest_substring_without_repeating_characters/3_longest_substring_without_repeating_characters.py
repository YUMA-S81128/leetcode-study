def lengthOfLongestSubstring(s: str) -> int:
    # 文字列長が0あるいは1ならその時点で探索終了
    if len(s) <= 1:
        return len(s)

    # 最大部分文字列の長さ
    max_substring_length = 0
    # 現在確認している、重複のない部分文字列
    current_substring = s[0]

    for i, char in enumerate(s[1:]):
        # 既に同じ文字が含まれている場合、その文字以前の部分を切り捨てて探索を続ける
        if char in current_substring:
            # 現時点の最大部分文字列長と比較して、長ければ更新する
            if len(current_substring) > max_substring_length:
                max_substring_length = len(current_substring)

            # 重複が見つかった文字まで、current_substringから除外する
            repeating_character_index = current_substring.index(char)
            current_substring = current_substring[repeating_character_index + 1 :]

        # 探索中の部分文字列に加える
        current_substring += char

    # 探索中の部分文字列の長さと現在保持している最大部分文字列長のうち、長い方を返す
    return max(max_substring_length, len(current_substring))


if __name__ == "__main__":
    # テストケース（例1〜例3）
    test_cases = [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]

    for i, (s, expected) in enumerate(test_cases, 1):
        print(f"--- 例 {i} ---")
        print(f'入力: s = "{s}"')
        try:
            result = lengthOfLongestSubstring(s)
            print(f"出力: {result}")
        except Exception as e:
            print(f"実行エラー: {type(e).__name__} - {e}")
        print(f"期待される出力: {expected}\n")
