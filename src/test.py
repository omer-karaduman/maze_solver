import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):

     
    def test_maze_reset_cells_visited(self):

        win = Window(360,120)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,win)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

      

if __name__ == "__main__":
    unittest.main()