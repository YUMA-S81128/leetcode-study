package main

import "strings"

func lengthOfLongestSubstring(s string) int {
	// 引数の文字列の長さが1以下ならその時点で探索終了
	if len(s) <= 1 {
		return len(s)
	}

	// 最大部分文字列の長さ
	maxSubstringLength := 0
	// 現在確認している、重複のない部分文字列
	// string型として取得したいため、スライスを利用する
	currentSubstring := s[:1]

	for _, charRune := range s[1:] {
		char := string(charRune)
		// すでに同じ文字列が含まれている場合、その文字以前の部分を切り捨てて探索を続ける
		if strings.Contains(currentSubstring, char) {
			if len(currentSubstring) > maxSubstringLength {
				maxSubstringLength = len(currentSubstring)
			}

			// 重複が見つかった文字まで、currentSubstringから除外する
			currentSubstring = currentSubstring[strings.Index(currentSubstring, char)+1:]
		}

		// 探索中の部分文字列に加える
		currentSubstring += char
	}

	// 探索中の部分文字列の長さと現在保持している最大部分文字列長のうち、長い方を返す
	return max(maxSubstringLength, len(currentSubstring))

}

func main() {
	// テストケース（例1〜例3）
	testCases := []struct {
		s        string
		expected int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
	}

	for i, tc := range testCases {
		println("--- 例", i+1, "---")
		println("入力: s =", "\""+tc.s+"\"")
		result := lengthOfLongestSubstring(tc.s)
		println("出力:", result)
		println("期待される出力:", tc.expected)
		println()
	}
}
