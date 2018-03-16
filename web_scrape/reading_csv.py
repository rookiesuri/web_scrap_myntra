import csv
f=open('input_list_kurtas.csv')
z=csv.reader(f,delimiter=',')

x=[]
for rows in z:
    x.append(rows)

for l in x:
    print l

print len(x)
