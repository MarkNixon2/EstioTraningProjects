years1 = {1977, 1982, 1966}
years2 = {1988, 1977, 1966, 1981}

dif = years2.difference(years1)
print(dif)
# This finds the data that is not in Year1 but is in Year2 so the differences

years2.difference_update(years1)
print(years2)
#This removes all data that is in both sets

years1 = {1977, 1982, 1966}
years2 = {1988, 1977, 1966, 1981}
intersect = years2.intersection(years1)
print(intersect)
#This returns the set of data that exists in both sets

years1.intersection_update(years2)
print(years1)
#This removes all data that is not inculded in both sets

years1 = {1977, 1982, 1966}
years2 = {1988, 1977, 1966, 1981}
supers = years1.issuperset(years2)
print(supers)
#This returns True if all items in the set exists in the original set otherwise it returns false

years1 = {1977, 1982, 1966}
years2 = {1988, 1977, 1966, 1981}
unionss = years1.union(years2)
print(unionss)
#This returns a set that combines both sets data together


