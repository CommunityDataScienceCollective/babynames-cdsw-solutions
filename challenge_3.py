# 3. What is the longest name in the dataset?

import ssadata

maximum_length = 0
longest_names = []

for boys_name in ssadata.boys.keys():
    if len(boys_name ) > maximum_length:
        maximum_length = len(boys_name)
        longest_names = []
        longest_names.append(boys_name)
    elif len(boys_name) == maximum_length:
        longest_names.append(boys_name)

for girls_name in ssadata.girls.keys():
    if len(girls_name) > maximum_length:
        maximum_length = len(girls_name)
        longest_names = []
        longest_names.append(girls_name)
    elif len(girls_name) == maximum_length:
        longest_names.append(girls_name)

print("The longest names in the data set are " + str(maximum_length) + " letters! They are:")

for name in longest_names:
    print(name)


