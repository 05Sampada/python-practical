a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
s = input("Enter a string: ")

# Arithmetic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division by zero not possible")

print("Power:", a ** b)

# String operations
print("Concatenation:", s + " Assignment")
print("Repetition:", s * 3)
print("Slicing:", s[0:3])
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
