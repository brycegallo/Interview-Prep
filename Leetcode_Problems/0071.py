# LeetCode 0071 - Simplify Path
# Medium - Stack
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
# The rules of a Unix-style file system are as follows:
#    A single period '.' represents the current directory.
#    A double period '..' represents the previous/parent directory.
#    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
#    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#    The path must start with a single slash '/'.
#    Directories within the path must be separated by exactly one slash '/'.
#    The path must not end with a slash '/', unless it is the root directory.
#    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

# Single Stack Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""

        for character in path + "/":
            if character == "/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current != "" and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += character
        return "/" + "/".join(stack)

