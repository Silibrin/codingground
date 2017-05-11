class Person:
	count = 1
	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age
	def display(self):
		print("Firstname = {0}, Lastname = {1}, Age = {2}".format(self.firstname, self.lastname, self.age))	
class Student(Person):
	def __init__(self, firstname, lastname, age, recordBook):
		Person.__init__(self, firstname, lastname, age)
		self.studentId = Person.count
		Person.count+=1
		self.recordBook = recordBook
	def display(self):
		Person.display(self)
		print("ID = {0}, Marks = {1}".format(self.studentId, self.recordBook))
dict1 = {'5' : 5, '4' : 7, '3' : 101, '2' : 0}
dict2 = {'5' : 2, '4' : 9, '3' : 1, '2' : 0}
dict3 = {'5' : 55, '4' : 7, '3' : 0, '2' : 0}
st1 = Student("Alexei", "Ivanov", "17", dict1)
st2 = Student("Venya", "Boss", "18", dict2)
st3 = Student("Misha", "Mishanov", "19", dict3)
st1.display()
st2.display()
st3.display()