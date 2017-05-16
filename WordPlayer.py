# -*- coding: utf-8 -*-
import json
import numpy as np
from collections import Counter, defaultdict
import sys
import time
from copy import deepcopy

st = time.time()

file1, file2, wordlen = '', '', ''
file1 = sys.argv[1]
file2 = sys.argv[2]
dict1, dict2, dictp = defaultdict(list), defaultdict(list), defaultdict(list)
dicta, dictcom = defaultdict(list), defaultdict(list)
dictcord = defaultdict(list) 
dicttemp =  defaultdict(list)
dictcord1 = {}
dicta1 = defaultdict(list)
dict1sort, dict2sort = defaultdict(dict), defaultdict(dict)
grid1, list1, list2, ans, result, grid4, grid3 = [], [], [], [], [], [], []
size1, len_ans_b, flag1, flag,counter = 0, 0, 0, 0, 0
lengths, lengthcopy, tempans, list4, list5, pathtemp = [], [], [], [], [], []
list_paths =[]

def neighbors(grid2):
    for i in range(0, size1):
        for j in range(0, size1):
            dictcord1[(i, j)] = grid2[i][j]
            if (j+1) < size1:
                dicta1[(i, j+1)].append((i,j))
                dicta1[(i, j)].append((i, j+1))
                if (i-1) != -1:
                    dicta1[(i-1, j+1)].append((i, j))
                    dicta1[(i, j)].append((i-1, j+1))
            if (i+1) < size1:
                dicta1[(i+1, j)].append((i,j))
                dicta1[(i, j)].append((i+1, j))
            if (i+1 < size1) and (j+1 < size1):
                dicta1[(i+1, j+1)].append((i,j))
                dicta1[(i, j)].append((i+1, j+1))
    return 0

def check4dup(dupt_coord, word, pointer):
    ele_cord = []
    pointercopy = 0 
    pointercopy += pointer
    global counter, pathtemp
    y = []
    letter = word[pointercopy]
    print("Letter in use: ", letter)
    
    print("Dupt_Cord: ",dupt_coord)
    #for cord1 in dupt_coord:
    pathtemp.append(dupt_coord)
    for keys, values in dictcord1.items():
        if letter == values:
            if keys in dicta1[dupt_coord]:
                ele_cord.append(keys)
                print("Ele_cord: ", ele_cord)
            else:
                return pathtemp
    print("pointer near cord1: ", pointercopy)
    for x in ele_cord:
        print("Pointer in elecord", pointercopy)
        print("Cord1: ", dupt_coord, "X: ", x)
        pointercopy += 1
        print("Pointer in if: ", pointercopy)
        counter += 1
        pathtemp.append(x)
        #print("Pathtemp in if: ", pathtemp)
        #print("Counter in if: ", counter)
        pathtemp.append(check4dup(x , word, pointercopy))                
    print("final path: ",pathtemp)
    return pathtemp

def chkdup(cord1, path1, word_ind, size1):
    for cord in dicta1[cord1]:
        if (word[word_ind] == dictcord1[cord]) and (word[word_ind] not in path1):
            if(word_ind == (size1-1)):
                list_paths.append(path1 + word[word_ind])
                return 0
            path1 += word[word_ind]
            chkdup(cord, path1, (word_ind+1), size1)

def searchword(grid3, lengths):
    wordlen = lengths[0]
    neighbors(grid3)
    print("Dict1sort: ", dict1sort)
    print("Dictcord1: ",dictcord1)
    for cord in dictcord1:
        for adjcord in dicta1[cord]:
            prev = dictcord1[cord]
            prev1 = dictcord1[adjcord]
            combo1 = prev + prev1
            if combo1 in dict1sort[wordlen]:
                print("dictcord: ", cord, " dicta1: ", adjcord)
                print("Prev: ", prev, " Prev1: ", prev1, " combo1: ", combo1)
                print("Dict1sort list: ", dict1sort[wordlen][combo1])
                wordlist = dict1sort[wordlen][combo1]
                for word in wordlist:
                    print("Current word= ", word)
                    path = combo1
                    chkdup(adjcord, combo1, 2, size1)                    
                    #path_final = []
                    #path_final.append(cord)
                    #letter = word[1]
                    #print("Letter= ",letter)
                    '''for keys, values in dictcord1.items():
                        if letter == values:'''
                    #key_final = adjcord
                    #pointer = 2
                    #path_final.append(check4dup(adjcord, word, pointer))
                #print("path: ",path_final)
                                        #break
                        #         else:
                        #             print("not there next to this cord, ")
                        # #find if each of list4 in cord1 adj
                # word = 'hoe'
                # k = 2
                # cord1 = adjcord
                # cord2 = adjcord
                # for i in dicta1[cord1]:         # i = adj coordinates of cord1
                #     print("i= ",i)
                #     # for j in word:
                #     if word[k] == dictcord1[i]:
                #         cord1 = 
                       # k = 2
                        # print("j= ", j)
                        # if dictcord1[i] == j:   # dictcord[i] is letter at i, 
                        #     print("i:", i, " j: ", j, "dictcord[i]: ", dictcord1[i])
                         #  cord1 = cord2
data = open(file1, 'r')
for word in data:
    word = word.replace("\n", "")
    len1 = len(word)
    dict1[len1].append(word)
for key in dict1:
    for word in dict1[key]:
        letter12 = word[0:2]
        dicttemp[letter12].append(word)
        dict1sort[key][letter12] = dicttemp[letter12]
    dicttemp.clear()
data = open(file2, 'r')
for word in data:
    word = word.replace("\n", "")
    len2 = len(word)
    dict2[len1].append(word)
for key in dict2:
    for word in dict2[key]:
        dicttemp[word[0:2]].append(word)
        dict2sort[key][word[0:2]] = dicttemp[word[0:2]]
    dicttemp.clear()

while(True):
    # try:
    line = input()
    dictp = json.loads(line)
    grid = dictp["grid"]
    size1 = int(dictp["size"])
    lengths = dictp["lengths"]
    for i in lengths:
        i = int(i)
    lengthcopy = deepcopy(lengths)
    for letters in grid:
        grid1.append(list(letters))
    grid2 = np.array(grid1)
    grid2 = np.transpose(grid2)
    wordlen = lengths[0]
    grid3 = np.copy(grid2)
    searchword(grid3, lengths)
    for a1 in result:
        print(a1)
    print(".")
    # except:
    end = time.time()
    print("Time = ", end-st)
    exit(0)
    