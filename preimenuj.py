import os

# Za hitrejši zajem podatkov sem si sposodil nekaj uporabniških računov. Funkcija
# preimenuj poskrbi, da se v html datotekah namesto njihovih imen pojavlja 'uporabnik'.

imena = []

def preimenuj(datoteka):
    '''V html datoteki vse pojavitve uporabniškega imena iz seznama 'imena' zamenja z 'uporabnik'.'''
    with open (datoteka, 'r', encoding='utf-8') as f:
        string = f.read()
        for x in imena:
            string = string.replace(x, 'uporabnik')
    with open (datoteka, 'w', encoding='utf-8') as f:
        f.write(string)
   

for datoteka in os.listdir('zajeti-podatki'):
    preimenuj('zajeti-podatki/' + datoteka)