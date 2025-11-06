# LeetCode 0983 - Minimum Cost For Tickets
# Medium - 1-D Dynamic Programming
# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
#     a 1-day pass is sold for costs[0] dollars,
#     a 7-day pass is sold for costs[1] dollars, and
#     a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
#     For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
# Return the minimum number of dollars you need to travel every day in the given list of days.

# Top-Down Dynamic Programming Solution
# Complexities:
# Time : O(n) - O(1 + 7 + 30), so constant really
# Space: O(365) - maximum number of days in most years, so constant
class TopDownSolution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = { len(days): 0 }

        def dfs(i):
            if i not in cache:
                cache[i] = float("inf")
                j = i
                for cost, duration in zip(costs, [1, 7, 30]):
                    while j < len(days) and days[j] < days[i] + duration:
                        j += 1
                    cache[i] = min(cache[i], cost + dfs(j))
            return cache[i]
        return dfs(0)
