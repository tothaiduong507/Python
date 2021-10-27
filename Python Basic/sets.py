
#Set= collection which is unordered, unindexed. No duplicate data

utensils={"fork","spoon","knife","knife"}
dishes={"bowl","plate","cup"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
dinner_table = utensils.union(dishes)
utensils.update(dishes)

print(utensils.difference(dishes))
for x in utensils:
    print(x)
for i in dinner_table:
    print(i)



