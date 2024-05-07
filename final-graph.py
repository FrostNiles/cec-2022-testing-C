import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys

function_numbers = [i for i in range(1, 13)]

dimension = sys.argv[1]
dimension = int(dimension)
matlab_deviations = []  # create an empty list to store deviations
deviations = []  # create an empty list to store deviations
python_deviations = []  # create an empty list to store deviations

# load deviations from files
for i in range(1, 13):
    if i in [12]:
        continue
    with open(f'test_data/result/graph/C/lowest_dev_{i}_dim_{dimension}.txt', 'r') as file:
        contents = file.read()
        if 'Deviation:' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = deviation.split('\n')[0]
            deviation = float(deviation)
            deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File lowest_dev_{i}_dim_{dimension}.txt does not contain a ':'")

# load deviations from files
for i in range(1, 13):
    with open(f'test_data/result/graph/Matlab/lowest_dev_{i}_dim_{dimension}.txt', 'r') as file:
        contents = file.read()
        if 'Deviation:' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = deviation.split('\n')[0]
            deviation = float(deviation)
            matlab_deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File lowest_dev_{i}_dim_{dimension}.txt does not contain a ':'")

for i in range(1, 13):
    with open(f'test_data/result/graph/Python/lowest_dev_{i}_dim_{dimension}.txt', 'r') as file:
        contents = file.read()
        if 'Deviation:' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = deviation.split('\n')[0]
            deviation = float(deviation)
            python_deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File lowest_dev_{i}_dim_{dimension}.txt does not contain a ':'")

fig, ax1 = plt.subplots(figsize=(15, 10))

# Define the width of a bar
bar_width = 0.2

# Positions of the left bar-boundaries
bar_l = [i + 1 for i in range(len(function_numbers))]

# Positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i + (bar_width / 2) for i in bar_l]

# Create the bar plot for the first set of data
ax1.bar(bar_l, deviations, width=bar_width, color='blue', label='C')

# Create a new axis for the second set of data
ax2 = ax1.twinx()
ax2.bar([p + bar_width for p in bar_l], matlab_deviations, width=bar_width, color='red', label='Matlab')

# Create a new axis for the third set of data
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Move the right axis 60 points outward
ax3.bar([p + 2*bar_width for p in bar_l], python_deviations, width=bar_width, color='green', label='Python')

# Set the x-axis tick labels to the tick_pos list and the x-axis labels to the function_numbers list
plt.xticks(tick_pos, function_numbers)

plt.title(f'Odchylky funkcí CEC 2022, D={dimension}')
ax1.set_xlabel('Číslo funkce')
ax1.set_ylabel('Odchylka C')
ax2.set_ylabel('Odchylka Matlab')
ax3.set_ylabel('Odchylka Python')

ax1.set_yscale('log')
ax2.set_yscale('log')
ax3.set_yscale('log')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

#plt.savefig(f'../2022-D{dimension}.png', dpi=600)

plt.show()