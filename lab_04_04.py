class Encode:
	def __init__(self):
		print("hello")
	def encode():
		print("i encode")
	def decode():
		print("i decode")
	def setCompressionCoef():
		print("i set comp")
	def getCompressionCoef():
		print("i get comp")

class LZEncoder(Encode):
	def __init__(self, fileIn, fileOut):
		self.fileIn = fileIn
		self.fileOut = fileOut
	def encode(self):
		def symbolsCounter(file):
			s = 0
			for line in file:
				for symbol in line:
					s+=1
			file.close()
			return s
		table = []
		findval = 0
		prevval = 0
		table.append("");
		buff = ""
		count = symbolsCounter(self.fileIn)
		k = 0
		fileIn = open("fileInLz.txt", "r")
		for line in fileIn:
			for symbol in line:
				k+=1
				prevval = findval
				isHere = False
				buff+=symbol
				print("buff = ", buff)
				for i in range(0, len(table)):
					if(buff == table[i]):
						findval = i;
						isHere = True
						break;
				if(isHere == True and k == count):
					self.fileOut.write(str(prevval))
					self.fileOut.write(symbol)
				if(not isHere):
					table.append(buff)
					self.fileOut.write(str(prevval))
					self.fileOut.write(symbol)
					prevval = 0
					findval = 0
					buff=""
		print(table)
		fileOut.close()
	def decode(self):
		def symbolsCounter(file):
			s = 0
			for line in file:
				for symbol in line:
					s+=1
			file.close()
			return s
		table = []
		table.append("")
		fileIn = open("fileOutLz.txt", "r")
		count = symbolsCounter(fileIn)
		fileIn = open("fileOutLz.txt", "r")
		fileOut = open("fileOutLz2.txt", "w")
		i = 0
		while(i < count/2 - 2):
			buff = table[0]
			num = fileIn.read(1)
			it = fileIn.read(1)
			while(it.isdigit() == True):
				num = int(num)*10 + int(it)
				it = fileIn.read(1)
			if(it == ""):
				break
			buff = table[int(num)] + str(it) 
			table.append(buff)
			fileOut.write(buff)
			i+=1
		fileIn.close()
		self.setCompressionCoef()
	def setCompressionCoef(self):
		fileIn = open("fileInLz.txt", "r")
		fileOut = open("fileOutLz.txt", "r")
		count = 0
		count2 = 0
		for line in fileIn:
			for symbol in line:
				count+=1
		for line in fileOut:
			for symbol in line:
				count2+=1
		self.compression = count / count2
		fileIn.close()
		fileOut.close()
	def getCompressionCoef(self):
		print("LZCoef = ", self.compression)

fileIn = open("fileInLz.txt", "r")
fileOut = open("fileOutLz.txt", "w")
lz = LZEncoder(fileIn, fileOut)
lz.encode()
lz.decode()
lz.getCompressionCoef()

class Node:
	def __init__(self, weight, left, right, name):
		self.weight = weight
		self.left = left
		self.right = right
		self.name = name
	def display(self):
		print("weight = {} left = {} right = {}".format(self.weight, self.left, self.right))
# Кастомный сорт object
def castomSort(object):
	return object.weight

