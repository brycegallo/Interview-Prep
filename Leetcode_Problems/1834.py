# LeetCode 1834 - Single-Threaded CPU
# Medium - Heap / Priority Queue
# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.
# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
#    If the CPU is idle and there are no available tasks to process, the CPU remains idle.
#    If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
#    Once a task is started, the CPU will process the entire task without stopping.
#    The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

# Min-Heap Solution with Sorting
# Complexities:
# Time : O(n * logn)
# Space: O(n)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key = lambda task : task[0])

        result, min_heap = [], []

        i, time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not min_heap:
                time = tasks[i][0]
            else:
                proc_time, index = heapq.heappop(min_heap)
                time += proc_time
                result.append(index)
        return result

