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

fileIn = open("fileInLz.txt", "r")
fileOut = open("fileOutLz.txt", "w")
lz = LZEncoder(fileIn, fileOut)
lz.encode()
lz.decode()
fileIn.close()
fileOut.close()
