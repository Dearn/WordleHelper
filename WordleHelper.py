#!/usr/bin/env python
import PySimpleGUI as sg
import sys


if len(sys.argv) > 1:
    dlugosc = int(sys.argv[1])
else:
    dlugosc = 5
with open('slownik' + str(dlugosc), 'r', encoding='utf-8') as dictionaryFile:
    slownik = dictionaryFile.readlines()
MozliweSlowa = []    
temp = []
for x in slownik:
    MozliweSlowa.append(x.replace("\n", ""))

def PosiadaLitereNaMiejscu(l,z):
    global MozliweSlowa
    for wyraz in MozliweSlowa:
        if(wyraz[z] == l):
            temp.append(wyraz)
    MozliweSlowa.clear()
    MozliweSlowa = temp.copy()
    temp.clear()


def NiePosiadaLitereNaMiejscu(l,z):
    global MozliweSlowa
    for wyraz in MozliweSlowa:
        if(wyraz[z] == l):
            MozliweSlowa.remove(wyraz)
        if(l not in wyraz):
            MozliweSlowa.remove(wyraz)


def BrakLitery(z):
    global MozliweSlowa
    for wyraz in MozliweSlowa:
        if(z in wyraz):
            MozliweSlowa.remove(wyraz)

            
default = ""
labels_and_keys = {'Zatwierdzone:':'-ZATWIERDZONE-', 'Złe:':'-ZLE-', 'Brak:':'-BRAK-'}

font = ('Courier New', 11)
sg.theme('DarkBlue4')
sg.set_options(font=font)

layout = [[sg.Push(), sg.Text(label), sg.Input(default, do_not_clear=False, key=key)]
        for label, key in labels_and_keys.items()] + [[sg.Push(), sg.Button('Send')]] + [[sg.Push(), sg.Button('Clear')]]

window = sg.Window('WordleHelper', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Clear':
        MozliweSlowa.clear()
       
        for x in slownik:
            MozliweSlowa.append(x.replace("\n", ""))
        
    zatwierdzone  = values['-ZATWIERDZONE-']
    zle = values['-ZLE-']
    brak = values['-BRAK-']

# Potwierdzone
    for i in range(5):
        if(len(zatwierdzone) == dlugosc):
            for i in range(0,dlugosc):
                if(zatwierdzone[i] != '.'):
                 PosiadaLitereNaMiejscu(zatwierdzone[i],i)
            # PosiadaLitereNaMiejscu('a',0)
    for i in range(50):
        if(len(zle) == dlugosc):
            for i in range(0,dlugosc):
                if(zle[i] != '.'):
                    NiePosiadaLitereNaMiejscu(zle[i],i)

    if(len(brak)>1):
        for i in range(50):
            for z in brak:
                BrakLitery(z)

    for i in MozliweSlowa:
        print(i, end=" ")
    print(len(MozliweSlowa), "\n\n")
    
window.close()
