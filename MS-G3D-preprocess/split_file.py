from operator import index
import os
import sys
import numpy as np
from itertools import chain

with open('D:\\NGHIEN-CUU-COMVIS\\Picture\\data_test\\1CM1_1_R_#217_1.txt','r') as f:
    lines=list(f.readlines())
    data = [str(line).replace('\n','') for line in lines]
    print(data)
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
    with open('D:\\NGHIEN-CUU-COMVIS\\Picture\\data_test\\test.txt','a') as f2:
        f2.write(repr(str(res)+'\n'))

    