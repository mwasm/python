
import pygal
from die import Die

# Create three D6 dices.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store the results in a list.
results =[]
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies =[]
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice, 1000 times."
x_labels = []
for label in range(3, max_result+1):
    x_labels.append(label)
hist.x_labels = x_labels
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')

print("The die roll results are: ")
print(results)

print("The frequency of each number from 3 to 18 is: ")
print(frequencies)
