// LeetCode 0392 - Is Subsequence
// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

// Iterative Solution
// Complexities:
// Time : O(n) - O(m or n) whichever is greater
// Space: O(1)
bool isSubsequence(char* s, char* t) {
    int s_index, t_index = s_index = 0;
    int s_len = strlen(s);
    int t_len = strlen(t);

    while (s_index < s_len && t_index < t_len) {
        if (s[s_index] == t[t_index++]) { s_index++; }
    }
    return s_index == s_len ? true : false;
}
