with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n")

state = 50
total_zeros = 0

for line in splitfile:
  if line[0] == "L":
    state -= int(line[1:])
  else:
    state += int(line[1:])
  state %= 100
  if state == 0:
    total_zeros += 1
print(total_zeros)
