# LeetCode 0895 - Maximum Frequency Stack
# Hard - Stack
# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# Implement the FreqStack class:
#    FreqStack() constructs an empty frequency stack.
#    void push(int val) pushes an integer val onto the top of the stack.
#    int pop() removes and returns the most frequent element in the stack.
#        If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Stack Solution
# Complexities:
# Time : O(1) - for each push() and pop() function call
# Space: O(n) - n is the number of elements on the stack at any given time
class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.count[val] = 1 + self.count.get(val, 0)
        if self.count[val] > self.max_count:
            self.max_count = self.count[val]
            self.stacks[self.count[val]] = []
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        result = self.stacks[self.max_count].pop()
        self.count[result] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return result
