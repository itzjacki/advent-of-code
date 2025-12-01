with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n")

state = 50
total_zeros = 0
previous = state

for line in splitfile:
  change = int(line[1:])

  if line[0] == "L":
    state -= change
  else:
    state += change

  if state <= 0:
    zeros_this_operation = abs((state - 1) // 100)
    if previous == 0:
      zeros_this_operation -= 1
  else:
    zeros_this_operation = abs(state // 100)

  total_zeros += zeros_this_operation
  state %= 100
  previous = state

print(total_zeros)
