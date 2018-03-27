# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implement a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***

def fibonacci(length):
  number_list = [0,1]
  for i in range(2, length):
    sum = number_list[i-1] + number_list[i-2]
    number_list.append(sum)
  return number_list

#test
print(fibonacci(10))
