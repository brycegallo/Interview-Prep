// LeetCode 1572 - Matrix Diagonal Sum
// Easy - Math & Geometry
// Given a square matrix mat, return the sum of the matrix diagonals.
// Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

// Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum = 0;
    for (int i = 0; i < matSize; i++) {
        sum += mat[i][i] + mat[i][matSize - 1 - i];
    }
    return matSize % 2 > 0 ? sum - mat[matSize / 2][matSize / 2] : sum;
}
