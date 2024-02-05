fname=input("Enter File name: ")
fh=open(fname)
read_list=[]
for line in fh:
    line=line.rstrip().split()
    for a in line:
        if a not in read_list:
            read_list.append(a)

read_list.sort()

print(read_list)
