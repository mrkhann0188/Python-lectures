'''f = open("sample.txt","r")
data = f.readline()
print(data) 

data = f.read()
print(data)
print(type(data))

f = open("sample.txt","w")
data = f.write("Text to overwrite \n the complete data.")

f = open("sample.txt",'a')
data = f.write("\nThis is the append function this is used to override the text in the file ")

f.close()


f = open("sample2.txt",'x')

f = open("sample.txt","r+")
f.write("123")
print(f.read())

f.close()

with open("sample.txt","r") as f:
    data = f.read()
    print(len(data))


f = open("sample3.txt",'x')

# TO DELETE A MODULE WE USE THE OS METHOD 
import os
os.remove("sample3.txt")

search = input("Enter the text to search :")
data = True
line =1
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if(search in data):
            print(f'{search} found at {line}')
            break
        line+=1

'''
#EXCEPTION HANDLING
try:
    x = int(input("Enter x:"))
    ans = 10/x
except ZeroDivisionError:
    print(f'Divide by 0 is not allowed')
else:
    print(f"ans ={ans}")      
 

