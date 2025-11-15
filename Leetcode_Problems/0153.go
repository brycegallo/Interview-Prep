// LeetCode 0153 - Find Minimum in Rotated Sorted Array
// Medium - Binary Search
// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
//     [4,5,6,7,0,1,2] if it was rotated 4 times.
//     [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
// Given the sorted rotated array nums of unique elements, return the minimum element of this array.
// You must write an algorithm that runs in O(log n) time.

// Solution
// Complexities:
// Time : O(log(n))
// Space: O(1)
func findMin(nums []int) int {
    left, right := 0, len(nums)-1
    for left < right {
        middle := left + (right-left)/2
        if nums[middle] < nums[right] {
            right = middle
        } else {
            left = middle + 1
        }
    }
    return nums[left]
}
