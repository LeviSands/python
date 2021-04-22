#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# In[47]:


import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# ### Reading in Data

# In[10]:


# Reading in the data to a pandas DataFrame
boston_housing = pd.read_csv("Boston_housing.csv")
boston_housing.head(5)


# ### Subplots

# In[63]:


# Subplots
# plt.subplot(nrows, ncols, index)
# nrows - number of rows
# ncols - number of columns
# index - subplot you want to select

# Generate data
# Generate data to plot
linear = [x for x in range(5)]
square = [x**2 for x in range(5)]
cube = [x**3 for x in range(5)]

# Can graph individually
# 3x1 grid, first subplot
plt.subplot(3, 1, 1)
plt.plot(linear)
# xticks(ticks, position, size)
plt.xticks([2, 4], position=(0, 0.1), size=10)

# 3x1 grid, second subplot
plt.subplot(3, 1, 2)
plt.plot(square)

# 3x1 grid, third subplot
plt.subplot(3, 1, 3)
plt.plot(cube)


# In[65]:


# Can plot all together
# tight_layout - automatically adjusts subplots
fig, axs = plt.subplots(1, 2, tight_layout=True)


# ### Scatterplot

# In[30]:


# set x and y
x = boston_housing["rm"]
y = boston_housing["medv"]

# sets colors for different kinds of rooms
colors= range(boston_housing["rm"].count())

# sets the figure
# figsize - size of graph
# dpi - resolution
# facecolor - background color
# edgecolor - border color
plt.figure(figsize=(10, 6), dpi= 80, facecolor='pink', edgecolor='k')

# Scatterplot
# x and y sets data points
# s - marker size of points
# c - list of colors
# marker - marker shape of points
# alpha - sets transparency from 0 to 1
# linewidths - sets linewidth of marker edges
plt.scatter(x, y, s=25, c=colors, marker = "^", alpha=0.5, linewidths = 4)

# Setting labels
plt.xlabel("No of Rooms")
plt.ylabel("Median value of owner-occupied homes in $1000s")
plt.title("Scatterplot of No of Rooms vs Price") 

# Shows plot
plt.show()


# ### Histogram

# In[45]:


N_points = 1000
n_bins = 40

# Generates a normal distribution, center at x=0 and y=5
x = np.random.randn(N_points)

# Histogram
# x is data points
# bins - sets number of bins
# range - lower and upper range of bins
# density - if true returns probability density
# cumulative - if true shows the cumulative amounts of each bin
# histtype - displays type of histogram 
#          - {'bar', 'barstacked', 'step', 'stepfilled'}
# align - alignment of bars 
#       - {'left', 'mid', 'right'}
# orientation - {'horizontal', 'vertical'}
# color - color of bars
plt.hist(x, bins=n_bins, range = (-2, 2), density = True, cumulative = True, histtype = 'step', 
         align = 'left', orientation = 'horizontal', color = 'k')

plt.show()


# In[48]:


# tight_layout - automatically adjusts subplots
fig, axs = plt.subplots(1, 2, tight_layout=True)

# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = axs[0].hist(x, bins=n_bins)

# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

# We can also normalize our inputs by the total number of counts
axs[1].hist(x, bins=n_bins, density=True)

# Now we format the y-axis to display percentage
axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))


# In[ ]:




