# LeetCode 1011 - Capacity to Ship Packages within D Days
# Medium - Binary Search
# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# Binary Search Solution
# Complexities:
# Time : O(n * logn)
# Space: O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = result = sum(weights)

        def canShip(capacity):
            ships, current_capacity = 1, capacity
            for weight in weights:
                ships = ships + 1           if current_capacity < weight else ships
                current_capacity = capacity if current_capacity < weight else current_capacity
                current_capacity -= weight
            return ships <= days

        while left <= right:
            capacity = left + (right - left) // 2
            if canShip(capacity):
                result = min(result, capacity)
                right = capacity - 1
            else:
                left = capacity + 1

        return result

