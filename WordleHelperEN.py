#!/usr/bin/env python
import PySimpleGUI as sg



with open('dict5') as dictionaryFile:
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

window = sg.Window('Window Title', layout)

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
    for i in range(50):
        if(len(zatwierdzone) == 5):
            for i in range(0,5):
                if(zatwierdzone[i] != '.'):
                 PosiadaLitereNaMiejscu(zatwierdzone[i],i)
        # PosiadaLitereNaMiejscu('a',0)
    for i in range(50):
        if(len(zle) == 5):
            for i in range(0,5):
                if(zle[i] != '.'):
                    NiePosiadaLitereNaMiejscu(zle[i],i)

    if(len(brak)>1):
        for i in range(50):
            for z in brak:
                BrakLitery(z)

    sg.Print(MozliweSlowa)
        

window.close()
