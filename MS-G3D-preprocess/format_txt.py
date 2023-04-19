import os
import sys
import glob
import csv

in_folder = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\data_test\\*.txt'
out_folder = 'D:\\NGHIEN-CUU-COMVIS\\Picture\\format_data'

for file1 in glob.glob(in_folder, recursive= True):
    in_name = os.path.basename(file1)
    out_txt = os.path.join(out_folder,in_name )
    print(out_txt)
    with open(file1,'r') as f1:
        result = str("".join(line.rstrip('\n') for line in f1))
        #convert string result to list and split elements by space
        result1 = list(result.split(' '))
        #remove even elements
        result2 = [v for i, v in enumerate(result1) if i % 2 != 0]
        #create new lists with only 3 elements
        threelines = range(0,len(result2),3)
        for num, line in enumerate(result2):
            if num in threelines:
                result3 =' '.join(result2[num:num+3])
                #convert list result3 to string
                final = ''.join(map(str, result3))
                
                for file2 in glob.glob(out_txt, recursive= True):
                    with open(file2,'a') as f2:
                        f2.write(final+'\n')
                    f2.close()
   