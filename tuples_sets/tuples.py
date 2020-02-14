# TUPLES
# ordered collection of items
# immutable
# cannot update/remove from it

single_element_tuple = (1,)
tuple_example = (1,2,3)
values = (1,2,3)
static_values = tuple(values)

# why use tuple
# faster and lighter weight than a list
# tuples are valid keys in a dictionary, unlike a list, a key of a coordinate location is a good example

# EXAMPLE of a good tuple
# would be the months of the year
# you don't need to ever change the months

# Tuple Unpacking

# Star Args will create a tuple of all the args given. We must unpack the tuple, made from the list provided as an arg
# When you have a function that accepts star args, but is passed a list not multiple args

def sum_all_values(*args):
  total = 0
  for num in args:
    total += num
  print(total)

nums = [1,2,3,4]

# pass list with a star in front
sum_all_values(*nums)
