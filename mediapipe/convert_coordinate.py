import numpy as np
import os

txt_path1= "D:\\NGHIEN-CUU-COMVIS\\Coding\\mediapipe\\coordinate-file-2.txt"
txt_path2= "D:\\NGHIEN-CUU-COMVIS\\Coding\\mediapipe\\skeleton-coordinate-2.txt"
f1=open(txt_path1,'r')
f2=open(txt_path2,'w')
lines= f1.readlines()

for line in lines:
    if 'x:' in line:
        new_line1= line.replace('x:','')
        f2.write(new_line1)
    if 'y:' in line:
        new_line2= line.replace('y:','')
        f2.write(new_line2)
    if 'z:' in line:
        new_line3= line.replace('z:','')
        f2.write(new_line3)
        
f1.close()
f2.close()