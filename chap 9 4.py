#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195
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
