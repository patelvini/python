# Write a program which accept file name from user and 
# create new file named as Demo.txt and copy 
# all contents from existing file into new file. 
# Accept file name through command line arguments.
# Input: ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import sys
from shutil import copyfile


f1 = sys.argv[1]
f2 = sys.argv[2]

def create_file(f_name):
	f = open(f_name,"w")
	f.write("Assessment_6_3_practice \n")
	f.close()

def copy_file(f_name):
	copyfile(f1,f2)

create_file(f1)
copy_file(f1)