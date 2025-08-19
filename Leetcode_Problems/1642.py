# LeetCode 1642 - Furthest Building You Can Reach
# Medium - Heap / Priority Queue
# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
# While moving from building i to building i+1 (0-indexed),
#    If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#    If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# Max-Heap Solution:
# Complexities:
# Time : O(n * log n)
# Space: O(n)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # Max heap of bricks used

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                bricks -= diff
                heapq.heappush(heap, -diff)

                if bricks < 0:
                    if ladders != 0:
                        ladders -= 1
                        bricks += -heapq.heappop(heap)
                    else:
                        return i

        return len(heights) - 1

