# Accept file name and one string from user and return the frequency 
# of that string from file.
# Input: Demo.txt Marvellous
# Search “Marvellous” in Demo.txt

import sys
import os
from pathlib import Path

f1 = sys.argv[1]
s = sys.argv[2]

path = os.path.abspath(f1)
path = Path(path)
fpath=str(path.parent)+"\\files\\"

count = 0

def fun_check(f1,s):
	f = open(fpath+f1,"r")
	str1 = f.read().split()
	count = 0
	for i in str1:
		if i == s:
			count += 1
	return count

print("Frequency of {} is {}".format(s,fun_check(f1,s)))