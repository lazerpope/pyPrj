from tkinter import *
from tkinter import messagebox as mb
import random
import math
import time
import threading
import datetime

arr = []
counter = 0

entryLength = 0
entryMaxValue = 0
entryDelay = 0

arrLength = 50
arrMaxValue = 500
autoSortDelay = 0.02
lineWidth = math.floor(1160 / arrLength)

pointerOne = 0
pointerTwo = 0

compares = 0
moves = 0

ii = 0
jj = 0

isSortContinues = bool(True)
lowestValueIndex = 0
itemToInsert = 0
itemToCompare = 0

myTimer = datetime.datetime.now()


def help(self):
    mb.showinfo(
        "Подсказки",
        "Пузырек авто - A             Пузырек вручную - Q\nВключение авто - S           Включение вручную - W\nВыбора авто - D            Выбора вручную - E\n\nОстановить\Продолжить - F      Новый массив - R         Ввод новых значений - L"
    )
    pass


def resetArr(self):
    global ii, jj, isSortContinues, compares, moves, pointerOne, pointerTwo, myTimer, itemToInsert, itemToCompare
    arrFillWithRandom()

    compares = 0
    moves = 0

    ii = 0
    jj = 0

    pointerOne = 0
    pointerTwo = 0

    isSortContinues = bool(False)

    myTimer = datetime.datetime.now()

    lowestValueIndex = 0

    itemToInsert = 0
    itemToCompare = 0

    drawArr()
    pass


def stopSort(self):
    global isSortContinues
    if isSortContinues:
        isSortContinues = bool(False)
    else:
        isSortContinues = bool(True)
        bubbleAutoSort(1)
    pass


def arrFillWithRandom():
    global arr
    arr = [random.randint(0, arrMaxValue) for i in range(arrLength)]
    pass


def inp(self):
    global arrLength, arrMaxValue, entryLength, entryMaxValue, autoSortDelay, entryDelay

    settings = Tk()

    settings.title("SortSettings")
    settings.configure(background='green')

    labelLength = Label(settings, text="Введите размер: ")
    labelMaxValue = Label(settings, text="Введите макс. значение: ")
    labelDelay = Label(settings, text="Введите макс. значение: ")
    labelLength.grid(row=1, column=0, sticky="w")
    labelMaxValue.grid(row=2, column=0, sticky="w")
    labelDelay.grid(row=3, column=0, sticky="w")

    entryLength = Entry(settings, width=24, textvariable=arrLength)
    entryLength.insert(0, str(arrLength))
    entryLength.grid(row=1, column=1, sticky="w")

    entryMaxValue = Entry(settings, width=24, textvariable=arrMaxValue)
    entryMaxValue.insert(0, str(arrMaxValue))
    entryMaxValue.grid(row=2, column=1, sticky="w")

    entryDelay = Entry(settings, width=24, textvariable=autoSortDelay)
    entryDelay.insert(0, str(autoSortDelay))
    entryDelay.grid(row=3, column=1, sticky="w")

    buttonPress = Button(settings,
                         text="Ввод",
                         width=20,
                         command=lambda: setInp())
    buttonPress.grid(row=4, column=1, sticky="w")

    settings.resizable(0, 0)
    settings.geometry("360x240")
    settings.mainloop()
    pass


def setInp():
    global arrLength, arrMaxValue, entryMaxValue, entryMaxValue,entryDelay,autoSortDelay
    if int(entryLength.get()) <= 410:
        arrLength = int(entryLength.get())
    if int(entryMaxValue.get()) <= 500:
        arrMaxValue = int(entryMaxValue.get())

    autoSortDelay = float(entryDelay.get())

    arrFillWithRandom()
    resetArr(1)
    drawArr()
    pass


#Сортировка  пузырьком
def bubbleManualSort(self):
    bubbleIncrementer(1)
    pass


def bubbleAutoSort(self):
    global isSortContinues, myTimer
    myTimer = datetime.datetime.now()
    isSortContinues = bool(True)

    def target():
        while isSortContinues:
            bubbleIncrementer(1)
            time.sleep(autoSortDelay)

    t = threading.Thread(target=target, daemon=True)
    t.start()
    pass


def bubbleIncrementer(self):
    global ii, jj, isSortContinues

    if ii == arrLength - 2:
        isSortContinues = bool(False)
    elif jj == arrLength - ii - 2:
        ii += 1
        jj = 0
    elif jj < arrLength - 1:
        jj += 1

    bubbleSort()
    pass


def bubbleSort():
    global arr, lineWidth, pointerOne, pointerTwo, ii, jj, compares, moves
    i = ii
    j = jj

    pointerOne = j
    pointerTwo = j + 1
    drawArr()
    compares += 1
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        moves += 1
    #print(i, " ", j)
    pass


#Сортировка выбором
def selectionManualSort(self):
    selectionIncrementer(1)
    pass


def selectionAutoSort(self):
    global isSortContinues, myTimer
    myTimer = datetime.datetime.now()
    isSortContinues = bool(True)

    def target():
        while isSortContinues:
            selectionIncrementer(1)
            time.sleep(autoSortDelay)

    t = threading.Thread(target=target, daemon=True)
    t.start()
    pass


def selectionIncrementer(self):
    global ii, jj, isSortContinues, lowestValueIndex

    if ii == arrLength - 2:
        isSortContinues = bool(False)
        selectionIncrementer(1)
    elif jj == arrLength - 1:
        ii += 1
        jj = ii + 1
        lowestValueIndex = ii
    elif jj < arrLength - 1:
        jj += 1
    #print(ii, " ", jj)
    sortSelection()
    pass


