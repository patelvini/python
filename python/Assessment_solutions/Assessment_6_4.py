#  Write a program which accept two file names from user and compare 
# contents of both the files. If both the files contains same contents then 
# display success otherwise display failure. Accept names of both the 
# files from command line.
# Input: Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt


import sys
import os
from pathlib import Path

f1 = sys.argv[1]
f2 = sys.argv[2]

path = os.path.abspath(f1)
path = Path(path)
fpath=str(path.parent)+"\\files\\"


def func_check(f1,f2):
	f1 = open(fpath+f1,"r")
	f2 = open(fpath+f2,"r")

	l1 = f1.read()
	l2 = f2.read()

	flag = 0

	if len(l1) != len(l2):
		print("Failure")
	else:
		for i in range(0,len(l1)):
			if l1[i]!=l2[i]:
				flag = 1
				print("Failure")
	if flag == 0:
		print("Success")

func_check(f1,f2)


