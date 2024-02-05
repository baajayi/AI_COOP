# fname=input("Enter file name: ")
fh=open("mbox-short.txt")
emdict={}
count=None
for line in fh:
    if line.startswith("From "):
        line=line.split()
        emailadd=line[1]
        emdict[emailadd]=emdict.get(emailadd,0)+1
    if count==None or count<emdict[emailadd]:
        count=emdict[emailadd]
print(emailadd,emdict[emailadd])