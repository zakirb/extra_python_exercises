# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***
array = [1,1,2,2,3,3,4,5,5,6,6,7,7]

def find_odd_man(num_list):
  oddman = []
  all_men = []
  normal_men = []
  for i in range(len(num_list)):
    if num_list[i] not in all_men:
      all_men.append(num_list[i])
    else:
      normal_man.append(num_list[i])
  for i in range(len(num_list)):
    if num_list[i] not in normal_man:
      print(f"The odd man is {num_list[i]}")

find_odd_man(array)
