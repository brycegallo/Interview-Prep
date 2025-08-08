# LeetCode 0973 - K Closest Points to Origin
# Medium - Heap / Priority Queue
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Iterative Solution with Min Heap
# Complexities:
# Time : O(k * logn)
# Space: O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for i in range(len(points)):
            points[i].insert(0, points[i][0] ** 2 + points[i][1] ** 2)
        heapq.heapify(points)
        for i in range(k):
            point = heapq.heappop(points)
            result.append(point[1:])
        return result
