import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
right_sample = 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\work-dir\\val_joint\\right-samples.txt'
with open(right_sample,'r') as f1:
    pred = [int(line.split(',')[0]) for line in f1]
    #print(pred)
with open(right_sample,'r') as f2:
    actual = [int(line.split(',')[1].replace('\n','')) for line in f2]
    #print(actual)

cf_matrix = confusion_matrix(actual,pred)
print(cf_matrix)
fig = plt.figure(figsize=(16, 14))
ax = plt.subplot()
sns.heatmap(cf_matrix, annot=True,ax=ax, cmap='Blues') # values_format = '.5f'
ax.set_title('Confusion Matrix of IPN Hand Gesture')
ax.set_xlabel('Predicted Values',fontsize =20)
ax.set_ylabel('Actual Values ',fontsize=20)
class_names= ["Pointing with one finger","Pointing with two fingers","Click with one finger","Click with two fingers","Throw up","Throw down","Throw left","Throw right","Open twice","Double click with one finger","Double click with two fingers","Zoom in","Zoom out"]
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(class_names,rotation=45,fontsize=10)
ax.yaxis.set_ticklabels(class_names,rotation=0,fontsize =10)

## Display the visualization of the Confusion Matrix.
plt.show()