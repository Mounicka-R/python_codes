
# input 6 names and marks
# display the name whose marks is the highest and lowest

h=0
hn=""
low=9999999999
sn=""
for i in range(0,6):
    name=input("enter the name:")
    marks=int(input("entr the marks:"))
    if(marks>h):
        h=marks
        hn=name             
    if(marks<low):
        low=marks
        sn=name
    i=i+1
print("name of the highest marks person:",hn)
print("highest marks obtained is:",h)
print("name of the lowest marks person:",sn)
print("lowest marks obtained is:",low )
