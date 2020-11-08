filename=input("enter a file name: ")
fhand=open(filename)
days={}
for line in fhand:
    if line.startswith("From:"):
        day=line.split()[1]
        days[day]=days.get(day,0)+1
largest=None
for key in days:
    if largest is None or days[key]>largest:
        largest=days[key]
        s=key
print(s,largest)
