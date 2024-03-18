my_set = { 122,234,3455,445,52}
print(my_set)
my_set.add(234)
print(my_set)
my_set.update([121,12,121])
print(my_set)
my_set2 = my_set.copy()
print(my_set)
print(len(my_set))
my_set.discard(234)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))
names = {"John", "Smith", "Andrew" ,"Peter"}
if "Andrew" in names :
    print("Andrew is present in the school system")
else:
    print("Andrew is not present present in the school system")
Parents = { "MBugua","Otieno", "Cheptoo","Wafula"}
one_value = "Otieno"
if one_value in Parents:
    output = one_value
    print(output)
Radio_stations ={100,88.5,96.4,80}
Radio1 = 88.5
if Radio1 in Radio_stations:
    Channel = Radio1
    print(Radio1)