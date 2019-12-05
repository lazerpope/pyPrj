from tkinter import *
from tkinter import messagebox as mb
import random
import math
import time
import threading

arr = []
counter = 0

arrLength = 50
arrMaxValue = 500
autoSortDelay = 0.0001
lineWidth = math.floor(1160 / arrLength)

pointerOne = 0
pointerTwo = 1

compares = 0
moves = 0

ii = 0
jj = 0


isSortContinues = bool(True)

def help(self):
    mb.showinfo(
        "Подсказки",
        "Пузырек авто - 1             Пузырек вручную - Q\nВключение авто - 2           Включение вручную - W\nВыбора авто - 3            Выбора вручную - E\n\nОстановить\Продолжить - S      Новый массив - R"
    )
    pass


def resetArr(self):
    global ii, jj, isSortContinues, compares, moves
    arrFillWithRandom()

    compares = 0
    moves = 0

    ii = 0
    jj = 0

    isSortContinues = bool(False)
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


def bubbleManualSort(self):
    bubbleIncrementer(1)
    pass


def bubbleAutoSort(self):
    global isSortContinues
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

    sortBubble()
    pass


def arrFillWithRandom():
    global arr
    arr = [random.randint(0, arrMaxValue) for i in range(arrLength)]
    pass


def drawArr():
    global canvas

    canvasNew = Canvas()

    i = 0
    global arr, lineWidth, pointerOne, pointerTwo, compares, moves

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
                          fill='red')

    canvasNew.create_line(0,
                          700 - arrMaxValue,
                          1280,
                          700 - arrMaxValue,
                          width=1,
                          fill='grey')

    stringToDraw = "Maximum value: " + str(arrMaxValue)
    canvasNew.create_text(60, 690 - arrMaxValue, text=stringToDraw, fill='white')

    canvasNew.create_line(0,
                          40,
                          math.floor((compares*1200) / (arrLength*arrLength)),
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

    canvas.destroy()
    canvasNew.pack(fill=BOTH, expand=1)
    canvas = canvasNew

    pass


def sortBubble():
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
root.bind("1", bubbleAutoSort)
root.bind("r", resetArr)
root.bind("s", stopSort)
root.bind("h", help)
root.mainloop()
