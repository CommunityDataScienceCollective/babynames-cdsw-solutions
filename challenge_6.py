# 6. How many names are subsets of other names?
#
# Note: this problem gets really slow when you consider boys and girls names
# together. For simplicity, I'm treating them separately.

import ssadata

boysNamesSubsets = 0
for boysName in ssadata.boys.keys():
    match = False
    for otherBoysName in ssadata.boys.keys():
        if not match and boysName in otherBoysName and otherBoysName != boysName:
            boysNamesSubsets = boysNamesSubsets + 1
            match = True

print(str(boysNamesSubsets) + " boys names are subsets of other boys names.")

girlsNamesSubsets = 0
for girlsName in ssadata.girls.keys():
    match = False
    for otherGirlsName in ssadata.girls.keys():
        if not match and girlsName in otherGirlsName and otherGirlsName != girlsName:
            girlsNamesSubsets = girlsNamesSubsets + 1
            match = True

print(str(girlsNamesSubsets) + " girls names are subsets of other girls names.")

