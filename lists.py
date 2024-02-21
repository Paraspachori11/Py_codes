#list creation
a = [1,2,4,56,6]

#printing the list using print() function
print(a)

#index elment accessing
print(a[0])

#updation of certain index value
a[0] = 98
print(a) 

#list can include items of different types
c = [1,"paras",False,9.5]

#list slicing
friends = ["harry","tom","brock","bill",45]
print(friends[0:4])
print(friends[-4:])#in this case indexing starts from right side from -1 and goes to the left with decrement like -2,-3,-4 and so on
print(friends[-4:-1])