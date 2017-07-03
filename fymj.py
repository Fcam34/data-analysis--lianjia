import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df=pd.read_csv('C:/Users/ThinkPad/Desktop/新建文件夹/instance.csv',encoding='GBK')
data=df.dropna()

mianji_num_split = pd.DataFrame((x.split('平') for x in data['大小']),index=data.index,columns=['mianji',''])

data=pd.merge(data,mianji_num_split,right_index=True, left_index=True)

data['mianji']=data['mianji'].map(str.strip)

data['mianji']=data['mianji'].astype(float)

#print(data['mianji'])


bins = [0, 50, 100, 150, 200, 250, 300]
group_mianji = ['0-50', '50-100', '100-150', '150-200','200-250','250-300']
data['group_mianji'] = pd.cut(data['mianji'], bins, labels=group_mianji)

group_mianji=data.groupby('group_mianji')['group_mianji'].agg(len)
print(group_mianji)


plt.rc('font', family='STXihei', size=15)
a=np.array([1,2,3,4,5,6])
plt.bar([1,2,3,4,5,6],group_mianji,color='blue',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('面积分组')
plt.ylabel('数量')
plt.title('房源面积分布')
plt.legend(['数量'], loc='upper right')
plt.grid(color='red',linestyle='--', linewidth=1,axis='x',alpha=0.4)
plt.xticks(a,('0-50', '50-100', '100-150', '150-200','200-250','250-300'))
plt.show()
