# Functions in Python
#
# def born(country):
#     return print('i am from' + country)
# born(' Brazil ')

#importing relevant modules

import matplotlib.pyplot as plt

# Graphs in Python without labels and title

# x = [1, 3, 5, 10]
# plt.plot(x)
# plt.show()

# y = [7,12,21,22]
# plt.plot(x,y)
# plt.show()

#Line graph

#Line 1 - points

x = [3,9,14]
y = [2,7,30]

# Plottig x and y
plt.plot(x,y, c = 'red', linewidth = 3, label = 'line 1')
plt.show()

#line 2- points
x2= [1,15,18]
y2=[0,3,12]
plt.plot(x2,y2, c = 'Green', linewidth=2, label='line 2')
plt.show()

#label the axes
plt.xlabel('X- axis')
plt.ylabel('Y- axis')
plt.title('Two Lines')
plt.showlegend
