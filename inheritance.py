class student:
	def __init__(self):
		self.name=input("enter the name")
		self.age=int(input("enter the age"))
		self.id=int(input("enter the id"))
	def display1(self):
		print("name :",self.name,"\nage :",self.age,"\nid :",self.id)
class ug(student):
	def __init__(self):
		super().__init__()
		self.ugcoure=input("enter the ug course")
		self.ugfees=int(input("enter the fees"))
	def display(self):
		print("ug cource :",self.ugcoure,"\nug fees :",self.ugfees)

class pg(student):
	def __init__(self):
		super().__init__()
		self.pgcoure=input("enter the pg course")
		self.pgfees=int(input("enter the pg  fees"))
	def display(self):
		print("pg cource :",self.pgcoure,"\npg fees :",self.pgfees)
while True:
	print("1.ug\n2. pg")
	ch=int(input("enter the choice"))
	if ch==1:
		u=ug()
		u.display1()
		u.display()
	elif ch==2:
		p=pg()
		p.display1()
		p.display()
	else:
		break

