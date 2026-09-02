class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cell = 0
        squares = collections.defaultdict(set)
        for r in range(len(board)):
            my_hor_set = set()
            my_ver_set = set()
            for c in range(len(board)):
                hor_cell = board[r][c]
                ver_cell = board[c][r]

                if hor_cell != ".":
                    key = (r // 3, c // 3)
                    if hor_cell in squares[key]:
                        return False

                    squares[key].add(hor_cell)

                    if hor_cell in my_hor_set:
                        return False
                    my_hor_set.add(hor_cell)

                if ver_cell != ".":
                    if ver_cell in my_ver_set:
                        return False
                    my_ver_set.add(ver_cell)    
        return True

                

                
                    
