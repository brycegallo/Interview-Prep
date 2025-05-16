// LeetCode 3110 - Score of a String
// Easy - Arrays & Hashing
// You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
// Return the score of s.

// Iterative Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int scoreOfString(char* s) {
    int i, score = i = 0;
    while (i < strlen(s) - 1) {
        score += abs(0 - (int)s[i] + (int)s[++i]);
    }
    return score;
}
