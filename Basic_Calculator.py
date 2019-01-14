# test code for simple calculator

 
#def functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#start

print('Select one of the following operations')
print('1 Add')
print('2 subtract')
print('3 multiply')
print('4 divide')


#calculations
choice = None
num1 = None
num2 = None

while choice is None:
    try:
        choice = int(input('Enter choice 1/2/3/4: '))
    except ValueError:
        print('ENTER AN INTEGER, GOD DAMMIT!!!')

while num1 is None:
    try:
        num1 = int(input('Enter first number: '))
    except ValueError:
        print('ENTER AN INTEGER, GOD DAMMIT!!!')

while num2 is None:
    try:
        num2 = int(input('Enter Second number: '))
    except ValueError:
        print('ENTER AN INTEGER, GOD DAMMIT!!!')
        
if choice == 1:
    print(num1,'+',num2,'=', add(num1,num2))

elif choice == 2:
     print(num1,'-',num2,'=', subtract(num1,num2))

elif choice == 3:
    print(num1,'*',num2,'=', multiply(num1,num2))

elif choice == 4:
    print(num1,'/',num2,'=', divide(num1,num2))

else:
    print('Did not enter 1,2,3 or 4!')
