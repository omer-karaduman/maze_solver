from cell import Cell
import time
import random
class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self._cells = []
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0,0)
    self._reset_cells_visited()
    if seed != None:
      self.seed = random.seed(seed)
    else:
       self.seed = random.seed(0)


  def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

  def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
  def _animate(self):
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)



  def _break_walls_r(self, i, j):
     
     current = self._cells[i][j]
     current.visited = True
     while True:
      directions = []
      can_go = []
      if i != self._num_cols-1:
           if not self._cells[i+1][j].visited:
              
            can_go.append((i+1,j))
            
            directions.append("right")

      if not self._cells[i-1][j].visited:
           
           if i != 0:

            can_go.append((i-1,j))
            directions.append("left")
      
      if not self._cells[i][j-1].visited:          
           if j != 0:             
            can_go.append((i,j-1))
            directions.append("up")
      
      if j != self._num_rows-1:
           if not self._cells[i][j+1].visited:
             
            can_go.append((i,j+1))
            directions.append("bottom")

      if len(can_go) == 0 :
          self._draw_cell(i,j) 
          return 
      random_direction = random.randrange(len(can_go))
      direction = can_go[random_direction]
      chosen_cell = self._cells[direction[0]][direction[1]]
      if directions[random_direction] == "bottom":
          current.has_bottom_wall=False
          chosen_cell.has_top_wall = False
      if directions[random_direction] == "up":
          current.has_top_wall = False
          chosen_cell.has_bottom_wall = False
      if directions[random_direction] == "right":
          current.has_right_wall = False
          chosen_cell.has_left_wall = False
      if directions[random_direction] == "left":
          current.has_left_wall = False
          chosen_cell.has_right_wall = False
  
      self._break_walls_r(direction[0],direction[1])
  def _reset_cells_visited(self):
     for i in self._cells:
        for cel in i:
           cel.visited = False
  def _solve(self):
     return self._solve_r(0,0)
  
  def _solve_r(self,i,j):
     self._animate()
     current = self._cells[i][j]
     current.visited = True
     if i == self._num_cols-1 and j == self._num_rows -1:
      return True
     
     if i>0 and self._cells[i][j].has_left_wall == False and not  self._cells[i-1][j].visited:
        current.draw_move(self._cells[i-1][j])
        result = self._solve_r(i-1,j)
        if result:
           return result
        current.draw_move(self._cells[i-1][j],True)

     if i <self._num_cols-1 and self._cells[i][j].has_right_wall == False and not self._cells[i+1][j].visited:
        current.draw_move(self._cells[i+1][j])
        result = self._solve_r(i+1,j)
        if result:
           return result
        current.draw_move(self._cells[i+1][j],True)

     if j< self._num_rows-1 and self._cells[i][j].has_bottom_wall == False and not  self._cells[i][j+1].visited:
        current.draw_move(self._cells[i][j+1])
        result = self._solve_r(i,j+1)
        if result:
           return result
        current.draw_move(self._cells[i][j+1],True)

     if j > 0 and self._cells[i][j].has_top_wall == False and not self._cells[i][j-1].visited :
        current.draw_move(self._cells[i][j-1])
        result = self._solve_r(i,j-1)
        if result:
           return result
        current.draw_move(self._cells[i][j-1],True)


     return False
         
           
    