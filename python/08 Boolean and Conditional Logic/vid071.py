a = 1
a == 1  # true
a is 1  # true

a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]

a == b  # true
a is b  # false

# the difference is == is checking if the values are the same. a is b is checking to see if they are stored in the same place in memeroy.

c = b
b is c  # is true because when you make c = b, they are pointing to the same list in memory.

x = 13
y = 13

x == y  # true
x is y  # true

a = [1, 2]
b = [1, 2]
a == b  # true. contains same values

a is b  # not true because when brackets are made, a new list in memeory is created. they are unique in memeory.

clone = a
a is clone  # true
