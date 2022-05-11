d=int(input("enter the day"))
m=int(input("enter the month"))
y=int(input("enter the year"))
leap=0
if(1<=d<=31):
    print("it's valid day")
else:
    print("it's invalid day")
if(1<=m<=12):
    print("it's valid month")
else:
    print("it's invalid month")
if(1000<=y<=3000):
    print("it's valid year")
else:
    print("it's invalid year")
if(1<=d<=31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)):
    print("it valid 31 date")      
elif(1<=d<=30 and (m==4 or m==6 or m==9 or m==11)):
    print("it's valid 30 days")
else:
    print("it's invalid days")
if(m==2):
    print("it's febuary month")
    if(y%100==0 and y%400==0):
        leap=1
        print("it's a leap year")
    elif(y%100!=0 and y%4==0):
        leap=1
        print("it's leap year")
    elif(1<=d<=28):
        print("it's not a leap year")
    else:
        print("it's invalid date because it's not a leap year")
    
             

            
