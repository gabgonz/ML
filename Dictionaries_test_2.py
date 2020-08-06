# 10 Stride Length
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# 11 Stride Length Practice
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]
print to_21
print odds
print middle_third

# 12 Anonymous Functions
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# 13 Lambda Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: len(x) == 6, languages)

#14 Filter() and Lambda()
squares = [x**2 for x in range(1,11)]
print filter(lambda x: 30 <= x <= 70, squares)

# 15 Iterating Over Dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
for key in movies:
  print movies.items()

 # 16 Comprehending Comprehensions
 threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

# 17 List Slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# 18 Lambda Expressions
ggarbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", ggarbled)
print message