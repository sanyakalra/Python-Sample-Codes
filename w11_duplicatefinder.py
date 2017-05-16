
# AUTHOR Sanya Kalra skalra@bu.edu
 from os import listdir, getcwd
import re
from skimage.io import imread
import numpy as np
import hashlib
from collections import defaultdict
dhash, dtr = defaultdict(list), defaultdict(list)
dict3 = {}
fnlist, fnlist2 = [], []
np.set_printoptions(threshold=np.nan)


def hash_calculation(img1):
    img1 = img1.copy(order='C')
    hashr = hashlib.md5()
    hashr.update(img1)
    hashr = hashr.hexdigest()
    return hashr


def image_splice(img1):
    img1 = 255 - img1
    array1 = img1.nonzero()
    a, b = np.min(array1[0]), np.max(array1[0])
    c, d = np.min(array1[1]), np.max(array1[1])
    return img1[a:b+1, c:d+1]

for filename1 in listdir(path=getcwd()):
    if filename1.endswith(".png") is True:
        c = re.split('([0-9]+)', filename1)
        c = int(c[1])
        fnlist2.append((c, filename1))
        img1 = imread(filename1)
        img1 = image_splice(img1)
        hash1 = hash_calculation(img1)
        dict3[filename1] = hash1
fnlist2.sort()
for (key, val) in fnlist2:
    fnlist.append(val)
i = 0
for filename1 in fnlist:
    img1 = imread(filename1)
    img1 = image_splice(img1)
    hash1 = dict3[filename1]
    dhash[hash1].append(filename1)
    imgt = np.fliplr(img1)
    hashr = hash_calculation(imgt)
    dtr[hash1].append(hashr)
    for m in range(0, 3):
        img1 = np.rot90(img1)
        hashr = hash_calculation(img1)
        dtr[hash1].append(hashr)
        imgt = np.fliplr(img1)
        hashr = hash_calculation(imgt)
        dtr[hash1].append(hashr)
    for filename2 in fnlist[i+1:]:
        hash2 = dict3[filename2]
        if hash1 == hash2:
            dhash[hash1].append(filename2)
            fnlist.remove(filename2)
        else:
            for v in dtr.values():
                if hash2 in v:
                    dhash[hash1].append(filename2)
                    fnlist.remove(filename2)
    i += 1
fnlist3 = []
for v in dhash.values():
    c = re.split('([0-9]+)', v[0])
    c = int(c[1])
    fnlist3.append((c, v))
fnlist3.sort()
with open("answers.txt", 'w') as f:
    for (keys, values) in fnlist3:
        z = str(values)[1:-1]
        z = z.split(", ")
        for ele in z:
            f.write(ele.strip("''"))
            if ele != z[-1]:
                f.write(' ')
        f.write('\n')
f.close()
hasher = hashlib.sha256()
with open('answers.txt', 'rb') as afile:
    buf = afile.read(65536)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(65536)
print(hasher.hexdigest())
