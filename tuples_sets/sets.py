# SETS

# do not have duplicate values
# elements in sets aren't ordered
# cannot access items in a set by index

# USES
# need to keep track of a collection of elements
# don't care about ordering, keys or values and duplicates

set_example = {1, 4, 5}

# function to create a set
s = set({1,4,5})

# if you have duplicates, set will remove them
s1 = {1,2,4,4,4}
# will equal {1,2,4}


# if you have a list of all the cities of where people at a confrence are 
# from but you just want all the cities without the duplicates
cities = ["LA", "Boulder", "LA", "NYC", "NYC"]
cities = list(set(cities))
print(cities)

# SET METHODS


# .add()

# adds an element to a set, if element already in set it doesn't change

s = set([1,2,3]) #or s = {1,2,3}
s.add(4)
print(s) # s = {1,2,3,4}


# .remove()

# removes a given element from the set,
# returns a KeyError if value is not found
# AVOID KeyError with .discard()

set1 = {1,2,3,4,5}
set1.remove(2)
print(set1) #set1 = {1,3,4,5}


# .copy()

# make a copy of an existing set

set2 = {1,2,3}
another_s = set2.copy()
print(another_s) #another_set = {123}
# another_s is set2 = FALSE


# COMPARING

set10 = {1,2,3,4}
set11 = {3,4,5,6}

set10 || set11 = {1,2,3,4,5,6}
set10 && set11 = {3,4}
