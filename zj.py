import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df=pd.read_csv('C:/Users/ThinkPad/Desktop/新建文件夹/instance.csv',encoding='GBK')
data=df.dropna()
zujing_num_split = pd.DataFrame((x.split('元/月') for x in data['租金']),index=data.index,columns=['zujing',''])
data=pd.merge(data,zujing_num_split,right_index=True, left_index=True)
data['zujing']=data['zujing'].map(str.strip)
data['zujing']=data['zujing'].astype(float)
ddata=data[data['zujing']>=25000] #租金大于25000元

mianji_num_split = pd.DataFrame((x.split('平') for x in ddata['大小']),index=ddata.index,columns=['mianji',''])
ddata=pd.merge(ddata,mianji_num_split,right_index=True, left_index=True)
ddata['mianji']=ddata['mianji'].map(str.strip)
ddata['mianji']=ddata['mianji'].astype(float)
#print(ddata['mianji'])

bins = [0, 50, 100, 150, 200, 250, 300]
group_mianji = ['0-50', '50-100', '100-150', '150-200','200-250','250-300']
ddata['group_mianji'] = pd.cut(ddata['mianji'], bins, labels=group_mianji)
group_mianji=ddata.groupby('group_mianji')['group_mianji'].agg(len)
print(group_mianji)

quyu=ddata.groupby('区域')['区域'].agg(len)
print(quyu)
