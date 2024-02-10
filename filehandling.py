f=open('file3.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    marks=line.strip().split(',')
    l1=marks[0]
    l2=marks[1]
    l3=marks[2]
    print(f"The marks of student {i} is {l1}")
    print(f"The marks of student {i} is {l2}")
    print(f"Th marks of student {i} is {l3}")
    print( " ")
f.close()