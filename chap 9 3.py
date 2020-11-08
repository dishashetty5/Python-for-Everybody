filename=input("enter a file name: ")
fhand=open(filename)
days={}
for line in fhand:
    if line.startswith("From:"):
        day=line.split()[1]
        days[day]=days.get(day,0)+1
print(days)
