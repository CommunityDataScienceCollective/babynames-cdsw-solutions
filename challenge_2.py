# 2. Are there more boys names or girls names? What about for particular
#    letters? What about for every letter?

import ssadata

num_boys_names = len(ssadata.boys)
num_girls_names = len(ssadata.girls)

print("total boy names: " + str(num_boys_names))
print("total girl names: " + str(num_girls_names))

for letter in "abcdefghijklmnopqrstuvwxyz":
    count_boys = 0
    count_girls = 0
    for name in ssadata.boys.keys():
        first_letter = name[0]
        if first_letter == letter:
            count_boys = count_boys + 1
    
    for name in ssadata.girls.keys():
        first_letter = name[0]
        if first_letter == letter:
            count_girls = count_girls + 1
    
    if count_boys == count_girls:
        print(letter + ": the same number of boys names and girls names")
    elif count_boys > count_girls:
        print(letter + ": more boys names than girls names")
    else:
        print(letter + ": more girls names than boys names")


