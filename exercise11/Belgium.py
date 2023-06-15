#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
Belgium_length = ' - ' * len(Belgium)

modified_string = Belgium.replace(',', ':')

fields = modified_string.split(':')
population_belgium = int(fields[1])
population_capital = int(fields[3])
combined_population = population_belgium + population_capital

print(Belgium_length)
print(modified_string)
print('Combined population:', combined_population)
