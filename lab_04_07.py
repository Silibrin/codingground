class Row:
    count=0
    def __init__(self, collection, value):
        Row.count+=1
        self.id = Row.count
        self.collection = collection
        self.value = value
class Table(Row):
    def __init__(self, rowsNum):
        self.rowsNum = rowsNum
        self.rows = []
    def addRow(self,row):
        flag = True
        for elem in self.rows:
            if elem == row:
                print("Error: This row already exists!")
                flag = False
        if flag:
            self.rows.append(row)

    def setRow(self, row):
        flag = True
        for i in self.rows:
            if i == row:
                flag = False
        if flag:
            print("Error: this row does not exist!")

    def getRow(self, rowID):
        if rowID < len(self.rows):
            return self.rows[rowID]
        else:
            print("Error: index list out of range!")

    def display(self):
        # вывод шапки
        print("id", end='  ')
        for i in range(0, int(len(self.rows[0].collection))):
            print("x%d  " % (i + 1), end='')
        print("| f(", end='')
        for i in range(0, int(len(self.rows[0].collection))):
            print("x%d" % (i + 1), end='')
        print(")")
        # вывод таблицы

        for i in range(0, self.rowsNum):
            print(self.rows[i].id, end='   ')
            for j in range (0, int(len(self.rows[0].collection))):
                print(self.rows[i].collection[j], end = '   ')
            print("|", end='  ')
            print(self.rows[i].value)


class LogicFunction(Table):
    def __init__(self, table):
        self.variableNum = len(table.rows)
        self.table = table
    def getExpression(self):
        new_table = list()
        for i in self.table.rows:#убираем строки в которых ф-ция равна 0
           if i.value == 1:
                new_table.append(i.collection)
        #print(new_table)
        z = 0
        index = 0
        t = ''
        star_table = list()
        def findDif(list):#узнаем, есть ли в списке элементы, отличающиеся только на один символ
            z = 0
            h = 0
            for i in range(0, len(list)):
                for j in range(i + 1, len(list)):
                    for k in range(0, len(list[0])):
                        if list[i][k] != list[j][k]:
                            z += 1
                    if z == 1:
                        return True
                    z = 0
            return  False

        while (findDif(new_table)):
            star_table = list()
            for i in range(0, len(new_table)):  # сравнение элементов, если одно различие, то выписывю эту строку, различие заменяю на звездочку
                for j in range(i + 1, len(new_table)):
                    for k in range(0, len(new_table[0])):
                        if new_table[i][k] != new_table[j][k]:
                            z += 1  # считаем количество различий
                            index = k  # индекс позиции с различием
                    if z == 1:  # если различие одно, то заменяем элемент с индексо index на звездочку
                        # print(new_table[i], new_table[j], index)
                        for c in range(0, len(new_table[i])):
                            if c == index:
                                t = t + "*"
                            else:
                                t = t + str(new_table[i][c])
                        star_table.append(t)
                        t = ''
                    z = 0
                    index = 0
            ##print(star_table)
            new_table = list(set(star_table))


        func = ""
        #print(new_table)
        for i in range (0, len(new_table)):
            for j in range (0, len(new_table[0])):
                #print(star_table1[i][j])
                if new_table[i][j] != "*":
                    if new_table[i][j] == '1':
                        func = func + "x" + str(j + 1)
                    else:
                        func = func + "x" + str(j + 1) + "'"
            if i != len(new_table) - 1:
                func += "+"
        return func


table = Table(8)
table.addRow(Row([0, 0, 0], 1))
table.addRow(Row([0, 0, 1], 1))
table.addRow(Row([0, 1, 0], 0))
table.addRow(Row([0, 1, 1], 0))
table.addRow(Row([1, 0, 0], 1))
table.addRow(Row([1, 0, 1], 1))
table.addRow(Row([1, 1, 0], 0))
table.addRow(Row([1, 1, 1], 0))


table.display()

func = LogicFunction(table)
print("Исходная формула: x1'x2'x3' + х1'x2'x3 + x1x2'x3' + x1x2'x3")
print("Сокращенная формула: ", func.getExpression())


