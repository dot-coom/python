from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def calc_salary(self):
        pass

    @abstractmethod
    def display(self):
        pass

class FullTimeEmp(Employee):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary

    def mnthly_salary(self):
        return self.salary
    
    def display_fulltime(self):
        return super().display_()


    


   
