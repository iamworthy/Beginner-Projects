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

#give choices values

choice = input('Enter choice 1/2/3/4: ')

num1 = input('Enter first number ')

num2 = input('Enter second number ')

#calculations

if choice == '1' and num1.isdigit()==True and num2.isdigit()==True:

    print(num1,'+',num2,'=', add(num1,num2))
 

elif choice == '2' and num1.isdigit()==True and num2.isdigit()==True:

     print(num1,'-',num2,'=', subtract(num1,num2))
 

elif choice == '3' and num1.isdigit()==True and num2.isdigit()==True:

    print(num1,'*',num2,'=', multiply(num1,num2))
   

elif choice == '4' and num1.isdigit()==True and num2.isdigit()==True:

    print(num1,'/',num2,'=', divide(num1,num2))


else:

    print('Invalid character entered')
