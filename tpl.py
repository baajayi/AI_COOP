# fname=input("Enter file name: ")
fh=open("mbox-short.txt")
timdict={}
count=None
for line in fh:
    if line.startswith("From "):
        line=line.split()
        hrtime=line[5]
        hrtime=hrtime.split(":")
        hr=hrtime[0]
        timdict[hr]=timdict.get(hr,0)+1
    if count==None or count<timdict[hr]:
        count=timdict[hr]
for key,value in sorted(timdict.items()):
    print(key, value)
# print(timdict)
        