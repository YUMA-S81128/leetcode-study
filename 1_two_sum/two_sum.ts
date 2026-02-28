function twoSum(nums: number[], target: number): number[] {
    const sortedNums: number[] = nums.toSorted((a, b) => b - a)

    let largeNumberIndex: number = 0
    let smallNumberIndex: number = sortedNums.length - 1

    while (largeNumberIndex < smallNumberIndex) {
        const currentSum: number = sortedNums[largeNumberIndex] + sortedNums[smallNumberIndex]

        if (currentSum === target) {
            break
        } else if (currentSum > target) {
            largeNumberIndex++
        } else {
            smallNumberIndex--
        }
    }

    const largeNumber: number = sortedNums[largeNumberIndex]
    const smallNumber: number = sortedNums[smallNumberIndex]

    const index1: number = nums.indexOf(largeNumber)
    const index2: number = largeNumber === smallNumber ? nums.indexOf(smallNumber, index1 + 1) : nums.indexOf(smallNumber)

    return [index1, index2]
}

console.log(twoSum([2, 7, 11, 15], 9))
console.log(twoSum([3, 2, 4], 6))
console.log(twoSum([3, 3], 6))