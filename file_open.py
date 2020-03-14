"""
Working with files - Opening

"""
# 'Data/my_data.txt'
# '/Users/allenmarkbrown/PROJECTS/nutritionix/Data/my_data.txt'
# first forward slash is very important

f_path = "/Users/allenmarkbrown/PROJECTS/Nutritionix/Data/my_data.txt"

try:
  with open(f_path) as f:
      lines = f.readlines()
  for line in lines:
      print(line.rstrip())

except FileNotFoundError:
  msg = "Can't find file {0}.".format(f_path)
  print(msg)
  # print("\n")
  msg2 = "Inspect path and file name!"
  print(msg2)
