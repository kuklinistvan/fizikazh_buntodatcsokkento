#!/usr/bin/env python3

import urllib.request
import csv
import io

import tkinter as tk
root = tk.Tk()
root.withdraw()
from tkinter import messagebox
 
CSV_OSZLOP_SZAM = 35

CSV_FILE_URLS = [
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vQq2Fb2v02ncoeFV7HDYh7gdAJvxdlO9Q9RSm1hQADPCrx_apAxJ7FnpKWvm9dC0vGeltdOAvvaYixn/pub?output=csv',
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vR3qidsHKppDu8LZD3fhAd4GDqJ_KqtUIvHmVgQX_Jc-0ezsGiZhfVpnFC_Y12rKDJnh31Y_vB8yn32/pub?output=csv'
]

csvUtf8 = []

for url in CSV_FILE_URLS:
    response = urllib.request.urlopen(url)
    data = response.read()
    csvUtf8.append(data.decode('utf-8'))

#print(csvUtf8)

megirtaSzamlalo = 0
atmentSzamlalo = 0
    
for csvString in csvUtf8:
    stringIO = io.StringIO(csvString)
    csvReader = csv.reader(stringIO, delimiter=',')
    for row in csvReader:
        ertek = row[CSV_OSZLOP_SZAM].split(',')[0]
        #print(ertek, end="")
        try:
            ertekSzamkent = int(ertek)
            megirtaSzamlalo+= 1
            if ertekSzamkent >= 40:
                atmentSzamlalo += 1
            #print(" - megszámolva, eddig megírta: ", megirtaSzamlalo, ", ebből átment: ", atmentSzamlalo, sep="")
        except Exception:
            pass

bukasSzazalek = round(((1-(atmentSzamlalo/megirtaSzamlalo)) * 100), 2)

szoveg = "Ennyit javítottak ki az IA0 és IB0 csoportban idáig: "+str(megirtaSzamlalo)+", ebből ennyi ment át: "+str(atmentSzamlalo)+".\n"+\
         "Azaz az évfolyam nem iMSc-s részének "+str(bukasSzazalek)+"%-a megbukott :)"   

print(szoveg)
messagebox.showinfo("Statisztika", szoveg)
