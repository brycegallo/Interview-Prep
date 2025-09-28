# LeetCode 0134 - Gas Station
# Medium - Greedy
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# Greedy Solution
# Complexities:
# Time : O(n)
# Speedy : O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) >= sum(cost):
            total, start_position = 0, 0
            for i in range(len(gas)):
                total += (gas[i] - cost[i])
                start_position = i + 1 if total < 0 else start_position
                total = 0 if total < 0 else total
        return start_position if sum(gas) >= sum(cost) else -1
