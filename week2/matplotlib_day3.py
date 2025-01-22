import pandas as pd
housing=pd.read_csv("dragon.csv")
import warnings #to remove warnings
warnings.filterwarnings("ignore")


import matplotlib.pyplot as plt
#line plot
housing.area.plot(kind='line', color='g', label= 'area', linewidth=2, alpha = 1, grid= True, linestyle=':')
housing.price.plot(color='r', label= 'Price', linewidth=2, alpha = 1, grid= True, linestyle='-.')
plt.legend(loc='upper right')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Plot')
plt.show()

#scatter plot
housing.plot(kind='scatter', x='area', y='price', alpha=0.5, color='r')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area Price Scatter Plot')

#histogram
#bins=no of bars in a figure
housing.price.plot(kind="hist", bins=50, figsize=(6,6))
plt.show()
