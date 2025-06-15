# LeetCode 0875 - Koko Eating Bananas
# Medium - Binary Search
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Binary Search Solution
# Complexities:
# Time : O(m * logn)
# Space: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        result = right = max(piles)

        while left <= right:
            rate = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            result = min(result, rate) if hours <= h else result
            right = rate - 1 if hours <= h else right
            left = rate + 1 if hours > h else left
        return result
