# -*- coding: utf-8 -*-
"""Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AbuWds8AZlJSwKuXUfXpawjcWauSA_n_
"""

#1. Introduction and Line Plot
import matplotlib.pyplot as plt # Data visualization library
plt.plot([1,2,3],[5,7,4]) # [1,2,3] -> x; [5,7,4] -> y;
plt.show() # move plot to the foreground

#2. Legends, Titles and Labels
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]
plt.plot(x,y)
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.show()
import matplotlib. pyplot as plt
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
plt.plot(x, y, label = 'First Line')
plt.plot(x2, y2, label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#3. Bar Charts and Histograms
import matplotlib.pyplot as plt
x = [2,4,6,8,10] # width of bar < 1
y = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y, label='Bars1', color = 'r')
plt.bar(x2,y2, label='Bars2', color = 'c') # c -> cyan
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
#------------------------------------------------------
import matplotlib.pyplot as plt
population_ages = [22,55,62,45, 21, 22,34, 
42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ids =[x for x in range(len(population_ages))]
plt.bar(ids, population_ages, label='bars')
# bins =[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
# plt.hist(population_ages, bins, label='bars',histtype = 'bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#4. Scatter Plots
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y= [5,2,4,7,6,9,3,1]
plt.scatter(x,y, label='skitscat', color='k', marker='o', s=100) # k-black
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
#*note: check "matplotlib marker option" at google

#5. Stack Plots
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
plt.plot([],[],color='m', label='sleeping', linewidth=5)
plt.plot([],[],color='c', label='eating', linewidth=5)
plt.plot([],[],color='r', label='working', linewidth=5)
plt.plot([],[],color='k', label='playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#6. Pie Charts
import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c','m','r','b']
plt.pie(slices, labels = activities, colors=cols, startangle=90, 
shadow = True, explode=[0, 0.1,0,0], autopct='%1.1f%%')
# explode - pull out; autopct - change to percentage 
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# Commented out IPython magic to ensure Python compatibility.
#7. Loading Dataset from Files
from google.colab import drive
drive.mount('/content/drive')         
# mount '/content/drive' to virtual machine directory for google colab user
#below where the file is in gdrive, change with your
data_path = "/content/drive/My Drive/Colab Notebooks/"
import numpy as np
data = np.loadtxt(data_path + 'data_decision_trees.txt', delimiter=',')
X, y = data[:, :-1], data[:, -1]
# print(X)
# %cd /content/drive/My Drive/Colab Notebooks
# %pwd

''' create a file "example.txt" and then save it to google drive
1,5
2,3
3,4
4,7
5,4
6,3
7,5
8.7
9,4
10,4
'''
from google.colab import drive
drive.mount('/content/drive')         
# mount '/content/drive' to virtual machine directory for google colab user
#below where the file is in gdrive, change with your
data_path = "/content/drive/My Drive/Colab Notebooks/"
import numpy as np
import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open(data_path + 'example.txt', 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter=',')
  for row in plots:
    x.append(row[0])
    y.append(row[0])
plt. scatter(x,y, label='Loaded from the file')
plt.plot(x,y, label='Loaded from the file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#2
'''
Use matplotlib.pyplot.plot to produce a plot of the functions 𝑓(𝑥) =
𝑒― 𝑥 10 and 𝑔(𝑥) = 𝑥𝑒―𝑥3 over the interval [0, 10]. Include labels for the 
x- and y-axes, and a legend explaining which line is which plot. Save 
the plot as a .jpg (“Jpeg”) file and send me a copy with your work.

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 50)

f_x = np.exp(-1*x/10)
g_x = np.exp(-x/3)*x


plt. plot(x,f_x, label='f(x) Graph')
plt.plot(x,g_x, label=' g(x) Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function Graph')
plt.legend()
plt.show()

# 3 
'''
The shape of a limacon can be defined parametrically as 
𝑟  =  𝑟0  + cos 𝜃
𝑥  =  𝑟cos 𝜃
𝑦  =  𝑟 𝑠𝑖𝑛 𝜃 
When 𝑟0 = 1, this curve is called a cardioid. Use this definition to plot 
the shape of a limacon for 𝑟0 = 0.8, 𝑟0 = 1.0, and 𝑟0 = 1.2. Be sure to 
use enough points that the curve is closed and appears smooth (except 
for the cusp in the cardioid). Use a legend to identify which curve is 
which. Save the plot as a .pdf file and send me a copy with your work.
'''
import matplotlib.pyplot as plt
import math
from matplotlib.pyplot import figure
#Set figure size
figure(num=None, figsize=(5,10))
r_values = [0.8, 1.0, 1.2]
#We will create subplots in 3x1 arrangement
for j in range(1,4):
    ax = plt.subplot(3,1, j)     #3,1,j means 3rd row, 1st column, jth subplot
    #Set title for jth subplot
    ax.set_title(str(r_values[j-1]))
    x = []        #Empty lists that will store values of x and y
    y = []
    #Generating x and y values according to r and theta as given in equation
    for theta in range(0,360):
        r = r_values[j-1] + math.cos(theta)
        x.append(r*math.cos(theta))
        y.append(r*math.sin(theta))
        #Plot x,y points
        plt.scatter(x, y, color='r')