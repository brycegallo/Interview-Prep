// LeetCode 1137 - N-th Tribonacci Number
// Easy - 1-D Dynamic Programming
// The Tribonacci sequence Tn is defined as follows: 
// T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
// Given n, return the value of Tn.

// One-Dimensional Dynamic Programming Solution
// (fun solution, not too legible, wouldn't submit for an interview)
// Complexities:
// Time : O(n)
// Space: O(1)
int tribonacci(int n) {
    int arr[3] = {1, 0, 0};
    for (int i = 1; i <= n; i++) {
        memcpy(arr, (int[3]){arr[1], arr[2], arr[0] + arr[1] + arr[2]}, 12);
    }
    return arr[2];
}
