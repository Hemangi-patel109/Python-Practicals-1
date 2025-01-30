a = int(input("Enter no. one: "))
b = int(input("Enter no. second: "))

print("Before swaping : a=",a," b=",b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swaping : a=",a," b=",b)