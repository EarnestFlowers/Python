#Developed by Earnest Flowers
#version 1.1
#updated - 6/1/2017
#using BeautifulSoup - to get stocks symbol, stock quantity, stock purchase price from file
#web scraps yahoo finance to show net gains/losses

import bs4 as bs
import urllib.request
import time
from colorama import Fore, Back, Style
import os.path 
import datetime
import subprocess
import locale

locale.setlocale( locale.LC_ALL, 'English_United States.1252' )

##file location
path = os.path.dirname(__file__)
symbolfile = open(path + "\\trackstocks.txt")
stockoutfile = open(path + "\\stockoutput.txt","w")

symbolslist = symbolfile.read()
readsymbollist = (symbolslist.split("\n"))
totalinvestment = 0

##loop for all symbols in symbolslist from symbolfile
i = 0
while i < len(readsymbollist):
    url = "https://finance.yahoo.com/quote/" + readsymbollist[i]
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    #finance yahoo
    stockcompany = soup.find('h1', {'data-reactid': '7'}).text
    currentprice = soup.find('span', {'data-reactid': '36'}).text

    stockoutfile.write(stockcompany + " is currently trading at $" + currentprice + "\n")
    #i+=1

    myshares = readsymbollist[i + 1]
    myprice = readsymbollist[i + 2]
    tradecommission = 6.95

    #total initial investment
    totalspent = float(myshares) * float(myprice)  + float(tradecommission)
    totalspent = round(totalspent, 2)
    temptotalspent = totalspent
    temptotalspent = locale.currency(temptotalspent, grouping = True )
    stockoutfile.write("My total investment in : " + stockcompany + " is " + str(temptotalspent) + "\n")

    #total current investment
    newtotal = float(myshares) * float(currentprice)
    newtotal = round(newtotal, 2)
    tempnewtotal = newtotal
    tempnewtotal = locale.currency(tempnewtotal, grouping = True )
    stockoutfile.write("NEW total investment in : " + stockcompany + " is " + str(tempnewtotal) + "\n")

    #money amount gain/loss
    netamount = newtotal - totalspent - float(tradecommission)
    netamount = round(netamount, 2)
    if netamount > 0:
        netamount = locale.currency(netamount, grouping = True)
        stockoutfile.write("Net gain of + " + str(netamount) + "\n")
        #print color (Fore.GREEN + "Net gain of + " + str(netamount) + "\n")
    else:
        netamount = locale.currency(netamount, grouping = True)
        stockoutfile.write("Net loss of - " + str(netamount) + "\n")
        #print color (Fore.RED + "Net loss of - " + str(netamount) + "\n")

    #% amount gain/loss
    gainloss = ((newtotal - totalspent - float(tradecommission)) / (totalspent - float(tradecommission))) * 100
    gainloss = round(gainloss, 2)
    if gainloss > 0:
        stockoutfile.write("Net gain of + " + str(gainloss) + "%" + "\n")
        #print color print(Fore.GREEN + "Net gain of + " + str(gainloss) + "%" + "\n")
    else:
        stockoutfile.write("Net loss of - " + str(gainloss) + "%" + "\n")
        #print color print(Fore.RED + "Net loss of - " + str(gainloss) + "%" + "\n")

    totalinvestment = totalinvestment + newtotal
    totalinvestment = round(totalinvestment, 2)
    i+=3
    stockoutfile.write("\n")

totalinvestment = locale.currency(totalinvestment, grouping = True )
stockoutfile.write("Total investment portfolio : " + str(totalinvestment) + "\n")

currentDT = datetime.datetime.now()
stockoutfile.write(currentDT.strftime("%m/%d/%Y") + " " + currentDT.strftime("%I:%M:%S %p"))
stockoutfile.close()

subprocess.call(['cmd.exe', '/c', path + "\\stockoutput.txt"])