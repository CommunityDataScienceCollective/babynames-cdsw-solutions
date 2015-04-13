# 4. How many boys and girls are described in the dataset (i.e., how many boys
#    and girls born in 2013 have names given to at least four others)?

import ssadata

numberOfBoys = 0
for boysName in ssadata.boys.keys():
        numberOfBoys = numberOfBoys + ssadata.boys[boysName]

numberOfGirls = 0
for girlsName in ssadata.girls.keys():
        numberOfGirls = numberOfGirls + ssadata.girls[girlsName]

print("There are " + str(numberOfBoys) + " boys and " + str(numberOfGirls) + " girls in the data set.")

