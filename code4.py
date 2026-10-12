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


class Laptop:
    storage_type = 'ssd'
    def __init__(self,RAM,Storage):
        self.RAM = RAM
        self.Storage = Storage
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
    
    def get_info(self): #INSTANCE METHORD 
        print(f'laptop has {self.RAM} RAM & {self.Storage}{self.storage_type}')

    @staticmethod
    def calc_discount(price,discount):
        final_price = price-(price*discount/100)
        print(f"final price = {final_price}")

l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb",'256gb')
l1.get_info()
Laptop.get_storage_type()
l1.calc_discount(40_000,20)


class Product:
    count =0 
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count +=1


    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_products(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def cal_disc(price,discount):
        finl = price -(price*discount/100)
        print(f"The old price  of the product is {price} and the new discounted price is : {finl} ")



p1 = Product("phone",20_000)
p2 = Product("Laptop",50_000)
p3 = Product("mac book",20_000)
p4 = Product("phone",20_000)

p1.get_info()
p2.get_info()
p3.get_info()
p4.get_info()

Product.get_products()
p1.cal_disc(20_000,10)


# OOPS
##### ENCAPSULATION 
class BankAccount:
    def __init__(self,name,balalnce,cvv):
        self.name = name  # PUBLIC
        self._balance = balalnce #PROTECTED 
        self.__cvv = cvv # PRIVATE


    def get_cvv(self): #GETTER 
        return self.__cvv
    
    def  set_cvv(self,newcvv):#SETTER 
        self.__cvv =newcvv



acc1 = BankAccount("Rahul ",100_000, 123)
acc1.set_cvv(200)
print(acc1.name,acc1._balance,acc1.get_cvv())

# ANOTHER METHOD TO GET ACCESS OF THIS PRIVATE VALUE

print(acc1._BankAccount__cvv)


# INHERITANCE 
 
class Employee:
    start_time = '10pm'
    end_time = '6pm'

    def change_time(self,new_end_time):
        self.end_time = new_end_time

class Teacher(Employee) :
    def __init__(self,subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
        
t1 = Teacher("Math")
staff1 = AdminStaff("Manager")

print(staff1.role,staff1.start_time,staff1.end_time)


print(t1.start_time,t1.end_time,t1.subject)



#MULTI LEVEL INHERITANCE
class College:
    open_time = "9am"
    close_time ="4pm"

class Admin(College):
    def __init__(self,role):
        self.role = role
class Accounts(Admin):
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary = salary

acc1 =Accounts(25_000,'CA')
print(acc1.salary,acc1.role,acc1.open_time,acc1.close_time)
  

#MULTIPLE INHERITANCE
class Teacher:
    def __init__(self,salary):
            self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa
class TA(Teacher,Student):
     def __init__(self, salary,gpa,name):
          super().__init__(salary)
          Student.__init__(self,gpa)
        
          self.name = name
          
ta1 =TA(25_000,9,'Ayaan')
print(ta1.salary,ta1.gpa,ta1.name)

'''
