# LeetCode 0232 - Implement Queue using Stacks
# Easy - Stack
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
#    void push(int x) Pushes element x to the back of the queue.
#    int pop() Removes the element from the front of the queue and returns it.
#    int peek() Returns the element at the front of the queue.
#    boolean empty() Returns true if the queue is empty, false otherwise.
#Notes:
#    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
#
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Two Stack Solution with Amortized Complexity
# Complexities:
# Time: O(1) amortized for pop() and peek() calls, O(1) for initialization and other function calls
# Space: O(n)
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)
