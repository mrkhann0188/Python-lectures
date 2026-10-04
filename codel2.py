'''

age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


color = input("Enter your color:")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Be ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color for traffic lights")



age = int(input("Enter your age :"))

if(age <= 13):
    print("Your a child")
elif(age >13 and age< 18 ):
    print("Your a teenager")
elif(age >= 18 ):
    print("Your an adult")



username = input("Enter your username:")
password = input("Enter your password:")

if(username == "admin" and password == "admin123"):
    print("Login successful")
elif(username != "admin"):
    print("Invalid username")
else:
    print("Invalid password")

    
n = int(input("Enter a no :"))
if(n % 5 == 0 ):
    print("The number is a multiple of 5")
else:
    print("Not a multiple of 5")
    


prime = int(input("Enter a no:"))
if(prime % 2 == 0):
    print("The number is prime")
else:
    print("The number is not prime")


user = input("Enter the username:")
pas = input("Enter the password:")

if(user == "admin" and pas =="admin"):
    print("Sucessful login")
else:
    if(user != "admin"):
        print("Invalid username")
    else:
        print("Wrong password")
    
colour = input("Enter the color :")

match colour:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go") 

# INFINITE LOOP 
while True:
    print("This is an infinite loop. Press Ctrl+C to stop.")


#FINITE LOOP 
count = 0
while count <= 5 :
    print("count",count)
    count += 1

# REVERSE A NUMBER 
i = 5
while i >= 1:
    print(i)
    i -= 1

    
no = int(input("Enter a number:"))
i =1
while i<=10 :
    print(no*i)
    i += 1


# for i in range(1, 11):

#     print(no*i)

i =1 
while i<= 10:
    if(i % 6 ==0 ):
        break
    print(i)
    i += 1
print("Loop ended")



i =1
while i<=10:
    if i % 3 ==0:
        i+=1
        continue
       
    print(i)
    i+=1

i = 1
while i<=10:
    print(i)
    i +=2

string = "Hello"
for var in string:
    print(var)
    

for i in range(5):
    print(i+1)
    
word = "Artificial intelligence"
count = 0
for i in word:
    if(i == "i"):
        count +=1
print(count)


word = "artificial"
count =0
for ch in word:
    if(ch =='a'or ch =='e' or ch =='i' or ch =='o' or ch =='u'):
        count += 1
print(count)


for i in range(5):
    print(i)

for i in range(1,5):
    print(i)


for i in range(1,20,3):
    print(i)
    
n = int(input("Enter a number:"))
sum = 0
for i in range(1,n+1):
    sum +=i
print(sum)

def sum(a,b):
    s = a+b
    return s


print(sum(10,20))

def cal_avg(a,b,c):
    avg = (a+b+c)/3
    return avg
a = int(input("Enter a number:"))
b = int(input("Enter b number:"))
c = int(input("Enter c number:"))
print(cal_avg(a,b,c))

sum = lambda a,b: a+b
print(sum(4,5))
'''
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i

    return fact
print(factorial(5))