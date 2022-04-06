# 1. input a number and check whether the 
#    number is in this range or not
#    157 to 489  (FIRST RANGE)
#    if the number is not in the range then 
#    check whether the number is in this range
#    670 to 978
#    if it is then add 10 to it else add 15 to it
#    if the number is in the FIRST RANGE
#    then raise the number to the power of 3

n= int(input("enter the number: "))
if n>=157 and n<=489:
    print("First Range")
    n=pow(n,3)
    print(n)
else:
    if n>=670 and n<=978:
        if n%4==0:
            n=n+12
            print(n)
        else:
            n=n+10
            print(n)
    else:
        n=n+15
        print(n)

# 2. input the avg of the student
#    and the category say 
#    G - General
#    D - Defence
#    O - Others
#    also input the year of passing 
#    the criteria for admission is as follwing 
#    For G the avg must be above 80 and the 
#    YOP must be 2021
#    For D the avg must be above 68 and the YOP
#    can be 2019 2020 or 2021
#    For O then avg must not be less than 60 and 
#    YOP could be 2020 or 2021


category=input("enter the category: ")
avg=float(input("enter the avg: "))
year=int(input("enter the year: "))
if category=="G":
    if avg>=80 and year==2021:
        print("criteria of admission is satified for General")
    else:
        print("not qualified for General ")  
elif category=="D":
    if avg>=68 and (year==2019 or year==2020 or year==2021):
        print("criteria of admission is satified for Defence")
    else:
        print("not qualified for Defence ")  
elif category=="O":
    if avg>=60 and (year==2020 or year==2021):
        print("criteria of admission is satified for others")
    else:
        print("not qualified for others ")  


# 3. once solution 2 is working as above 
#    then add the following check
#    for the candidate who could not get in the above 

#    if the candidate parents/gurdian income is 
#    less than 80000 pa and they have passed after 2019
#    and thier avg is above 55 then grant admission
#    otherwise no admission

category=input("enter the category: ")
avg=float(input("enter the avg: "))
year=int(input("enter the year: "))
income=float(input("enter the parents/gurdain income: "))
if category=="G":
    if avg>=80 and year==2021:
        print("criteria of admission is satified for General")
    else:
        if income<=80000 and avg>=55 and year>2019:
            print("qualified for General ")  
        else:
            print("not qualified for general")
elif category=="D":
    if avg>=68 and (year==2019 or year==2020 or year==2021):
        print("criteria of admission is satified for Defence")
    else:
        if income<=80000 and avg>=55 and year>2019:
            print("qualified for Defence ")  
        else:
            print("not qualified for Defence ")  
elif category=="O":
    if avg>=60 and (year==2020 or year==2021):
        print("criteria of admission is satified for others")
    else:
        if income<=80000 and avg>=55 and year>2019:
            print("qualified for others ")  
        else:
            print("not qualified for others ")  



