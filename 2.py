# List 
L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List:", L)
print("Indexing:", L[2])
print("Slicing:", L[1:5])

# Tuple
T = ("Apple", "Mango", "Banana", "Grapes", "Orange")
print("Tuple:", T)
print("Indexing:", T[1])
print("Slicing:", T[1:4])

# Dictionary
D = {"Amit": 80, "Riya": 90, "Sam": 75,
     "Neha": 85, "Raj": 70}
print("Dictionary:", D)

D["Pooja"] = 95       # Add
D["Amit"] = 88        # Update
del D["Raj"]          # Delete
print("Updated Dictionary:", D)

# Sets with duplicates
A = {1, 2, 3, 4, 4, 5, 5, 6}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
