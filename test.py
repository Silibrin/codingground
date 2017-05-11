class Node:
	def __init__(self, weight, left, right, name):
		self.weight = weight
		self.left = left
		self.right = right
		self.name = name
	def display(self):
		print("weight = {} left = {} right = {}".format(self.weight, self.left, self.right))
	# def __add__(self, other):

	# 	self.weight += other.weight
	# 	self.right = 
def castomSort(object):
	return object.weight
a = Node(4, 0, 0, 'a')
b = Node(3, 0, 0, 'b')
c = Node(2, 0, 0, 'c')
d = Node(2, 0, 0, 'd')
e = Node(2, 0, 0, 'e')

dirty2 = []
dirty2.append(a)
dirty2.append(b)
dirty2.append(c)
dirty2.append(d)
dirty2.append(e)
dirty2.sort(key = castomSort)
for elements in dirty2:
	print("el = {} weight = {}".format(elements, elements.weight))


dirty = []
dirty.append([])
dirty[0].append(a)
dirty[0].append(b)
dirty[0].append(c)
dirty[0].append(d)
dirty[0].append(e)

# # Кастомная Функция сортировки, создание объекта из двух обеъектов c наименьшим весом, 
# создание нового элемента dirty и его заполнение 

de = Node(d.weight + e.weight, d, e, d.name + e.name)
dirty.append([])
dirty[1].append(dirty[0][0])
dirty[1].append(dirty[0][1])
dirty[1].append(dirty[0][2])
dirty[1].append(de)

# dirty[n].append(adebc)
# Пока dirty[n].amount() != 1

dirty[1][3].display()