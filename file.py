# fname=input("Enter file name: ")
fh=open("mbox-short.txt")
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        value=float(line[line.find(":")+2:])
        total+=value
print("Average spam confidence:", total/count)
