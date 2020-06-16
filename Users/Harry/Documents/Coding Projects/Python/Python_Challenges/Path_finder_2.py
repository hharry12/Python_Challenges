def path_finder(maze):
    row_length = maze.find('\n')
    tracking = []
    tally = 0
    function = Path_Find()
    count = function.expand([0], maze, row_length, tracking, tally)
    return count
    
class Path_Find:

    def __init__(self):
        self.count = [0]
        self.high_count = False
        self.elements = []

    def expand(self, elements, maze, row_length, tracking, tally):
        tally += 1
        if tally == row_length**10:
            return self.high_count
        new_elements = []
        for element in elements:
            tracking.append(element)
            self.count.append(self.count[-1] + 1)
            for i in [1, -1, row_length + 1, - (row_length + 1)]:
                if element + i < 0 or element + i > len(maze) - 1:
                    pass
                else:
                    if maze[element + i] == ".":
                        if element + i == len(maze) - 1:
                            self.high_count = tally
                            return self.high_count
                        else:
                            if element + i in tracking:
                                pass
                            else:
                                if new_elements.count(element + i) == 0:
                                    new_elements.append(element + i)
        self.elements.append(new_elements)
        result = self.expand(self.elements[tally - 1], maze, row_length, tracking, tally)
        self.count.append(self.count[-1] - 1)
        return result                 

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])


b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])


c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))