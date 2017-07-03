import pandas as pd
df=pd.read_csv('C:/Users/ThinkPad/Desktop/新建文件夹/instance.csv',encoding='GBK')
data=df.dropna()
#print(data)
huxing=data.groupby('类型')['类型'].agg(len)
print(huxing)

import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='STXihei', size=11)
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
plt.barh([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],huxing,color='#052B6C',alpha=0.8,align='center',edgecolor='white')
plt.ylabel('类型')
plt.xlabel('数量')
plt.xlim(0,500)
plt.ylim(0,16)
plt.title('房源户型分布情况')
plt.legend(['数量'], loc='upper right')
plt.grid(color='red',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.yticks(a,('1室0厅','1室1厅','1室2厅','2室0厅','2室1厅','2室2厅','3室0厅','3室1厅','3室2厅','4室0厅','4室1厅','4室2厅','4室3厅','5室1厅','5室2厅','5室3厅'))
plt.show()
