def path_finder(maze):
    row_length = maze.find('\n')
    tracking = []
    function = Path_Find()
    can_be_done = function.expand(0, maze, row_length, tracking)
    return can_be_done
    
class Path_Find:
    
    def expand(self, element, maze, row_length, tracking):
        tracking.append(element)
        for i in [1, -1, row_length + 1, - (row_length + 1)]:
            if element + i < 0 or element + i > len(maze) - 1:
                pass
            else:
                if maze[element + i] == ".":
                    if element + i == len(maze) - 1:
                        return True
                    else:
                        if element + i in tracking:
                            pass
                        else:
                            if self.expand(element + i, maze, row_length, tracking) == True:
                                return True
        return False
        

d = "\n".join([
  ".W...W",
  ".W.W.W",
  ".W.W.W",
  ".W.W.W",
  ".W.W..",
  "...WW."
])

print(path_finder(d))