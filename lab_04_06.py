import math
class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits #количество информационных разрядов
        self.controlBits = int(math.log(dataBits, 2)) + 1 #количество контрольных разрядов

    def encode(self, str):
        k = 1
        n_str = list()
        l = 0
        for i in range (1, len(str) + self.controlBits + 1): #дописываем нули на места контрольных разрядов
            if i == k:
                k *= 2
                n_str.append('0')
            else:
                n_str.append(str[l])
                l += 1
        g = 0
        #print(n_str)
        z = 1
        for i in range (1, len(n_str) + 1):
            if i == z:
                for j in range (i - 1, len(n_str), i + i):
                    for k in range (0, i):
                        if j + k >= len(n_str):
                            break
                        g = g + int(n_str[j + k])
                #print(g)
                if g % 2 != 0:
                    n_str[i - 1] = '1'
                g = 0
                z *= 2
        return n_str

    def decode(self, str):
        z = 1
        mis = 0
        g = 0
        for i in range (1, len(str) + 1):
            if i == z:
                for j in range (i - 1, len(str), i + i):
                    for k in range (0, i):
                        if j + k >= len(str):
                            break
                        g = g + int(str[j + k])
                #print(g)
                if str[i - 1] == '1':
                    g -= 1
                if (str[i - 1] == '1' and g % 2 != 1) or (str[i - 1] == '0' and g % 2 != 0):
                    mis += i
                g = 0
                z *= 2
        return mis


Ham = HammingEncoder(4)
print(Ham.encode("0101"))
print("Ошибка в %d бите"%Ham.decode("0000101"))

