names=["Rajat","Rjt","RajatJain"]
print(names)
print(names[0][-3])
print(names[-2])

names.append("JainRajat")
print(names)
ages=[22,23,25,20]
names.extend(ages)
print(names)
names.remove("Rjt")
print(names)
print(names,ages)
print(len(ages))
print(max(ages))
ages.pop()
print(ages)
