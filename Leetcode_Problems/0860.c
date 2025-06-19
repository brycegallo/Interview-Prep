// LeetCode 0860 - Lemonade Change
// Easy - Greedy Algorithms
// At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
// Note that you do not have any change in hand at first.
// Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

// Greedy Solution (Terse)
// Complexities:
// Time : O(n)
// Space: O(1)
bool lemonadeChange(int* bills, int billsSize) {
    int five, ten = five = 0;
    for (int i = 0; i < billsSize; i++) {
        if ((bills[i] > 9 && five == 0) || (bills[i] > 10 && !((five > 0 && ten > 0) || (five >2)))) {
            return false;
        } else if (bills[i] == 5) {
            five += 2;
        } else if (bills[i] == 10 || ten > 0) {
            ten = bills[i] == 10 ? ten + 1 : ten - 1;
        } else {
            five -= 2;
        }
        five--;
    }
    return true;
}
