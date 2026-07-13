class Solution {
   public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rowSet[9] = {};
        int colSet[9] = {};
        int boxSet[9] = {};
        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                if (board[row][col] != '.') {
                    int val = board[row][col] - '1';
                    int boxIndex = (row / 3) * 3 + (col / 3);

                    if ((rowSet[row] & (1 << val)) || (colSet[col] & (1 << val)) ||
                        (boxSet[boxIndex] & (1 << val))) {
                        return false;
                    }

                    rowSet[row] = rowSet[row] | (1 << val);
                    colSet[col] = colSet[col] | (1 << val);
                    boxSet[boxIndex] = boxSet[boxIndex] | (1 << val);
                }
            }
        }
        return true;
    }
};
