import os
import sys
import numpy as np
from itertools import chain
txt_path = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix3\\IPN_train\\4CM11_7_R_#35_18.txt'
with open(txt_path,'r') as f1:
    lines=list(f1.readlines())
    data = [str(line).replace('\n','') for line in lines]
    # initializing k 
    k = '1'
  
    # initializing N
    N = 21
    # using itertool.chain()
    # inserting K after every Nth number 
    res = list(chain(*[data[i : i+N] + [k] 
            if len(data[i : i+N]) == N 
            else data[i : i+N] 
            for i in range(0, len(data), N)]))
    final = '\n'.join(map(str, res))
    with open(os.path.join('D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix4\\IPN_train',os.path.basename(txt_path)),'a') as f2:
        f2.write(final+'\n')
f1.close()
f2.close()