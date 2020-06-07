# mpl_squares.py

import matplotlib.pyplot as plt

#-list to hold data to be plotted
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#-generates plots in the same figure
#-fig represents the entire figure or collection of plots that are generated
#-ax represents  single plot in the figure and is the variable most used
plt.style.use('seaborn')
fig, ax = plt.subplots()

#-plot will plot the data in a meaningful way
ax.plot(input_values, squares, linewidth=3)

#-set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#-set size of tick labels
ax.tick_params(axis='both', labelsize=14)

#-plt.show() opens Matplotlib's viewer to display the plot
plt.show()