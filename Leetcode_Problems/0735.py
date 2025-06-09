# LeetCode 0735 - Asteroid Collision
# Medium - Stack
# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Stack Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                outcome = stack[-1] + asteroid
                asteroid = asteroid if outcome < 0 else 0
                if outcome <= 0:
                    stack.pop()
            if asteroid:
                stack.append(asteroid)
        return stack

