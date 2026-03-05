# -1) Explain in comments the difference between list / set / tuple.

#in a list you can change stuff 

#in a tuple you cant change stuff

#in a set




# 0) Explain in comments the following methods:
# add / update / remove / discard / union 

#an add is when you add an element to a set

#an update is when you update the set like if it says anna mark and stacy you can update it to add annabelle so it will be
# updated every time you run it and it will be added to the set so it will be like anna,mark,stacy,annabelle

#an remove is when you remove a name a num or a symbol from the set like anna stacy and mark so if you want to 
# remove mark you can write to remove it and it will be like anna,stacy but if you remove an name
#  from it that it does not have it will print an error

#an discard is same as an remove but when you type an name thats not there nothing will be printed

#an union is when you add an element to it like group1.union(group2) it wiill add the both group sets together

# Create two sets: group1 and group2.

group1 = {"vano","giorgi","Lukiana"}
group2 = {"mark","annabelle","stacy"}

group1.add("anna")



print(group1)
# 1) Use the add() method and add one new element to group1.
#done


# 2) Use the update() method and add multiple elements to group2.
set1 = {"vano","giorgi","Lukiana"}
set2 = {"mark","annabelle","stacy"}

set1.update(set2)

print(set1)


# 3) Use the remove() method and delete one element from group1.

x = group1.remove("vano")

print(x)
# 4) Use the discard() method and delete one element from group2.

y = group2.discard("Lukiana")

print(y)

# 5) Use the union() method and create a new set that combines both groups.

i = group1.union(group2)

print(i)

# 6) Print all the results using the print() function.
#done
# 7) Create a tuple named numbers, which contains at least 8 numbers (some numbers should be repeated).

numbers = (1,6,3,1,4,5,6,7,8,1,1,2,3,5,6,8,7,7,3)

print(numbers)


# 8) Print the third and seventh elements using indexing.

# 9) Use slicing and print elements from index 2 to 6.



# 10) Use count() and count how many times a chosen number appears.




# 11) Use index() and find the index of a specific element.

# 12) Create a second tuple and concatenate (add) it to the first one.

# 13) Convert the tuple to a list, add one element, then convert it back to a tuple and print the final result.