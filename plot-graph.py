import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys
import math 
import pandas as pd
skipped = {}

function_numbers = [i for i in range(1, 13) if i not in skipped]

dimension = dimension
dimension = dimension
number_of_element = number_of_element
number_of_element = int(number_of_element)

deviations = []  # create an empty list to store deviations
matlab_deviations = []  # create an empty list to store deviations
python_deviations = []
data = []
matlab_data = []
python_data = []


# load deviations from files
for i in range(1, 13):
    if i in skipped:
        continue
    with open(f'test_data/result/result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
        contents = file.read()
        if ':' in contents:
            deviation = contents.split(':')[1].strip()
            deviation = float(deviation)
            if deviation == math.inf:
                deviation = 10e12
            deviations.append(deviation)
            if deviation == 10e12:
                deviaton = math.inf
            data.append([i, deviation])

        else:
            print(f"File result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt does not contain a ':'")
    
    with open(f'../test2022-mat/test_data/result/result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
        contents = file.read()
        if ':' in contents:
            deviation = contents.split(':')[1].strip()
            deviation = float(deviation)
            if deviation == math.inf:
                deviation = 10e12
            matlab_deviations.append(deviation)
            if deviation == 10e12:
                deviaton = math.inf
            matlab_data.append([i, deviation])
        else:
            print(f"File result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt does not contain a ':'")
    
    with open(f'../test2022-pyth/test_data/result/result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
        contents = file.read()
        if ':' in contents:
            deviation = contents.split(':')[1].strip()
            deviation = float(deviation)
            if deviation == math.inf:
                deviation = 10e12
            python_deviations.append(deviation)
            if deviation == 10e12:
                deviaton = math.inf
            python_data.append([i, deviation])
        else:
            print(f"File result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt does not contain a ':'")
    



fig, ax = plt.subplots(figsize=(15, 10))

# Define the width of a bar
bar_width = 0.2

# Positions of the left bar-boundaries
bar_l = [i + 1 for i in range(len(function_numbers))]

# Positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i + (bar_width / 2) for i in bar_l]

# Create the bar plot for the first set of data
ax.bar(bar_l, deviations, width=bar_width, color='blue', label='C')

# Create the bar plot for the second set of data
ax.bar([p + bar_width for p in bar_l], matlab_deviations, width=bar_width, color='red', label='Matlab')

# Create the bar plot for the third set of data
ax.bar([p + 2*bar_width for p in bar_l], python_deviations, width=bar_width, color='green', label='Python')

# Set the x-axis tick labels to the tick_pos list and the x-axis labels to the function_numbers list
plt.xticks(tick_pos, function_numbers)

plt.title(f'Odchylky funkcí CEC 2022, D={dimension}', fontsize=18)
ax.set_xlabel('Číslo funkce', fontsize=14)
ax.set_ylabel('Odchylka', fontsize=14)

ax.set_yscale('log')

# Create a unified legend for all three datasets
ax.legend(loc='upper right', fontsize='x-large')

plt.savefig(f'./test_data/graph-results/2022-D{dimension}-E{number_of_element}.png', dpi=600, bbox_inches='tight')

plt.clf()
#plt.show()


# Create a new figure with a specific size (fullscreen)
fig, ax = plt.subplots(figsize=(14, 10))

# Hide axes
ax.axis('off')

# Create a table and add it to the axes
table = ax.table(cellText=data, colLabels=['Číslo funkce (F*)', 'deviation'], loc='center', cellLoc = 'center')

# Scale the cells' size
table.scale(1, 2)

# Center the data in the cells
table.auto_set_font_size(False)
table.set_fontsize(10)
for key, cell in table.get_celld().items():
    cell.set_linewidth(1)  # Add border to cells
    cell.set_fontsize(14)
    cell.set_text_props(ha='center')

# Make the first row and column bold
for i in range(len(data[0])):
    table[(0, i)].set_fontsize(14)
    table[(0, i)].set_text_props(weight='bold', color='k')
for i in range(len(data)+1):
    table[(i, 0)].set_fontsize(14)
    table[(i, 0)].set_text_props(weight='bold', color='k')

# Save the figure in fullscreen
#plt.savefig(f'table-2022-{dimension}.png', dpi=600, bbox_inches='tight', bbox_extra_artists=[table])

# Show the plot
#plt.show()

# Create a DataFrame from your data
df = pd.DataFrame(data, columns=['Číslo funkce (F*)', 'deviation'])

# Set the first column as index
df.set_index('Číslo funkce (F*)', inplace=True)

# Export the DataFrame to a CSV file
df.to_csv(f'./test_data/table-results/C/table-2022-{dimension}-{number_of_element}.csv')

# Create a new figure with a specific size (fullscreen)
fig, ax = plt.subplots(figsize=(14, 10))

# Hide axes
ax.axis('off')

# Create a table and add it to the axes
table = ax.table(cellText=matlab_data, colLabels=['Číslo funkce (F*)', 'deviation'], loc='center', cellLoc = 'center')

# Scale the cells' size
table.scale(1, 2)

# Center the data in the cells
table.auto_set_font_size(False)
table.set_fontsize(10)
for key, cell in table.get_celld().items():
    cell.set_linewidth(1)  # Add border to cells
    cell.set_fontsize(14)
    cell.set_text_props(ha='center')

# Make the first row and column bold
for i in range(len(matlab_data[0])):
    table[(0, i)].set_fontsize(14)
    table[(0, i)].set_text_props(weight='bold', color='k')
for i in range(len(matlab_data)+1):
    table[(i, 0)].set_fontsize(14)
    table[(i, 0)].set_text_props(weight='bold', color='k')

# Save the figure in fullscreen
#plt.savefig(f'table-2022-{dimension}.png', dpi=600, bbox_inches='tight', bbox_extra_artists=[table])

# Show the plot
#plt.show()

# Create a DataFrame from your data
df = pd.DataFrame(matlab_data, columns=['Číslo funkce (F*)', 'deviation'])

# Set the first column as index
df.set_index('Číslo funkce (F*)', inplace=True)

# Export the DataFrame to a CSV file
df.to_csv(f'./test_data/table-results/matlab/table-2022-{dimension}-{number_of_element}.csv')


# Create a new figure with a specific size (fullscreen)
fig, ax = plt.subplots(figsize=(14, 10))

# Hide axes
ax.axis('off')

# Create a table and add it to the axes
table = ax.table(cellText=python_data, colLabels=['Číslo funkce (F*)', 'deviation'], loc='center', cellLoc = 'center')

# Scale the cells' size
table.scale(1, 2)

# Center the data in the cells
table.auto_set_font_size(False)
table.set_fontsize(10)
for key, cell in table.get_celld().items():
    cell.set_linewidth(1)  # Add border to cells
    cell.set_fontsize(14)
    cell.set_text_props(ha='center')

# Make the first row and column bold
for i in range(len(python_data[0])):
    table[(0, i)].set_fontsize(14)
    table[(0, i)].set_text_props(weight='bold', color='k')
for i in range(len(python_data)+1):
    table[(i, 0)].set_fontsize(14)
    table[(i, 0)].set_text_props(weight='bold', color='k')

# Save the figure in fullscreen
#plt.savefig(f'table-2022-{dimension}.png', dpi=600, bbox_inches='tight', bbox_extra_artists=[table])

# Show the plot
#plt.show()

# Create a DataFrame from your data
df = pd.DataFrame(python_data, columns=['Číslo funkce (F*)', 'deviation'])

# Set the first column as index
df.set_index('Číslo funkce (F*)', inplace=True)

# Export the DataFrame to a CSV file
df.to_csv(f'./test_data/table-results/python/table-2022-{dimension}-{number_of_element}.csv')