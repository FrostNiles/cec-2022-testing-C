import sys
import matplotlib.pyplot as plt
import pandas as pd

dimension = sys.argv[1]
dimension = int(dimension)

def load_deviations(filename, deviations_list):
    with open(filename, 'r') as file:
        result = file.read()
    result = result.split('deviation:')
    deviation = float(result[1])
    deviations_list.append(deviation)
    return deviations_list

data = []
deviations = []
matlab_deviations = []
python_deviations = []
matlab_bigger_than_c = 0
python_bigger_than_c = 0
python_bigger_than_matlab = 0
c_bigger_than_matlab = 0
c_bigger_than_python = 0
matlab_bigger_than_python = 0
matlab_equal_to_python = 0
python_equal_to_c = 0
c_equal_to_matlab = 0
skipped = {}
for i in range(1, 13):
    if i in skipped:
        continue
    for j in [dimension]:
        for k in range(1, j+1):   
            filename = f'test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            matlab = f'../test2022-mat/test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            python = f'../test2022-pyth/test_data/result/result_data_{i}_dim_{j}_number_of_element_{k}.txt'
            deviations = load_deviations(filename, deviations)
            matlab_deviations = load_deviations(matlab, matlab_deviations)
            python_deviations = load_deviations(python, python_deviations)
    for index, (deviation, matlab_deviation, python_deviation) in enumerate(zip(deviations, matlab_deviations, python_deviations)):
        if deviation != matlab_deviation:
            print(index+1)
            if deviation > matlab_deviation:
                c_bigger_than_matlab += 1
                
            else:
                matlab_bigger_than_c += 1
        else:
            c_equal_to_matlab += 1
        if deviation != python_deviation:
            print(index+1)
            if deviation > python_deviation:
                c_bigger_than_python += 1
            else:
                python_bigger_than_c += 1
        else:
            python_equal_to_c += 1
        if matlab_deviation != python_deviation:
            print(index+1)
            if matlab_deviation > python_deviation:
                matlab_bigger_than_python += 1
            else:
                python_bigger_than_matlab += 1
        else:
            matlab_equal_to_python += 1
    print(f"func={i}")
    print("\n")
    
    data.append([
    i, 
    ('+' + str(matlab_bigger_than_c) if matlab_bigger_than_c != 0 else '') + ('/=' + str(c_equal_to_matlab) if c_equal_to_matlab != 0 and matlab_bigger_than_c != 0 else '=' + str(c_equal_to_matlab) if c_equal_to_matlab != 0 else '') + ('/-' + str(c_bigger_than_matlab) if c_bigger_than_matlab != 0 else ''), 
    ('+' + str(python_bigger_than_c) if python_bigger_than_c != 0 else '') + ('/=' + str(python_equal_to_c) if python_equal_to_c != 0 and python_bigger_than_c != 0 else '=' + str(python_equal_to_c) if python_equal_to_c != 0 else '') + ('/-' + str(c_bigger_than_python) if c_bigger_than_python != 0 else ''), 
    ('+' + str(python_bigger_than_matlab) if python_bigger_than_matlab != 0 else '') + ('/=' + str(matlab_equal_to_python) if matlab_equal_to_python != 0 and python_bigger_than_matlab != 0 else '=' + str(matlab_equal_to_python) if matlab_equal_to_python != 0 else '') + ('/-' + str(matlab_bigger_than_python) if matlab_bigger_than_python != 0 else '')
])
    print(f"Matlab bigger than python: {matlab_bigger_than_python}, C bigger than python: {c_bigger_than_python}, C bigger than matlab: {c_bigger_than_matlab}")    
    print(f"Matlab bigger than C: {matlab_bigger_than_c}, Python bigger than C: {python_bigger_than_c}, Python bigger than Matlab: {python_bigger_than_matlab}")    
            
    
    # Compare the three lists
    deviations = []
    matlab_deviations = []
    python_deviations = []
    c_bigger_than_matlab = 0
    c_bigger_than_python = 0
    matlab_bigger_than_python = 0
    python_bigger_than_matlab = 0
    matlab_bigger_than_c = 0
    python_bigger_than_c = 0
    matlab_equal_to_python = 0
    c_equal_to_matlab = 0
    python_equal_to_c = 0




# Create a new figure with a specific size (fullscreen)
fig, ax = plt.subplots(figsize=(14, 10))

# Hide axes
ax.axis('off')

# Create a table and add it to the axes
table = ax.table(cellText=data, colLabels=['Číslo funkce (F*)', 'C/MATLAB', 'C/Python', 'MATLAB/Python'], loc='center', cellLoc = 'center')

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
plt.show()

# Create a DataFrame from your data
df = pd.DataFrame(data, columns=['Číslo funkce (F*)', 'C/MATLAB', 'C/Python', 'MATLAB/Python'])

# Set the first column as index
df.set_index('Číslo funkce (F*)', inplace=True)

# Export the DataFrame to a CSV file
df.to_csv(f'table-2022-{dimension}.csv')
df.to_excel(f'table-2022-{dimension}.xlsx')