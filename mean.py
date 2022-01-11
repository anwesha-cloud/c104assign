import csv

with open("c104assign/Weight.csv",newline='') as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
sum=0
for i in range(len(data)):
    sum+=float(data[i][2])

mean=sum/len(data)
print("the sum of the data is",sum)
print("length of data is",len(data))
print("therfore the mean is",mean)