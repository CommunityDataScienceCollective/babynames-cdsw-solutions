# 9. Take a prefix as input and print the number of boys and girls with that
#    prefix. (i.e., "m" would list babies whose names start with "m" and "ma"
#    would list babies whose names start with "ma", etc).

import ssadata

prefix = input("Input a prefix: ")

boysNamesWithPrefix = 0
for boysName in ssadata.boys.keys():
    if boysName.startswith(prefix):
        boysNamesWithPrefix = boysNamesWithPrefix + 1

print("There are " + str(boysNamesWithPrefix) + " boys names that start with " + prefix + ".")

girlsNamesWithPrefix = 0
for girlsName in ssadata.girls.keys():
    if girlsName.startswith(prefix):
        girlsNamesWithPrefix = girlsNamesWithPrefix + 1

print("There are " + str(girlsNamesWithPrefix) + " girls names that start with " + prefix + ".")
