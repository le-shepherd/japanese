#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Start: 2017/03/12
# This little program teaches the Japanese Kana scripts
#
# Below the first fully working version
# For my notes, see martin_python.org
import csv
import random
import re # for regular expression stuff
import time
import pickle # to turn the csv table into a byte stream
import os.path # to check whether pickled data exists in file already
# for terminal output in color
from colorama import init
from colorama import Fore, Back, Style

init()

# inputData = open("japanese_kana-tables.csv","r",newline="")

if os.path.isfile("./data.pickle"):
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
else:
    with open("japanese_kana-tables.csv","r",newline="") as inputData:  
    # the with statement guarantee that the opened file is closed at the
    # end of the exectution of the whole block  
        data = list(csv.reader(inputData, delimiter=','))
    
    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

        
# data[0][0] # now we can index into the list, with list[row nr][col nr]
# 'vowel'
len(data) # for the number of rows
len(data[0]) # for the number of columns (actually counting the items in a row)

# We need to collect examples for the kana
# https://en.wiktionary.org/wiki/Appendix:1000_Japanese_basic_words
# HIER WEITER
# format: table with all kana and simple examples, or interactive searching? And should the kana be highlighted?
if os.path.isfile("./dataExamples.pickle"):
    with open('dataExamples.pickle', 'rb') as f:
        dataEx = pickle.load(f)
else:
    with open("japanese_kana-examples.csv","r",newline="") as inputData:  
    # the with statement guarantee that the opened file is closed at the
    # end of the exectution of the whole block  
        dataEx = list(csv.reader(inputData, delimiter=','))
    
    with open('dataExamples.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(dataEx, f, pickle.HIGHEST_PROTOCOL)

examplesKana = [x[0] for x in dataEx]

# Please write ka in hiragana
# OK: procedure:
# 1. first randomly selecting a specific row k and a specific column l (except the 0 rows or 0 colums)
# 2. secondly construe the romanji out of that rows row[0][l] row[k][0]

# Why not count the number of elements and then load them in some usable format
kanaVowels = len(data) 
kanaOnsetsFull = len(data[0]) 
kanaVowelRange = list(range(1, kanaVowels))
kanaOnsetRange = list(range(1, kanaOnsetsFull))
kanaOnsetHira = list(range(1, kanaOnsetsFull,2))
kanaOnsetKata = list(range(2, kanaOnsetsFull,2))

preferences = input("Do you want do train all kana, only hiragana, or only katakana? (a/h/k)")
if preferences == "h":
     kanaOnsetRange = kanaOnsetHira
     print("Training only hiragana.")  
elif preferences == "k":
    kanaOnsetRange = kanaOnsetKata
    print("Training only Katakana.")
else:
    print("Training all kana.")

# we are setting up an empty list to collect the items that were wrong
wrongItems = []

# random.seed(7)
random.shuffle(kanaOnsetRange)
for x in (kanaOnsetRange):
       y = random.choice(kanaVowelRange)
       kanaItem = data[y][x]
       if kanaItem == "":
            continue
       else:
           # print(vocabItem)
           # if kanaItem in dataEx
           kanaEx = [x[0] for x in dataEx].index(kanaItem)
           input("Please read out {0}.".format(kanaItem))
           # time.sleep(10)
           # construct romanji
           onset = data[0][x]
           coda = data[y][0]
           onsetClean = re.sub("_[kh]","",onset)
           # m = re.search('(?<=_)\w+',onset) # (?<=...) A positive
           # lookbehind assertion. Matches if the current position in the
           # string is preceded by a match for ... that ends at the
           # current postion. 
           # m.group(0)
           romanji = onsetClean + coda
           # Add: romanji specials!
           if romanji == "du":
                 romanji = "dzu"
           elif romanji == "tu":
                 romanji = "tsu"
           elif romanji == "ti":
                 romanji = "chi"
           elif romanji == "di":
                 romanji = "dji"
           elif romanji == "si":
                 romanji = "shi"
           elif romanji == "zi":
                 romanji = "ji"
           elif romanji == "hu":
                 romanji = "fu"
           print(romanji)
           knowDontknow = input("Did you know this kana? (y/n)")
           if knowDontknow == "y":
                 print("Good job!")
           else:
                  print("You'll do better next time!")
                  print("Use this example to remember the kana:")
                  print(Fore.RED + dataEx[kanaEx][1],dataEx[kanaEx][3],dataEx[kanaEx][4])
                  print(Style.RESET_ALL)
                  wrongItems.append([kanaItem,romanji])
           choice = input("Press q to Quit, else continue.")
           # input("Continue?")
           if choice == 'q':
               print("These items were wrong" + str(wrongItems))
               break
# inputData.close()
#############################################
#
#   END 
#      
##################################################

#











