// LeetCode 0074 - Search a 2D Matrix
// Medium - Binary Search
// You are given an m x n integer matrix matrix with the following two properties:
//     Each row is sorted in non-decreasing order.
//     The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.
// You must write a solution in O(log(m * n)) time complexity.

// Solution
// Complexities:
// Time : O(log(m * n))
// Space: O(1)
func searchMatrix(matrix [][]int, target int) bool {
    rows, cols := len(matrix), len(matrix[0])
    left, right := 0, rows*cols-1

    for left <= right {
        middle := left + (right-left)/2
        row, col := middle / cols, middle % cols
        if matrix[row][col] == target {
            return true
        } else if matrix[row][col] < target {
            left = middle + 1
        } else {
            right = middle - 1
        }
    }
    return false
}
