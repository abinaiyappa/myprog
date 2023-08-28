class Person:
    #def _init_(self):
	def Hello(self,name=None,age=None):
		self.name=name
		self.age=age
		if name != None and age != None:
			print("Hello:",name)
			print("Your Age:",age)
		elif name != None:
			print("Hello:",name)
		else:
			print("Hello")
p = Person()
a=input("enter name")
p.Hello(a)
print("0 parameter passing")
a=input("enter name")
p.Hello(a)
print("1 parameter passing")
a=input("enter name")
b=int(input("enter age"))
p.Hello(a,b)
print("2 parameter passing")
