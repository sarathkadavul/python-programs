#program to convert string to binary format
#author $ @ (R) @ -|- #  |< @ D @ \/ |_| |_

import sys
data = raw_input('enter the string  ')
ba = bytearray(data)
for bi in ba:
    print(bin(bi).split('b')[1])
