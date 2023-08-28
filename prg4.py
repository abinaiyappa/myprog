class open:
	def __init__(self):
		self.l1=[]
	def accept(self):
		n=int(input("enter the number of list elements"))
		for i in range (0,n):
			m=int(input("enter the list element"))
			self.l1.append(m)
		print("list elements are",self.l1)
	def __add__(self,other):
		newlist=[]
		for i in range(0,len(self.l1)):
			newlist.append(self.l1[i]+other.l1[i])
		print("addition of two",newlist)

	def __sub__(self,other):
		newlist=[]
		for i in range(0,len(self.l1)):
			newlist.append(self.l1[i]-other.l1[i])
		print("subtraction of two",newlist)


	def __or__(self,other):
		newlist=[]
		for i in range(0,len(self.l1)):
			newlist.append(self.l1[i] or other.l1[i])
		print("subtraction of two",newlist)

