// LeetCode 2678 - Number of Senior Citizens
// Easy - Arrays & Hashing
// You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:
//    The first ten characters consist of the phone number of passengers.
//    The next character denotes the gender of the person.
//    The following two characters are used to indicate the age of the person.
//    The last two characters determine the seat allotted to that person.
// Return the number of passengers who are strictly more than 60 years old.

// Iterative Solution - converting chars to ints
// Complexities:
// Time : O(n)
// Space: O(1)
int countSeniors(char** details, int detailsSize) {
    int count = 0;
    for (int i = 0; i < detailsSize; i++) {
        char* str = details[i]+11; 
        int num1 = str[0] - '0';
        int num2 = str[1] - '0';
        if (num1 > 6 || (num1 == 6 && num2 != 0)) {
            count++;
        }
    }
    return count;
}
