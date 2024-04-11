
import numpy as np

sudoku_puzzle=[[9,6,2,0,7,8,5,0,0],
               [1,0,5,0,0,9,3,0,0],
               [3,0,0,5,0,0,8,2,0],
               [0,0,1,0,0,0,0,7,0],
               [6,0,0,0,5,0,0,0,8],
               [0,0,0,6,0,3,9,0,5],
               [0,1,8,0,0,5,0,0,1],
               [0,0,6,8,3,2,7,0,0],
               [7,5,3,1,9,0,4,8,0]]

def possibility(row,col,n):
    global sudoku_puzzle
    for i in range(0,9):
        if sudoku_puzzle[row][i] ==n:
            return False
        
    for i in range(0,9):
        if sudoku_puzzle[i][col] ==n:
            return False
        
    x=(col//3)*3
    y=(row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_puzzle[y+1][x+1]==n:
                return False
    return True

def solution():
    global sudoku_puzzle
    for row in range(0,9):
        for col in range(0,9):
            if sudoku_puzzle[row][col]== 0:
                for n  in range(1,10):
                    if possibility(row,col,n):
                        sudoku_puzzle[row][col]=n
                        solution()
                        sudoku_puzzle[row][col]=0
                
    print(np.matrix(sudoku_puzzle))
    input("More possible solutions")

solution()