class Solution {
   public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rowSet(9);
        vector<unordered_set<char>> colSet(9);
        vector<unordered_set<char>> boxSet(9);
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                if (board[row][col] != '.') {
                    int boxIndex = (row / 3) * 3 + (col / 3);
                    if (rowSet[row].count(board[row][col]) || colSet[col].count(board[row][col]) ||
                        boxSet[boxIndex].count(board[row][col])) {
                        return false;
                    }

                    rowSet[row].insert(board[row][col]);
                    colSet[col].insert(board[row][col]);
                    boxSet[boxIndex].insert(board[row][col]);
                }
            }
        }
        return true;
    }
};
