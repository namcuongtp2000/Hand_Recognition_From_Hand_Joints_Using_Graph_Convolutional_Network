import os
import sys
import numpy as np
from itertools import chain

with open(str(sys.argv[1]),'r') as f1:
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
    with open(os.path.join('D:\\NGHIEN-CUU-COMVIS\\Picture\\insert_data',str(sys.argv[1])),'a') as f2:
        f2.write(final+'\n')
f1.close()
f2.close()