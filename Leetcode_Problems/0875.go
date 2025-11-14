// LeetCode 0875 - Koko Eating Bananas
// Medium - Binary Search
// Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
// Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
// Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
// Return the minimum integer k such that she can eat all the bananas within h hours.

// Solution
// Complexities:
// Time : O(n * log(m)) - n = length of piles array, m = maximum number of bananas in a pile
// Space: O(1)
func minEatingSpeed(piles []int, h int) int {
    left, right := 1, 0
    for _, pile := range piles {
        if pile > right {
            right = pile
        }
    }
    result := right

    for left <= right {
        k := (left + right) / 2
        total_time := 0

        for _, pile := range piles {
            total_time += int(math.Ceil(float64(pile) / float64(k)))
        }

        if total_time <= h {
            result = k
            right = k - 1
        } else {
            left = k + 1
        }
    }
    return result
}
