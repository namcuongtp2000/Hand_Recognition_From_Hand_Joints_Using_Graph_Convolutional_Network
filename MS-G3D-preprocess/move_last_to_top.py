import os
import sys
txt_path = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix6\\IPN_train\\4CM11_7_R_#35_18.txt'
with open(txt_path,'r') as f1:
    lines=list(f1.readlines())
    data = [str(line).replace('\n','') for line in lines]
    data.insert(0,data.pop())
    data.insert(0,data.pop())
    data.insert(0,data.pop())
    final = '\n'.join(map(str, data))
    with open(os.path.join('D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix7\\IPN_train',os.path.basename(txt_path)),'a') as f2:
        f2.write(final+'\n')
f2.close()
f1.close()