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
                    int shif = (1 << val);

                    if ((rowSet[row] & shif) || (colSet[col] & shif) ||
                        (boxSet[boxIndex] & shif)) {
                        return false;
                    }

                    rowSet[row] = rowSet[row] | shif;
                    colSet[col] = colSet[col] | shif;
                    boxSet[boxIndex] = boxSet[boxIndex] | shif;
                }
            }
        }
        return true;
    }
};
