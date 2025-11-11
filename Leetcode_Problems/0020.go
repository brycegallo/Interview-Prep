// LeetCode 0020 - Valid Parentheses
// Easy - Stack
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// An input string is valid if:
//     Open brackets must be closed by the same type of brackets.
//     Open brackets must be closed in the correct order.
//     Every close bracket has a corresponding open bracket of the same type.

// Solution
// Complexities:
// Time : O(n)
// Space: O(n)
func isValid(s string) bool {
    stack := linkedliststack.New()
    close_to_open := map[rune]rune{')': '(', ']': '[', '}': '{'}

    for _, close := range s {
        if open, exists := close_to_open[close]; exists {
            if !stack.Empty() {
                top, ok := stack.Pop()
                if ok && top.(rune) != open {
                    return false
                }
            } else {
                return false
            }
        } else {
            stack.Push(close)
        }
    }
    return stack.Empty()
}
