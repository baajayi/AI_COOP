fname=input("Enter file name: ")
fh=open(fname)
count=0
for line in fh:
    if line.startswith("From "):
        line.split()
        count+=1
        line.split()