import os

with open('D:\\NGHIEN-CUU-COMVIS\\Picture\\data_test\\1CM1_1_R_#217_1.txt','r') as f:
    lines=list(f.readlines())
    data = [str(line).replace('\n','') for line in lines]
    target_label = str(data[2]).split(' ')[0]
    print(target_label)
