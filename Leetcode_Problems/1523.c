// LeetCode 1523 - Count Odd Numbers in an Interval Range
// Easy - Math & Geometry
// Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

// Solution
// Complexities:
// Time : O(1)
// Space: O(1)
int countOdds(int low, int high){
    int count = (high - low + 1) / 2;
    return low % 2 == 1 && high % 2 == 1 ? count + 1 : count;
}
