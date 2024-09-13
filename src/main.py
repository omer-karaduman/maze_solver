from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze
import sys
def main():
    sys.setrecursionlimit(10000)
    win = Window(800, 600)
    
    num_cols = 50
    num_rows = 50
    m1 = Maze(20, 20, num_rows, num_cols, 10, 10,win)
    if m1._solve():
        print("Solved")
    else:
        print("It can't be solvable")
    win.wait_for_close()

main()