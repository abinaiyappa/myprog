class Employee:
    def _init_(self):
        self.first = input("")
        self.last = input("")
        self.empid = input("")
        self.pay = int(input("pay"))
    def display(self):
        print("Name:",self.first,self.last)
        print("Empid:",self.empid)
        print("Salary:",self.pay)
class Developer(Employee):
    def apply_raise(self):
        self.raise_pay = 1.14
        self.a=self.pay * self.raise_pay
        print("Developer's hike in income:",self.a)
class Manager(Employee):
    def apply_raise(self):
        self.raise_pay = 1.25
        self.b=self.pay * self.raise_pay
        print("Manager's hike in income:"self.b)
d = Developer()
m = Manager()
print("Developer details---")
d.apply_raise()
print("Manager details---")
m.apply_raise()