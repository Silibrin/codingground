import time
class Ticket:
	def __init__(self, date, name,deadline):
		self.createDate = date
		self.owner = name
		self.deadline = deadline
	def __del__(self):
		print("Delete ticket: ", time.asctime(self.createDate))
	def display(self):
		print("Ticket:")
		print(" createDate: ",time.asctime(self.createDate))
		print(" owner: ",self.owner)
		print(" deadline: ",time.asctime(self.deadline))
ticket1 = Ticket(time.localtime(),"Ivan Ivanov", time.strptime("17.12.2017", "%d.%m.%Y"))
ticket1.display()
print("Owner: ", ticket1.owner)
print("Owner(getattr): ", getattr(ticket1,"owner"))
print("hasattr: ", hasattr(ticket1,"owner"))
setattr(ticket1,"owner","Alexei Petrov")
print("Owner(setattr): ", ticket1.owner)
delattr(ticket1,"owner")
setattr(ticket1, "owner", "Pavel Pavlovich")
print("delattr: ", ticket1.owner)
currentTime = time.localtime()
print("Current time : ", time.asctime(currentTime))
stroka = "17.07.2017 10:53:00"
anotherTime = time.strptime(stroka, "%d.%m.%Y %H:%M:%S")
print("anotherTime : ", time.asctime(anotherTime))
# del ticket1
# print(ticket1)