#Accept marks in 5 subjects
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))

#average
total = m1 + m2 + m3 + m4 + m5
avg = total / 5

print("Average:", avg)

#Assign grade
if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
elif avg >= 35:
    print("Grade D")
else:
    print("Grade F")

#Check individual subject
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")
