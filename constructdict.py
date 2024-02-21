cities = {'Delhi':'INDIA','LONDON':'UK','Manchester':'UK','Paris':'France','Indoor':'INDIA','Seoul':'Korea'}
d={}
for c in cities:
    if cities[c] in d:
        d[cities[c]].append(c)
    else:
        d[cities[c]]=[c]

print(d)