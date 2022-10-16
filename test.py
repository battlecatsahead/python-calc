print("enter first input")
first = input()
firstint = int(first)
print("enter second input")
second = input()
secondint = int(second)

print("enter expression:+, -, *, /")
expression = input()



if (expression == "+"):
	print(firstint + secondint)
if (expression == "-"):
	print(firstint - secondint)
if (expression == "*"):
	print(firstint * secondint)
if (expression == "/"):
	print(firstint / secondint)
