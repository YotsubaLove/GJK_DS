import pandas as pd
pdbike = pd.read_csv('xxx.csv',usecols=[3,4,5])
pdcar = pd.read_csv('xxx.csv',usecols=[0,1,2])
pdVcar = pd.read_csv('xxx.csv',usecols=[6])
radcar = pdcar['carRad'].tolist()
Xcar = pdcar['carX'].tolist()
Ycar = pdcar['carY'].tolist()
Xbike = pdbike['bikeX'].tolist()
Ybike = pdbike['bikeY'].tolist()
Vcar = pdVcar['Vcar'].tolist()
coor = [(Xcar[i], Ycar[i]) for i in range(len(Xcar))]
coorbike = [(Xbike[i], Ybike[i]) for i in range(len(Xbike))]
radbike = pdbike['bikeRad'].tolist()
# print(radcar)
# print(radbike[0])
print(coor)