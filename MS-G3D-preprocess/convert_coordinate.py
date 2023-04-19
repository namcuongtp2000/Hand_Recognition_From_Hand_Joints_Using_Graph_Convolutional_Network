import numpy as np
import os
import sys

txt_path1= 'D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix1\\IPN_train\\4CM11_7_R_#35_18.txt'
txt_path2= os.path.join("D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix2\\IPN_train", os.path.basename(txt_path1))
f1=open(txt_path1,'r')
f2=open(txt_path2,'a')
lines= f1.readlines()

for line in lines:
    if 'x:' in line:
        new_line1= line
        f2.write(new_line1.replace('x:',''))
    if 'y:' in line:
        new_line2= line
        f2.write(new_line2.replace('y:',''))
    if 'z:' in line:
        new_line3= line
        f2.write(new_line3.replace('z:',''))
        
f1.close()
f2.close()