// Leetcode 0069 - Sqrt(x)
// Easy - Binary Search
// Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
// You must not use any built-in exponent function or operator.
// For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

// Binary Search Solution
// Complexities:
// Time : O(logn)
// Space: O(1)
int mySqrt(int x) {
    int left = 0;
    int right = x;
    int result = 0;

    if (x == 0 || x == 1) {
        return x;
    }

    while (left <= right) {
        int middle = left + ((right - left) / 2);
        if (middle > x / middle) {
            right = middle - 1;
        }
        else if (middle < x / middle) {
            left = middle + 1;
            result = middle;
        }
        else {
            return middle;
        }
    }
    return result;
}
