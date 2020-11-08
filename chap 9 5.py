filename=input("enter a file name: ")
fhand=open(filename,'r')
days={}
for line in fhand:
    if line.startswith("From:"):
        day=line.split()[1]
        n=day.split("@")[1]
        days[n]=days.get(n,0)+1
print(days)
