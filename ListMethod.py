list1 = [2, 8, 4, 10, 6, 1, 3, 5, 7,]
list2 = ['banana', 'apples', 'mango', 'oranges']
list2.append('Cherry')
list2.insert(1, 'carrot')
list2.remove('banana')
list2.clear()
list1.extend(list2)
list1.sort()
list1.reverse()
print(list1)
# the len function is used to check the length of the 
# list. list 1 will print the whole number both
# list1 and list2 while list2 only display the 
# number on list2
# to remove a value you use the word remove
# to clear you use clear function
print(len(list1))

# extend function combine the two list together while
# the append function or method add the value to the
# list as you can see above.
# insert function insert a value in-between values
# in a list

print(list1.index(10))
print(list1.count(1))
# sort function arrange the numbers in arithmetically.
# while reverse function will reverse the numbers