class HuffmanEncoder(Encode):
	def __init__(self, fileIn, fileOut):
		self.fileIn = fileIn
		self.fileOut = fileOut
	def encode(self):
		symDict = []
		symDict.append([])
		#Проход по строкам файла
		for line in fileIn:
			#Проход по символам в строке
			for symbol in line:
				existense = False
				#Проход по ключам в словаре и сравнение с текущим символом в строке
				for key in symDict[0]:
					if symbol == key.name:
						existense = True
						key.weight+=1
				#нет совпадений - добавляем новую пару ключ - значение в словарь
				if not existense:
					symDict[0].append(Node(1, 0, 0, symbol))
					existense = False
		i = 0
		symDictCopy = []
		while(len(symDict[i]) != 1):
			symDict[i].sort(key = castomSort)
			i+=1
			symDict.append([])
			# создаем новый элемент содержащий объекты
			symDict[i].append(Node(symDict[i-1][0].weight + symDict[i-1][1].weight, symDict[i - 1][1].name, symDict[i - 1][0].name, symDict[i-1][0].name + symDict[i-1][1].name))
			symDictCopy.append(Node(symDict[i-1][0].weight + symDict[i-1][1].weight, symDict[i - 1][1].name, symDict[i - 1][0].name, symDict[i-1][0].name + symDict[i-1][1].name))
			j = 0
			for elements in symDict[i - 1]:
				if(j < 2):
					j+=1
					continue
				else:
					symDict[i].append(elements)
		rootLength = len(symDict[i][0].name)
		levelAmount = len(symDict)
		# создаем словарь ключ значение символ - его код
		tableHaf = {}
		for key in symDict[0]:
			tableHaf[key.name] = ""
		i = 0
		for key in tableHaf:
			# поиск символа начиная с узлов первого уровня
			while(i != levelAmount - 1):
				if(symDictCopy[i].name.find(key) == -1):
					i+=1
					continue
				if(symDictCopy[i].left.find(key) != -1):
					print("----------")
					print("symbol = {} name = {} left = {} right = {}".format(key, symDictCopy[j].name, symDictCopy[j].left, symDictCopy[j].right))
					tableHaf[key]+='0'
				else:
					tableHaf[key]+='1'
				i+=1
			i = 0
		for key in tableHaf:
			tableHaf[key] = tableHaf[key][::-1]
		newFileIn = open("fileIn.txt", "r")
		newFileOut = open("fileOut.txt", "w")
		for line in newFileIn:
			for symbol in line:
				newFileOut.write(tableHaf[symbol])
		print(tableHaf)
	def decode(self):
		fileIn = open("fileIn.txt", "r")
		fileOut = open("fileOut.txt", "w")
		symDict = []
		symDict.append([])
		#Проход по строкам файла
		for line in fileIn:
			#Проход по символам в строке
			for symbol in line:
				existense = False
				#Проход по ключам в словаре и сравнение с текущим символом в строке
				for key in symDict[0]:
					if symbol == key.name:
						existense = True
						key.weight+=1
				#нет совпадений - добавляем новую пару ключ - значение в словарь
				if not existense:
					symDict[0].append(Node(1, 0, 0, symbol))
					existense = False
		i = 0
		symDictCopy = []
		while(len(symDict[i]) != 1):
			symDict[i].sort(key = castomSort)
			i+=1
			symDict.append([])
			# создаем новый элемент содержащий объекты
			symDict[i].append(Node(symDict[i-1][0].weight + symDict[i-1][1].weight, symDict[i - 1][1].name, symDict[i - 1][0].name, symDict[i-1][0].name + symDict[i-1][1].name))
			symDictCopy.append(Node(symDict[i-1][0].weight + symDict[i-1][1].weight, symDict[i - 1][1].name, symDict[i - 1][0].name, symDict[i-1][0].name + symDict[i-1][1].name))
			j = 0
			for elements in symDict[i - 1]:
				if(j < 2):
					j+=1
					continue
				else:
					symDict[i].append(elements)
		rootLength = len(symDict[i][0].name)
		levelAmount = len(symDict)
		# создаем словарь ключ значение символ - его код
		tableHaf = {}
		for key in symDict[0]:
			tableHaf[key.name] = ""
		i = 0
		for key in tableHaf:
			# поиск символа начиная с узлa первого уровня
			while(i != levelAmount - 1):
				if(symDictCopy[i].name.find(key) == -1):
					i+=1
					continue
				if(symDictCopy[i].left.find(key) != -1):
					# print("----------")
					# print("symbol = {} name = {} left = {} right = {}".format(key, symDictCopy[j].name, symDictCopy[j].left, symDictCopy[j].right))
					tableHaf[key]+='0'
				else:
					tableHaf[key]+='1'
				i+=1
			i = 0
		# реверт значений словаря

		
		for key in tableHaf:
			tableHaf[key] = tableHaf[key][::-1]
		fileIn.close()
		fileOut.close()
		newFileOut = open("fileOut.txt", "r")
		newFileOut2 = open("fileOut2.txt", "w")
		searchFor = symDict[levelAmount - 1][0].name
		print("ss = ", searchFor)
		for line in newFileOut:
			k = 0
			while( k < len(line)):
				isFounded = False
				while(not isFounded):
					i = levelAmount - 1
					while(i >= 0):
						for j in range(0, len(symDict[i])):
							if(symDict[i][j].name != searchFor):
								continue
							if(len(symDict[i][j].name) == 1):
								print(symDict[i][j].name)
								newFileOut2.write(symDict[i][j].name)
								isFounded = True
								i = levelAmount - 1
								j = 0
							if(k == len(line)):
								k+=1
								isFounded = True
								break
							if(line[k] == '0'):
								searchFor = symDict[i][j].left
							elif(line[k] == '1'):
								searchFor = symDict[i][j].right
							else:
								print("k")
							k+=1
							if(isFounded):
								break
						if(isFounded):
							break
						i-=1
	def setCompressionCoef(self):
		fileIn = open("fileIn.txt", "r")
		fileOut = open("fileOut.txt", "r")
		count = 0
		count2 = 0
		for line in fileIn:
			for symbol in line:
				count+=1
		for line in fileOut:
			for symbol in line:
				count2+=1
		self.compression = count * 8 / count2
		fileIn.close()
		fileOut.close()
	def getCompressionCoef(self):
		print("LZCoef = ", self.compression)

fileIn = open("fileIn.txt", "r")
fileOut = open("fileOut.txt", "w")
huff = HuffmanEncoder(fileIn, fileOut)
huff.encode()
huff.decode()