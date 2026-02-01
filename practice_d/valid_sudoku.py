board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


for i in range(len(board[0])):
    nums = set()
    for x in range(len(board)):
        val = board[i][x]
        if val!=".":
            if val in nums or int(board[i][x])>9:
                print(f"not valid {i} {x}")
            else:
                nums.add(val)


for x in range(len(board[0])):
    nums = set()
    for i in range(len(board)):
        val = board[i][x]
        if val!=".":
            if val in nums or int(board[i][x])>9:
                print(f"not valid {i} {x}")
            else:
                nums.add(val)

