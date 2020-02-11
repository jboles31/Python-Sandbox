
num = [1,2,3]
nums = [x*10 for x in num]
# nums = [10,20,30]

name = 'colt'
upper_name = [char.upper() for char in name]
# upper_name = ['C', 'O', 'L', 'T']

friends = ['evan', 'sean', 'mark']
upper_friends = [friend[0].upper() for friend in friends]
# upper_friends = ['Evan', 'Sean', 'Mark']

numbers = [1,2,3,4,5,6]
odd_even = [num*2 if num %2 == 0 else num/2 for num in numbers]
print(odd_even)

with_vowels = 'This is so much fun'
without_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(without_vowels)

# NESTED LISTS

nested_list = [[1,2,3], [4,5,6], [7,8,9]]
[[print(val) for val in l] for l in nested_list]

# Board
# board = [[val for val in range(1,4)] for num in range(1,4)]
board = [['X' if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(board)

answer = [[num for num in range(0,10)] for val in range(0,10)]
print(answer)

# SLICES

#  list[ start(inclusive), stop(non-inclusive), step]

first_list = [1,2,3,4,5,6]
first_list[1::2] # [2,4,6]
first_list[::2] # [1,3,5]

#  Negative steps!

first_list[1::-1] # [2,1]
first_list[:1:-1] # [6,5,4,3]
first_list[2::-1] # [3,2,1]

# REVERSE

first_list[::-1] # [6,5,4,3,2,1]

