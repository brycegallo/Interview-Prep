// LeetCode 0263 - Ugly Number
// Easy - Math & Geometry
// An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
// Given an integer n, return true if n is an ugly number.

// Solution
// Complexities:
// Time : O(log2 n)
// Space: O(1)
bool isUgly(int n) {
    int primes[3] = {2, 3, 5};
    for (int i = 0; n > 0 && i < 3; i++) { while (n % primes[i] == 0) { n /= primes[i]; } }           
    return n == 1;
}
