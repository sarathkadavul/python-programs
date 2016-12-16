#program to convert raw text to ascii integer format
#author $ @ (R) @ -|- #  |< @ D @ \/ |_| |_

import sys

data = raw_input("enter the string of data  ")
for asc in data:
    print(ord(asc))
