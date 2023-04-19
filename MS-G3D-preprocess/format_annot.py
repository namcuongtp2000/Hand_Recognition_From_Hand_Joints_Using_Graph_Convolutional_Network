import os
import sys


with open('D:\\NGHIEN-CUU-COMVIS\\Picture\\annotations\\Annot_TestList.txt','r') as f:
    lines = list(f.readlines())
    data = [str(line).replace('\n','') for line in lines]
    for num,line in enumerate(data):
        if 'D0X' in line:
            data.remove(line)
    for x,row in enumerate(data):    
        new_line = row.replace(',',' ')
        with open('D:\\NGHIEN-CUU-COMVIS\\Picture\\annotations\\format_test.txt','a') as f1:
                f1.write(str(new_line)+'\n')
        f1.close()
f.close()