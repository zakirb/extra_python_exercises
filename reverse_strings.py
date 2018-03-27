# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***
def reverse_words(string):
  string_list = string.split(' ')
  print(string_list)
  for i in range(len(string_list)):
    string_list[i] = string_list[i][::-1]
  reversed_words = ' '.join(string_list)
  print(reversed_words)

reverse_words("Hello my friends")
