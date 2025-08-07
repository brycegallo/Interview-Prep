# LeetCode 1046 - Last Stone Weight
# Easy - Heap / Priority Queue
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#    If x == y, both stones are destroyed, and
#    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
#At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Iterative Solution with MinHeap
# Complexities:
# Time : O(n * logn)
# Space: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_x, stone_y = heapq.heappop(stones), heapq.heappop(stones)
            if stone_x < stone_y:
                heapq.heappush(stones, stone_x - stone_y)
        return -1 * heapq.heappop(stones) if stones else 0
