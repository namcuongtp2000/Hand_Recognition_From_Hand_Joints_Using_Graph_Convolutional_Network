import os
import re
import sys
txt_path = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix2\\IPN_train\\4CM11_7_R_#35_18.txt'
with open(txt_path) as f:
   result = str("".join(line.rstrip('\n') for line in f))
   
   #convert string result to list and split elements by space
   result1 = list(result.split(' '))
   #remove first '' elements
   del result1[0]
   #create new lists with only 3 elements
   threelines = range(0,len(result1),3)
   for num, line in enumerate(result1):
      if num in threelines:
         result2 =' '.join(result1[num:num+3])
         #convert list result3 to string
         final = ''.join(map(str, result2))
         with open(os.path.join('D:\\NGHIEN-CUU-COMVIS\\Picture\\fix_data\\fix3\\IPN_train',os.path.basename(txt_path)),'a') as w:
            w.write(final+'\n')
w.close()
f.close()
