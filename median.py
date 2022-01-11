import csv

with open("c104assign/Weight.csv",newline='') as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
new_data=[]
for i in range(len(data)):
    new_data.append(data[i][2])

new_data.sort()
n=len(new_data)

if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2+1])
    median=(median1+median2)/2
else:
    median=float(new_data[n//2])

print("median is",median)