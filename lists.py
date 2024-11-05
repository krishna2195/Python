mylist  = ["banana", "cherry", "apple"]
print(mylist)

#calling item to in list
item  = mylist[0]
item2 = mylist[-1]

print(item, item2)

#print all elements
for x in mylist:
    print(x)

# to check for elements
if "banana" in mylist:
    print(yes)
else:
    print(no)

#LENGTH of my list
len(mylist)

#append
mylist.append("lemon")
print(mylist)

#in a specific position
mylist.insert(2, "strawberry")
print(mylist)

#pop gives and removes last item
popitem = mylist.pop()
print(popitem)

#remove specific element
remitem = mylist.remove("strawberry")
print(mylist)

#clear list
mylist.clear()

#reverse list
mylist.reverse()

mylistnum = [-3,2,0,-5,6]

#sort list in list
mylistnum.sort()

#to sort in newlist
new_list = sorted(mylistnum)
print(new_list)

#list operators
#multiply
oplist = [0]*5
print(oplist)

#concatnate
addlist = [1,2,3,4,5]
new_list2 = oplist + addlist
print(new_list2)

##Slicing
sli_list = [1,2,3,4,5,6,7,8,9]
a =  sli_list[1:5]
print(a)

b =  sli_list[:5]
print(b)


#step
c =  sli_list[1:]
print(c)

#copy
list_org = ["banana", "cherry", "apple"]

list_cpy1 = list_org.copy()
list_cpy2 = (list_org)
list_cpy3 = list_org[:]

# list comprehension