def sortSelection():
    global arr, lineWidth, pointerOne, pointerTwo, ii, jj, compares, moves, lowestValueIndex
    i = ii
    j = jj

    pointerOne = j
    pointerTwo = lowestValueIndex

    compares += 1
    if arr[j] < arr[lowestValueIndex]:
        lowestValueIndex = j

    if j == len(arr) - 1:
        arr[i], arr[lowestValueIndex] = arr[lowestValueIndex], arr[i]
        moves += 1

    drawArr()
    pass


#Сортировка включением
def insertionManualSort(self):
    insertionIncrementer(1)
    pass


def insertionAutoSort(self):
    global isSortContinues, myTimer
    myTimer = datetime.datetime.now()
    isSortContinues = bool(True)

    def target():
        while isSortContinues:
            insertionIncrementer(1)
            time.sleep(autoSortDelay)

    t = threading.Thread(target=target, daemon=True)
    t.start()
    pass


def insertionIncrementer(self):
    global ii, jj, isSortContinues, itemToCompare, itemToInsert, moves, compares, arr, pointerOne, pointerTwo

    if ii == arrLength - 1:
        isSortContinues = bool(False)
    else:
        ii += 1
        item_to_insert = arr[ii]

        jj = ii - 1

        pointerOne = ii
        pointerTwo = jj

        while jj >= 0 and arr[jj] > item_to_insert:
            pointerTwo = jj
            compares += 2
            moves += 1
            arr[jj + 1] = arr[jj]
            jj -= 1
            drawArr()

        moves += 1
        arr[jj + 1] = item_to_insert


    drawArr()
    pass


def sortInsertion():
    global arr, lineWidth, pointerOne, pointerTwo, ii, jj, compares, moves, lowestValueIndex
    i = ii
    j = jj

    pointerOne = j
    pointerTwo = lowestValueIndex

    compares += 1
    if arr[j] < arr[lowestValueIndex]:
        lowestValueIndex = j

    if j == len(arr) - 1:
        arr[i], arr[lowestValueIndex] = arr[lowestValueIndex], arr[i]
        moves += 1

    drawArr()
    pass


#отрисовка
def drawArr():
    global canvas

    canvasNew = Canvas()

    i = 0
    global arr, lineWidth, pointerOne, pointerTwo, compares, moves, lineWidth, myTimer

    lineWidth = math.floor(1160 / arrLength)

    canvasNew.configure(background='black')

    while i < arr.__len__():
        canvasNew.create_line(i * lineWidth + 20 + i,
                              700,
                              i * lineWidth + 20 + i,
                              700 - arr[i],
                              width=lineWidth,
                              fill="white")
        i += 1

    canvasNew.create_line(pointerOne * lineWidth + 20 + pointerOne,
                          700,
                          pointerOne * lineWidth + 20 + pointerOne,
                          700 - arr[pointerOne],
                          width=lineWidth,
                          fill='red')

    canvasNew.create_line(pointerTwo * lineWidth + 20 + pointerTwo,
                          700,
                          pointerTwo * lineWidth + 20 + pointerTwo,
                          700 - arr[pointerTwo],
                          width=lineWidth,
                          fill='green')

    canvasNew.create_line(0,
                          700 - arrMaxValue,
                          1280,
                          700 - arrMaxValue,
                          width=1,
                          fill='grey')

    stringToDraw = "Maximum value: " + str(arrMaxValue)
    canvasNew.create_text(60,
                          690 - arrMaxValue,
                          text=stringToDraw,
                          fill='white')

    delta = datetime.datetime.now() - myTimer
    stringToDraw = "Time: " + str(delta) + " microseconds"
    canvasNew.create_text(560,
                          690 - arrMaxValue,
                          text=stringToDraw,
                          fill='white')

    canvasNew.create_line(0,
                          40,
                          math.floor(
                              (compares * 1200) / (arrLength * arrLength)),
                          40,
                          width=20,
                          fill='green')

    stringToDraw = "Compares: " + str(compares)
    canvasNew.create_text(50 + math.floor(
        (compares * 1200) / (arrLength * arrLength)),
                          40,
                          text=stringToDraw,
                          fill='white')

    canvasNew.create_line(0,
                          80,
                          math.floor((moves * 1200) / (arrLength * arrLength)),
                          80,
                          width=20,
                          fill='green')

    stringToDraw = "Moves: " + str(moves)
    canvasNew.create_text(40 + math.floor(
        (moves * 1200) / (arrLength * arrLength)),
                          80,
                          text=stringToDraw,
                          fill='white')

    stringToDraw = str(arrLength)
    canvasNew.create_text(((1 + lineWidth) * arrLength) + 10,
                          710,
                          text=stringToDraw,
                          fill='white')

    stringToDraw = str(arrLength // 2)
    canvasNew.create_text(((1 + lineWidth) * arrLength / 2) + 10,
                          710,
                          text=stringToDraw,
                          fill='white')

    stringToDraw = '0'
    canvasNew.create_text(10, 710, text=stringToDraw, fill='white')

    canvas.destroy()
    canvasNew.pack(fill=BOTH, expand=1)
    canvas = canvasNew

    pass


root = Tk()

root.title("SortByKalinin")
root.configure(background='black')

canvas = Canvas()
canvas.pack(fill=BOTH, expand=1)

root.resizable(0, 0)
root.geometry("1280x720")

arrFillWithRandom()
drawArr()

root.bind("q", bubbleManualSort)
root.bind("a", bubbleAutoSort)

root.bind("w", selectionManualSort)
root.bind("s", selectionAutoSort)

root.bind("e", insertionManualSort)
root.bind("d", insertionAutoSort)

root.bind("1", insertionIncrementer)

root.bind("l", inp)
root.bind("r", resetArr)
root.bind("f", stopSort)
root.bind("h", help)
root.mainloop()
