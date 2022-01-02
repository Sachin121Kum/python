print("""
+ ADD 
- SUBTRACT
* MULTIPLY
/ DIVIDE
""")

num1=int(input("Enter The Value 1"))
num2=int(input("ENter The Value 2"))
opr=input("Enter the Opearator")

if opr is "+":
    print(num1+num2)
if opr is "-":
    print(num1-num2)
if opr is "*":
    print(num*num2)
if opr is "/":
    print(num1/num2)

if opr is not "+" and opr is not "-" and opr is not "*" and opr is not "/":
    print("Invalid Operator")