#week2, day 2 
#numpy and pandas

x=np.arange(0,18)
x=x.reshape(6,3)
y=np.arange(20,38)
y=y.reshape(6,3)
print('x=',x,'\n','y=', y)
print('Addition Result=' ,'\n', np.add(x,y))


#pandas
import pandas as pd
pd.DataFrame({'Yes' : [50,21], 'No':[131,2]}) #creates a table

pd.Series([1,2,3,4,5]) 

housing=pd.read_csv("dragon.csv") #importing csv data
housing.info() #shows dataset info
housing.describe() #shows count, mean, 
