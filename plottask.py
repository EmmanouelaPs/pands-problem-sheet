import matplotlib.pyplot as plt #import matplotlib
import numpy as np #import numpy

xpoints = np.array(range(0,4)) #define range for x
fpoints = xpoints #define f function equal to x
gpoints = xpoints * xpoints #define g function x^2
hpoints = xpoints * xpoints * xpoints #define h function as x^3

#setting the axes at tehe centre

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#insert function for plots

plt.plot(xpoints, xpoints, label= "straight", color ="blue")
plt.plot(xpoints, gpoints, label= "xsquared", color ="red")
plt.plot(xpoints, hpoints, label= "xcubed", color ="green")

#randompoints = np.random.randint(1,100, 4)
#plt.scatter(xpoints, randompoints, label = "random")

#show the plots
plt.show()

#https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
#https://juejung.github.io/jdocs/Comp/html/Slides_Plot.html

 

 