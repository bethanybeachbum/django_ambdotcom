"""
Working with files
"""

# appending to an existing file
filename = 'Data/my_data.txt'
with open(filename, 'a') as f:
    f.write("fat: 4 grams\n")

# writing to an empty file:
filename = 'user_food_entry.txt'
with open(filename, 'w') as f:
  filename.write("I love programming!")


