
import math
with open("02/input.txt", "r") as f:
  splitfile = f.read().split(",")

  def is_even_length(n): return len(n) % 2 == 0

  def n_nines(n): return int("9" * n)

  sum = 0

  for segment in splitfile:
    start_string, stop_string = segment.split("-")
    start, stop = int(start_string), int(stop_string)

    # This solution assumes that the ranges are between numbers that are at most 1 power of magnitude apart
    if not is_even_length(start_string) and not is_even_length(stop_string):
      continue

    for i in range(n_nines(math.ceil(len(stop_string) / 2))):
      i_doubled = int(str(i) * 2)
      if start <= i_doubled <= stop:
        sum += i_doubled

  print(sum)
