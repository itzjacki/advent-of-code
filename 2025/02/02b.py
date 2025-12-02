with open("02/input.txt", "r") as f:
  splitfile = f.read().split(",")

  def n_nines(n): return int("9" * n)

  def find_ids(expression_length, start, stop):
    ids = set()
    for repetitions in range(2, expression_length + 1):
      if expression_length % repetitions == 0:
        for i in range(n_nines(expression_length // repetitions) + 1):
          i_repeated = int(str(i) * repetitions)
          if start <= i_repeated <= stop:
            ids.add(i_repeated)
    return ids

  sum = 0

  for segment in splitfile:
    start_string, stop_string = segment.split("-")
    start, stop = int(start_string), int(stop_string)

    if len(start_string) == len(stop_string):
      ids = find_ids(len(start_string), start, stop)
    else:
      # This solution assumes that the ranges are between numbers that are at most 1 power of magnitude apart
      ids = find_ids(len(start_string), start, stop).union(
          find_ids(len(stop_string), start, stop))
    for id in ids:
      sum += id

  print(sum)
