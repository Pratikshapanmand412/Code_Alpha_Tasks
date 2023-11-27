def fibonacci_series():
    num1,num2 = 0,1
    while True:
        yield num1
        num1,num2 =num2,num1+num2


number = int(input("Enter a number to generate fibonacci series :"))
print(number,"numbers of fibonacci series")
result = fibonacci_series()
for i in range (number):
    print(next(result),end=" ")