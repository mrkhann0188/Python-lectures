#STRINGS 
'''
word1 = "I love "
word2 = "Python"
# Concatination 
print(word1 + word2)

print(word1[3])

for ch in word1:
    print(ch)
    
str = 'Python is a programming language'
print(str[1:3])
print(str[12:])
print(str[:])
print(str[::2])
print(str[-4:-2])


#DYNAMIC STRINGS
a =5 
b =10 
sum = a+b
#NORMAL FORMATTING 
print("sum of {} and {} is {}".format(a,b,sum))
print("language is {}".format("Python"))
#INDEX BASED FORMATTING 
print("Sum of {1} & {0} is {2}".format(a,b,sum))

#F STRING FORMATTING 
A = 5
B =10 
print(f"Sum of {A} & {B} is {A+B}")

#lists 
marks = [10,20,30,40,50,"abc"]
print(marks)
print(len(marks))
print(type(marks))
print(marks[1:4])

num = [1,2,3]
num.append(4)
print(num)
num.insert(2,10)
print(num)

print(sum(num))
num.sort()
print(num)
num.sort(reverse = True)
print(num)
num.reverse()
print(num)

list = [1,2,3,4,5]
for i in list:
    print(i)
    

num = [1,2,310,4,10]
x = 10
i =0 
for val in num:
    if val == x:
        print(i)
        break
    i+=1

#TUPLESS 
tup  = (1,2,3,4,3,3,3,3,6,8,10)
print(tup[2])
print(tup[2:])
for val in tup:
    print(val)
sum = 0 
for val in tup:
    sum += val
print(f"The sum of vals is {sum}")

print(tup.index(3))
print(tup.count(3))
'''
info ={
    "name":"Ayaan khan",
    "roll no":32,
    "cgpa": 9,
    "subjects":["maths","physics","chemistry"]
}
'''
print(info)
print(type(info))
print(info["name"])
print(info.keys())
dict_keys = list(info.keys())
print(dict_keys)
dict_val = list(info.values())
print(dict_val)
print(info.items())

print(info[3])
print(info.get("name"))

print(info.get(32))
print(info["cgpa"])

info.update({
    'city':'hyderabad',
    'class':'be'
})
print(info)

s ={1,2,3,4,4}
print(s)
print(type(s))
s.add(5)
s.remove(2)
# s.clear()
s.pop()
print(s)

s1 ={1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
'''
info = {
    ("ayaan",'maths'),
    ('bob','science'),
    ('ayaan','science'),
    ('charlie','maths'),
    ('bob','maths'),
    ('ayaan','english'),
    ('charlie','english'),
}
unique_courses = set()
'''
for tup in info:
    print(tup)
    print(tup[0])
    print(tup[1])
    unique_courses.add(tup[1])

print(unique_courses) 

for name,courses in info:
    if(courses == 'english'):
        print(name)
        '''
dict ={ }

for name,courses in info :
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(courses)
    else:
        dict[name].add(courses)
print(dict)