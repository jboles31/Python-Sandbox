# SETS

# do not have duplicate values
# elements in sets aren't ordered
# cannot access items in a set by index


set_example = {1, 4, 5}

# function to create a set
s = set({1,4,5})

# if you have duplicates, set will remove them
s1 = {1,2,4,4,4}
# will equal {1,2,4}

# USES
# need to keep track of a collection of elements
# don't care about ordering, keys or values and duplicates

# if you have a list of all the cities of where people at a confrence are 
# from but you just want all the cities without the duplicates
cities = ["LA", "Boulder", "LA", "NYC", "NYC"]
cities = list(set(cities))
print(cities)