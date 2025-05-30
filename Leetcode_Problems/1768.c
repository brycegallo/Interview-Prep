// LeetCode 1768 - Merge Strings Alternately
// Easy - Two Pointers
// You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
//
// Return the merged string.

// Two-pointer Solution
// Complexities:
// Time : O(m+n)
// Space: O(m+n) 
char * mergeAlternately(char * word1, char * word2){
    // assume caller will free() or else we'll encounter memory leaks
    char* result = malloc(strlen(word1)+strlen(word2)+1);
    int result_index = 0;
    int words_index = 0;

    while (words_index < strlen(word1) && words_index < strlen(word2)) {
        result[result_index++] = word1[words_index];
        result[result_index++] = word2[words_index++];
    }
    // avoiding using strcpy() and strncpy() in these while loops for safety reasons
    while (words_index < strlen(word1)) {
        result[result_index++] = word1[words_index++];
    }
    while (words_index < strlen(word2)) {
        result[result_index++] = word2[words_index++];
    }
    // must make last character null
    result[result_index] = '\0';
    return result;
}
