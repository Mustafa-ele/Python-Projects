print("Welcome to Calculator App")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Operation 
print("Select Operation:")
print("1. Addition (+)")
print("2. Subraction (-)")
print("3. Multuiplication (*)")
print("4. Divison (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
    print("result: ", result)
elif choice == '2':
    result = num1 - num2
    print("result: ", result)
elif choice == '3':
    result = num1 * num2
    print("result: ", result)
elif choice == '4':
    if num2 !=0:
        result = num1 / num2
        print("result: ", result)
    else:
        print("cannot divide by zero!")
else:
    print("Invalid Output")