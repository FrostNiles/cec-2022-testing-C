import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


skipped = {6,7,8,12}

function_numbers = [i for i in range(1, 13) if i not in skipped]

dimension = 10
number_of_element = 1
deviations = []  # create an empty list to store deviations

# load deviations from files
for i in range(1, 13):
    if i in skipped:
        continue
    with open(f'test_data/result/result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt', 'r') as file:
        contents = file.read()
        if ':' in contents:
            deviation = contents.split(':')[1].strip()  # extract the deviation value
            deviation = float(deviation)
            deviations.append(deviation)  # add the deviation to the list
        else:
            print(f"File result_data_{i}_dim_{dimension}_number_of_element_{number_of_element}.txt does not contain a ':'")
print(deviations)
# I need to extract the deviation value from the string
# Change the format of the y-axis labels


plt.figure(figsize=(10, 6))
plt.bar(function_numbers, deviations, color='blue')

formatter = ticker.FuncFormatter(lambda x, pos: '{:.20f}'.format(x))
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Odchylky funkcí')
plt.xlabel('Číslo funkce')
plt.ylabel('Odchylka')
plt.yscale('log') 
plt.xticks(range(1, 31))

plt.show()