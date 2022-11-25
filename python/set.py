# A set is a collection which is unordered, unchangeable*, and unindexed. Duplicate value ignore
"""
================================================
Method    ========= 	Description
================================================
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()	            Removes the items in this set that are also included in another, specified set
discard()	                    Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
"""
"""x = {"apple", "apple", "banana", "orange", "pineapple", 5, True, False}
print(type(x))
print(x)
print(len(x))

#x = set(("apple", "apple", "banana", "orange"))
#print(type(x))

# add the item in a set
x.add(6)
print(x)

# add another set for use update() method
y = set(("potato", "graph"))
x.update(y)
print(x)

# list add in set by update
z = ['egg', 'mango']
x.update(z)
print(x)

# remove item in a set
x.remove("banana")
x.discard("apple")

i = x.pop()
print(i)
print(x)

#x.clear()
#print(x)

#del x
#print(x) #this will raise an error because the set no longer exists

# Loop set
print("###---------The loop value is: --------###")
for a in x:
    print(a)"""

# union amd update exclude duplicate value
b = {"bangladesh", "india", "pakistan", "nepal", "bhutan"}
c = {"afghanistan", "myanmar", "bangladesh", "nepal"}
# set1 = b.union(c)
# print(set1)
#
# b.update(c)
# print(b)

# keep only duplicate or common value
# set2 = b.intersection(c)
# print(set2)
#
# b.intersection_update(c)
# print(b)

# keep all except duplicate
# c.symmetric_difference_update(b)
# print(b)

# keep value that are not present
set3 = b.symmetric_difference(c)
print(set3)

b.symmetric_difference_update(c)
print(b)