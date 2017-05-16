
# AUTHOR Sanya Kalra skalra@bu.edu
import sys
from collections import defaultdict
from itertools import permutations
from copy import deepcopy
data = open(sys.argv[1], 'r')
list1, list2 = [], []
dict1, dict2 = defaultdict(list), defaultdict(list)
dictp = defaultdict(list)
dict3 = defaultdict(dict)
for listword in data:
    listword = listword.replace("\n", "")
    m = len(listword)
    dict1[m].append(listword)
    listwordcopy = ''.join(sorted(listword))
    dictp[listwordcopy].append(listword)
while (True):
    inputword, n = input().split()
    n = int(n)
    if n == 0:
        exit(0)
    inputwordcopy = inputword
    if n == len(inputword):
        inputwordsort = ''.join(sorted(inputword))
        if inputwordsort in dictp:
            list2 = deepcopy(dictp[inputwordsort])
        else:
            break
    else:
        for listword in dict1[n]:
            for i in range(0, n):
                if listword[i] not in inputword:
                    break
                else:
                    inputword = inputword.replace(listword[i], "", 1)
                    if i == n-1:
                        list2.append(listword)
            inputword = inputwordcopy
    list2.sort()
    for word in list2:
        print(word)
    list2.clear()
    print('.')
