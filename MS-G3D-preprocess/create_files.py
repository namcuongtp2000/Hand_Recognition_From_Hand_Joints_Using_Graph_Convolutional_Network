import os
from this import d

for file in os.listdir('D:\\NGHIEN-CUU-COMVIS\\Picture\\data_raw'):
    filename = (os.path.basename(file)).replace('.txt','')
    for i in range(1,22,1):
        wrt_filename = "%s_%i.txt" %(filename,i)
        with open(os.path.join('D:\\NGHIEN-CUU-COMVIS\\Picture\\format_data',wrt_filename),'a') as f:
            f.write('')    
        f.close()