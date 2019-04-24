from tkinter import *
import slate3k, time, tkinter.filedialog, keyboard

def czytaj():
    try:
        predkosc = int(wpm.get('1.0', 'end-1c'))
    except:
        predkosc = 100

    try:
        zacznij_od = int(wordCount.get("1.0", 'end-1c'))
    except:
        zacznij_od = 0

    listaSlow = []
    cont = True
    # usuwanie elementów okienka
    wpm.destroy()
    start.destroy()
    wordCount.destroy()
    wpmButton.destroy()
    # tworzenie miejsca do wyświetlenia liczby słów
    wordNum = 0
    counter = Label(window, text=wordNum)
    counter.pack()
    # ładowanie pliku
    listaSlow = Load_File()
    # Wyswietlanie kolejnych słów z zadaną prędkością w label 'word'

    for i in range(zacznij_od, len(listaSlow)):
        if cont:
            wurd = StringVar()
            wurd.set(listaSlow.__getitem__(i))
            word.configure(textvariable=wurd)
            word.update()
            vari = StringVar()
            vari.set(i)
            counter.configure(textvariable=vari)
            counter.update()
            lastWord = i
            cont = Pauza()
            time.sleep(60 / predkosc)


# Sprawdza jakiego typu jest plik, a nastepnie umieszcza kolejne słowa w listaSlow
def Load_File():
    listaSlow1 = []
    filename = tkinter.filedialog.askopenfilename()
    if filename[-3:] == 'pdf':
        with open(filename, 'rb') as file:
            extracted_text = slate3k.PDF(file)
        for page in extracted_text:
            listaSlow1 = listaSlow1 + page.split()
    elif filename[-3:] == 'txt' or filename[-3:] == 'ocx':
        with open(filename, 'r') as inputfile:
            for line in inputfile:
                line.split()
                for word in line:
                    listaSlow1.append(word)
    else:
        print("Nie udało się uzyskać rozszerzenia pliku")
    return listaSlow1


def Pauza():
    cont1 = 1
    if keyboard.is_pressed('l'):
        cont1 = 0
    else:
        pass
    return cont1


# GUI okienka
window = Tk()
window.title = "FastReader"
window.configure(background='black', height=100, width=200)
window.geometry('400x150')
window.resizable(0, 0)

word = Label(window, text="___Hello World__", fg='white', bg='black', font=("Verdana", 24))
word.pack()

wpm = Text(window, height=2, width=30)
wpm.pack()
wpmButton = Button(window, text="set wpm", command=czytaj)
wpmButton.pack()

start = Label(window, text='Od którego słowa zacząć? ')
start.pack()
wordCount = Text(window)
wordCount.pack()

window.mainloop()
