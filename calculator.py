def add(a,b):
    return a + b 

def sub(a,b):
    return a - b 

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b 

def mul(a,b):
    return a*b

print("1. Addition ")
print("2. Subtraction ")
print("3. Division ")
print("4. Multiplication ")
print("5. Exit ")

s = int(input("Enter your choice: "))

if s in [1,2,3,4]:
    n = float(input("Enter first number: "))
    m = float(input("Enter second number: "))

    if s == 1:
        print("Result:", add(n,m))
    elif s == 2:
        print("Result:", sub(n,m))
    elif s == 3:
        print("Result:", div(n,m))
    elif s == 4:
        print("Result:", mul(n,m))

elif s == 5:
    print("Thank you for your visit")

else:
    print("Please select a valid choice")