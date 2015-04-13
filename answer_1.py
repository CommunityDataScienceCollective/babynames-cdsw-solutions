# 1. Search for your own name. Are there both boys and girls that have your
#    name? Is it more popular for one group than for the other?

import ssadata

name = "mako"

if name in ssadata.boys.keys():
    boys_count = ssadata.boys[name]
    print("there were " + str(boys_count) + " boys named " + name)
else:
    boys_count = 0
    print("there were no boys named " + name) 


if name in ssadata.girls.keys():
    girls_count = ssadata.girls[name]
    print("there were " + str(girls_count) + " girls named " + name)
else:
    girls_count = 0
    print("there were no girls named " + name)


if boys_count > girls_count:
    print("there were more boys named " + name + " than girls")
elif boys_count == girls_count:
    print("there were the same number boys and girls named " + name)
else:
    print("there were more girls named " + name + " than boys")
