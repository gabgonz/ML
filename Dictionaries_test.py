#Practicing some basic operations on dictionaries
# 1 Iterators for Dictionaries
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]

# 2 keys() and values()
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]

# 3 The 'in' Operator
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]

# 4 Building Lists
vens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# 5 List Comprehension Syntax
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares

# 6 More of List Comprehension Syntax
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four

# 7 List Slicing Syntax
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

# 8 Omitting Indices
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]

# 9 Reversing a List
my_list = range(1, 11)

backwards = my_list[::-1]
print backwards
