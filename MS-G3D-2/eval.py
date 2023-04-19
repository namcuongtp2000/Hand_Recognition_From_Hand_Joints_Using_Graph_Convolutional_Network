import os

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
right_sample = 'D:\\TAI-LIEU-HOC-TAP\\Coding\\MS-G3D\\work-dir\\val_joint\\right-samples.txt'
with open(right_sample,'r') as f1:
    pred = [int(line.split(',')[0]) for line in f1]
    #print(pred)
with open(right_sample,'r') as f2:
    actual = [int(line.split(',')[1].replace('\n','')) for line in f2]
    #print(actual)
#confusion matrix
cf_matrix = confusion_matrix(actual,pred)
print(cf_matrix)
#normalize matrix
cmn=cf_matrix.astype('float') /cf_matrix.sum(axis=1)[:,np.newaxis]
fig = plt.figure(figsize=(10, 7))
#ax = sns.heatmap(cf_matrix, annot=True,fmt='d', cmap='Blues')
ax = sns.heatmap(cmn, annot=True,fmt='.2f', cmap='Blues')
ax.set_title('Confusion Matrix of IPN Hand Gesture')
ax.set_xlabel('Predicted labels',fontsize =14)
ax.set_ylabel('Actual labels ',fontsize=14)
class_names= ["Pointing with one finger","Pointing with two fingers","Click with one finger","Click with two fingers","Throw up","Throw down","Throw left","Throw right","Open twice","Double click with one finger","Double click with two fingers","Zoom in","Zoom out"]
## Ticket labels - List must be in alphabetical order
ax.xaxis.set_ticklabels(class_names,rotation=90)
ax.yaxis.set_ticklabels(class_names,rotation=0)

## Display the visualization of the Confusion Matrix.
plt.show()

#precison,recall and F1 score
print(classification_report(actual,pred,digits=3))
