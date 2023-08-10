import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/Acer/Desktop/FOD/house.csv")
print("csv  data ")
print(data)
house_data=np.array(data)
house_data=house_data.astype(int)
print("numpy array")
print(house_data)
bedroom=house_data[:,1]
four=house_data[bedroom>4]
avg=np.mean(four[:,0])
print("average of price greater than 4 bedroom",avg)
