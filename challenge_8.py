# 8. What is the most popular girls name that is also a boys name?

import ssadata

mostPopularName = ""
mostPopularNameCount = 0

for girlsName in ssadata.girls.keys():
    if girlsName in ssadata.boys.keys() and ssadata.girls[girlsName] > mostPopularNameCount:
        mostPopularNameCount = ssadata.girls[girlsName]
        mostPopularName = girlsName

print("The most popular girls name that is also a boys name is " + mostPopularName + ", with " + str(mostPopularNameCount) + " girls.")
print("There were also " + str(ssadata.boys[mostPopularName]) + " boys named " + mostPopularName + ".")

