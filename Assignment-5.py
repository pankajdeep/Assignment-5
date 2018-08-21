#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter year to check if it is leap year or not"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a Leap year")
else:
    print("It is not a Leap year")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("Enter Length"))
breadth=int(input("Enter Breadth"))
if(length==breadth):
    print("The given dimensions are of Square")
else:
    print("The given dimensions are of Rectangle")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
p1=int(input("Enter your age"))
p2=int(input("Enter your age"))
p3=int(input("Enter your age"))
if(p1>p2 and p1>p3):
    print("The oldest person is P1")
elif(p2>p1 and p2>p3):
    print("The oldest person is P2")
else:
    print("The oldest person is P3")
    
if(p1<p2 and p1<p3):
    print("The youngest person is P1")
elif(p2<p1 and p2<p3):
    print("The youngest person is P2")
else:
    print("The youngest person is P3")


'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 
1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR".'''
age=int(input("Enter age"))
sex=input("Enter sex - M for male and F for female")
mart=input("Enter marital status - Y for yes and N for no")
if(sex=='F' and age>=20 and age<=60):
    print("You can only work in Urban Areas")
elif(sex=='M'):
    if(age>=20 and age<40):
        print("You can work anywhere")
    elif(age>=40 and age<=60):
        print("You can only work in Urban Areas")
    else:
        print("ERROR")
else:
    print("ERROR")



'''Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.'''
quan=int(input("Enter Quantity in units"))
cost=quan*100
if(cost>1000):
    cost=cost-(0.1*cost)
print("Total cost is",cost)


#------------------------------- LOOPS -----------------------------------------------


#Q.1- Take 10 integers from user and print it on screen.
li=[]
print("Enter 10 integers")
for i in range(10):
    inp=int(input())
    li.append(inp)
print("Integers are:")
for i in range(10):
    print(li[i],end=" ")


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
i=0
while(True):
    i=i+1
    print(i)


#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
li=[]
li2=[]
n=int(input("Enter size of list"))
print("Enter elements")
for i in range(n):
    inp=int(input())
    li.append(inp)
    li2.append(inp**2)
print(li2)


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
list1=[4,3,"Pankaj",5.6,9,"Deep",2.735]
l1_int=[i for i in list1 if isinstance(i,int)]
l2_float=[i for i in list1 if isinstance(i,float)]
l3_string=[i for i in list1 if isinstance(i,str)]
print("Integer list is:",l1_int,"Float list is",l2_float,"String list is",l3_string)


#Q.5- Using range(1,101), make a list containing only prime numbers.
flag=0
li=[]
for i in range(1,101):
    if(i==1):
       pass
    else:
       for j in range(2,i):
           if(i%j==0):
               flag=1
       if(flag==0):
           li.append(i)
    flag=0
print(li)


'''Q.6- Print the following patterns: 
* 
** 
*** 
**** '''
for i in range(1,5):
    print('*'*i)


'''Q.7- Take inputs from user to make a list.
Again take one input from user and search it in the list and delete that element, if found.
Iterate over list using for loop. '''
li=[]
flag=0
n=int(input("Enter size of list"))
print("Enter elements")
for i in range(n):
    inp=int(input())
    li.append(inp)
no=int(input("Enter Number to delete"))
for i in range(n):
    if(li[i]==no):
        flag=1
        break
if(flag==1):
    li.remove(no)
else:
    print("Element not found")
print(li)
