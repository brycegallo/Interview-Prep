# LeetCode 2558 - Take Gifts from the Richest Pile
# Easy - Heap / Priority Queue
# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
#    Choose the pile with the maximum number of gifts.
#    If there is more than one pile with the maximum number of gifts, choose any.
#    Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.
# Return the number of gifts remaining after k seconds.

# Min-Heap Solution
# Complexities:
# Time : O(k * log n)
# Space: O(n)
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            gift = -1 * heapq.heappop(gifts)
            heappush(gifts, -1 * floor(sqrt(gift)))
        return -sum(gifts)
