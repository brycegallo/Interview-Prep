// LeetCode 0881 - Boats to Save People
// Medium - Two Pointers
// You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
//
// Return the minimum number of boats to carry every given person.

// Two Pointer Solution with Sorting
// Complexities:
// Time : O(n * logn)
// Space: O(1)
int compare(const void* a, const void* b) {
    int* int_a = a;
    int* int_b = b;
    return *int_a - *int_b;
}

int numRescueBoats(int* people, int peopleSize, int limit) {
    qsort(people, peopleSize, sizeof(people[0]), compare);

    int result;
    int left = 0;
    int right = peopleSize - 1;

    for (result = 0; left <= right; result++) {
        int remaining_weight = limit - people[right--];
        if (left <= right && remaining_weight >= people[left]) {
            left++;
        }
    }
    return result;
}
