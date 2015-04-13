# 7. Write a program that will take a name as input and return the number of
#    girls and boys with that name.

import ssadata

name = input("Input a name: ")

if name in ssadata.boys.keys():
    print("There are " + str(ssadata.boys[name]) + " boys named " + name)
else:
    print("There are 0 boys named " + name)

if name in ssadata.girls.keys():
    print("There are " + str(ssadata.girls[name]) + " girls named " + name)
else:
    print("There are 0 girls named " + name)

