# 6. How many names are subsets of other names?
#
# Note: this problem gets really slow when you consider boys and girls names
# together. For simplicity, I'm treating them separately.

import ssadata

boysNamesSubsets = 0
for boysName in ssadata.boys.keys():
    for otherBoysName in ssadata.boys.keys():
        if boysName in otherBoysName and otherBoysName != boysName:
            boysNamesSubsets = boysNamesSubsets + 1

girlsNamesSubsets = 0
for girlsName in ssadata.girls.keys():
    for otherGirlsName in ssadata.girls.keys():
        if girlsName in otherGirlsName and otherGirlsName != girlsName:
            girlsNamesSubsets = girlsNamesSubsets + 1

print(str(boysNamesSubsets) + " boys names are subsets of other boys names.")
print(str(girlsNamesSubsets) + " girls names are subsets of other girls names.")

