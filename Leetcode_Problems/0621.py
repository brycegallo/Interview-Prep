# LeetCode 0621 - Task Scheduler
# Medium - Heap / Priority Queue
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
# Return the minimum number of CPU intervals required to complete all tasks.

# Iterative Solution with Min Heap and Double-Ended Queue
# Complexities:
# Time : O(m * n) - m is the number of tasks, n is the idle time
# Space: O(1) - because we have at most 26 different characters

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  # create hashmap of tasks
        max_heap = [-count for count in count.values()]  # create minHeap of negatives of count values
        heapq.heapify(max_heap)

        time = 0
        queue = deque()  # pairs of [-count, idle time]

        while max_heap or queue:
            time = queue[0][1] if not max_heap else time + 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time
