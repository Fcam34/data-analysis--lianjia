import pandas as pd
import matplotlib.pyplot as plt
from dateutil.parser import parse  
import numpy as np 

df=pd.read_csv('C:/Users/ThinkPad/Desktop/新建文件夹/instance.csv',encoding='GBK')
data=df.dropna()

time = data.sort_values(by='挂牌时间').head(80)

zujing_num_split = pd.DataFrame((x.split('元/月') for x in time['租金']),index=time.index,columns=['zujin',''])
time=pd.merge(time,zujing_num_split,right_index=True, left_index=True)
time['zujin']=time['zujin'].map(str.strip)
time['zujin']=time['zujin'].astype(float)
print(time['zujin'])

bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
group_zujin = ['0-5000', '5000-10000', '10000-15000', '15000-20000','20000-25000','25000-30000','35000-40000','40000-45000']
time['group_zujin'] = pd.cut(time['zujin'], bins, labels=group_zujin)
group_zujin=time.groupby('group_zujin')['group_zujin'].agg(len)
print(group_zujin)

quyu=time.groupby('区域')['区域'].agg(len)
print(quyu)
