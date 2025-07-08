class Employee:
    def __init__(self,name,salary,ssn):
        self.name=name#public variable
        self._salary=salary#protected variable
        self.__ssn=ssn#private variable
if __name__ =="__main__":
    emp =Employee("Nimrah",70000,12345)
    print("public variable:",emp.name)
    print("protected variable:",emp._salary)
    print("private variable:",emp.__ssn)

    