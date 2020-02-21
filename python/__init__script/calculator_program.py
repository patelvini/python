from calculator_pkg import *

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

print("Addition is : ",addition_fun(n1,n2))
print("Subtraction is : ",subtraction_fun(n1,n2))
print("Multiplication is : ",multiplication_fun(n1,n2))
print("Division is : ",division_fun(n1,n2))

and_result = and_fun(n1,n2)
or_result = or_fun(n1,n2)
xor_result = xor_fun(n1,n2)


print("{} AND {} is -> {} ".format(n1,n2,and_result))
print("{} OR {} is -> {} ".format(n1,n2,or_result))
print("{} XOR {} is -> {} ".format(n1,n2,xor_result))


