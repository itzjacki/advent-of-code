with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")
  grid = [list(line) for line in splitfile]

  max_y = len(grid)
  max_x = len(grid[0])

  def get_neighbors(row, col):
    vectors = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
               (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []

    for v in vectors:
      square_new = (row + v[0], col + v[1])
      if 0 <= square_new[0] < max_y and 0 <= square_new[1] < max_x:
        neighbors.append(square_new)

    return neighbors

  def is_roll(row, col): return grid[row][col] == "@"

  available = 0

  for row in range(max_y):
    for col in range(max_x):
      if is_roll(row, col):
        neighbor_rolls = 0
        for s in get_neighbors(row, col):
          if is_roll(s[0], s[1]):
            neighbor_rolls += 1
        if neighbor_rolls < 4:
          available += 1

  print(available)
