'''class Student:
    subject ='python'
    college ='abc'
    year = 4
stu1 = Student()
print(stu1)
print(stu1.college,stu1.subject,stu1.year)

class Student:
    def __init__(self):
        print("THIS IS A DEFAULT TYPE CONSTUCTOR ")
    def __init__(self, name,cgpa): # THIS IS A PARAMETERIZED TYPE CONSTRUCTOR 
        print('the constuctor is called...')
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
stu1 = Student('ayaan',9)
stu2 = Student('rahul',8)
print(stu1.name,stu1.cgpa)
print(stu2.name)
print(stu1.get_cgpa())
print(f'{stu1.name} has cgpa of :{stu1.get_cgpa()}') 

class Student:
    college_name = 'abc college' #CLASS ATTRIBUTES 

    def __init__(self,name,gpa): 
        self.name = name
        self.gpa = gpa
stu1 = Student('rahul',9.2)
print(stu1.name,stu1.gpa)
print(Student.college_name)
print(stu1.college_name)
        '''

class Laptop:
    storage_type = 'ssd'
    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage
    def get_info(self):
        print(f'laptop has {self.RAM} RAM & {self.Storage}{self.storage_type}')
l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb",'256gb')
l1.get_info()