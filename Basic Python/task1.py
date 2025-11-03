#Day 1: Task
# ---------- LIST ----------
list1 = [1,5,10,5.25,3.69,"Riya",2,2.5,"Lama",[4,5,6]]
print("List indexing:", list1[4]) # 3.69
print("List slicing:", list1[2:7]) # [10, 5.25, 3.69, 'Riya', 2]

# ---------- STRING ----------
name = "Riya Lama"
print("String indexing:", name[7]) # 'm'
print("String slicing:", name[0:6]) # 'Riya L'

# ---------- TUPLE ----------
tuple1 = (1,2,3,4,"Riya",6,7,[1,2,3])
print("Tuple indexing:", tuple1[4]) # 'Riya'
print("Tuple slicing:", tuple1[1:5]) # (2, 3, 4, 'Riya')

# ---------- SET ----------
set1 = {1,2,3,"Riya","Lama","GHI"}
set2 = {"ABC","DEF","GHI"}
# Note: Sets have no indexing or slicing because they are unordered
print("Set difference:", set1.difference(set2)) # elements in set1 but not in set2
print("Set union:", set1.union(set2)) # all unique elements
print("Set intersection:", set1.intersection(set2)) # common elements

