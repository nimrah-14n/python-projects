class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):#inheriting person
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject

    def display(self):
        print(f"name:{self.name} , Subject:{self.subject}")

if __name__=="__main__":
    teacher=Teacher("Miss Nimrah","maths")
    teacher.display()