# 5. How many boys names are also girls names? How many girls names are also
#    boys names?

# Note: these are asking the same question! The result from the code below
# should convince you of that.

import ssadata

boysNameAlsoGirlsName = 0
for boysName in ssadata.boys.keys():
    if boysName in ssadata.girls.keys():
        boysNameAlsoGirlsName = boysNameAlsoGirlsName + 1

print("There are " + str(boysNameAlsoGirlsName) + " boys names that are also girls names.")

girlsNameAlsoBoysName = 0
for girlsName in ssadata.girls.keys():
    if girlsName in ssadata.boys.keys():
        girlsNameAlsoBoysName = girlsNameAlsoBoysName + 1

print("There are " + str(girlsNameAlsoBoysName) + " girls names that are also boys names.")


