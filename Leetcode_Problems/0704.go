// LeetCode 0704 - Binary Search
// Easy - Binary Search
// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
// You must write an algorithm with O(log n) runtime complexity. 

// Solution
// Complexities:
// Time : O(log n)
// Space: O(1)
func search(nums []int, target int) int {
    left, right := 0, len(nums)-1
    for left <= right {
        middle := left + (right-left)/2

        if nums[middle] > target {
            right = middle - 1
        } else if nums[middle] < target {
            left = middle + 1
        } else {
            return middle
        }
    }
    return -1
}
