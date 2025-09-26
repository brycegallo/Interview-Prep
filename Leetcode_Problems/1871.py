# LeetCode 1871 - Jump Game VII
# Medium - Greedy
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
#     i + minJump <= j <= min(i + maxJump, s.length - 1), and
#     s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        furthest = 0

        while queue:
            i = queue.popleft()
            start = max(i + minJump, furthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    if j == len(s) - 1:
                        return True
                    queue.append(j)
            furthest = i + maxJump
        return False
