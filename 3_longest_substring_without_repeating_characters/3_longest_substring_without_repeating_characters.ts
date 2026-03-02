function lengthOfLongestSubstring(s: string): number {
    // 引数の文字列の長さが1以下ならその時点で探索終了
    if (s.length <= 1) {
        return s.length
    }

    // 最大部分文字列の長さ
    let maxSubstringLength = 0
    // 現在確認している、重複のない部分文字列
    let currentSubstring = s[0]

    for (let char of s.slice(1)) {
        // 既に同じ文字が含まれている場合、その文字以前の部分を切り捨てて探索を続ける
        const charIndex = currentSubstring.indexOf(char)
        if (charIndex !== -1) {
            // 現時点の最大部分文字列長と比較して、長ければ更新する
            if (currentSubstring.length > maxSubstringLength) {
                maxSubstringLength = currentSubstring.length
            }

            // 重複が見つかった文字まで、currentSubstringから除外する
            currentSubstring = currentSubstring.slice(charIndex + 1)
        }

        // 探索中の部分文字列に加える
        currentSubstring += char
    }

    // 探索中の部分文字列の長さと現在保持している最大部分文字列長のうち、長い方を返す
    return Math.max(maxSubstringLength, currentSubstring.length)

};

if (require.main === module) {
    // テストケース（例1〜例3）
    const testCases: [string, number][] = [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3]
    ];

    testCases.forEach(([s, expected], index) => {
        const i = index + 1;
        console.log(`--- 例 ${i} ---`);
        console.log(`入力: s = "${s}"`);
        try {
            const result = lengthOfLongestSubstring(s);
            console.log(`出力: ${result}`);
        } catch (e) {
            const err = e as Error;
            console.log(`実行エラー: ${err.name} - ${err.message}`);
        }
        console.log(`期待される出力: ${expected}\n`);
    });
}


