# 1. Enter a name and check whether the 8th element is 
#    vowel or not vowel
#                             |
#    example:  i/p is sanjay kumar
#    handle if the length of the string is small (say less than 8)

name=input("enter the name: ")
if len(name)>=8:
    letter=name[7]
    if letter.lower() in ('a','e','i','o','u') or letter.upper() in ('A','E','I','O','U'):
        print(letter,"is vowel")
    else:
        print(letter, "is not vowel")
else:
    print("entered name length is less than 8 letter")


# 2. enter a sentence
#    enter a word to search in it
#    does the word exists ?
#    if it does how many words are there?
#    which position is the first occurance of the word in the sentence?

sentence=input("enter the sentence: ")
word=input("enter the word to find: ")
count=0
pos=pos1=0
if word in sentence:
    print("word exist in sentence")
    pos=sentence.index(word)
    count=sentence.count(word)
else:
    print("word does not exist in sentence")
print("position of the word in sentence: ",pos)
print("count of word: ",count)


# 3. enter a name 
#    print the name in upper case, lower case  and title case
#    find out how many char are there?

name=input("enter the name: ")
print("upper case name: ",name.upper())
print("lower case name: ",name.lower())
print("title case name: ",name.title())
c=0
for i in name:
    if i.isalpha():
        c=c+1
print("number of char in name is: ",c)

    
# 4. input the mobile number (as string)
#    check whether the last digit of the mobile number is either 5 or 8
#                       |
#    example:  9886612675
#    if the mobile number inputted is not 10 char then display 
#    'INVALID mobile number'

mobile=input("enter the mobile number: ")
mobile1=list(mobile)
if len(mobile1)==10:
    print("entered number is valid")
    if mobile1[-1]=='5' or mobile1[-1]=='8':
        print("last digit of mobile number is: ",mobile1[-1])
    else:
        print("last digit of mobile number is not 5 or 8")
else:
    print("entered mobile number is not valid")


# 5. given a string say
#    name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
#    word1 ='VEENA'
#    find this word1 in name1 irresprective of lower case/upper case
#    how will you solve it?

name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
word1 ='VEENA'
name1=name1.split(",")
flag=True
for i in name1:
    if word1.upper()==i.upper():
        print("word is found",word1)
        flag=False
        break
if flag==True:
    print("not found")


# 6. enter the day, month and year as numbers, one by one
#    dd = 9
#    mn = 12
#    yr = 2020
#    display it is valid date or not
#    valid date rule is 
#    day must be 1 to 31 for any month 1 to 12
#    day must be 1 to 30 if the month is 4,6,9,11
#    day must be 1 to 29 if the year is Leap and the month is 2
#    Leap year rule
#    if the year is not century year like 2004, 1984 , 1996 etc then
#    divide such year by 4, if it is divisible then it is Leap or not
#    leap
#    Non-leap year have 28 days
#    if the year is like 1700, 1800, 1900, 2000 - then they are century
#    year , such year divide by 400 and if it is divisible then it is 
#    leap century year such year will have 29 days in Feb
#    hence 29 2 1800 is invalid
#          29 2 1600 is valid
#          29 2 2000 is valid
#          29 2 1900 is invalid

dd=int(input("enter the date: "))
mn=int(input("enter the month: "))
yr=int(input("enter the year: "))
if mn==1 or mn==3 or mn==5 or mn==7 or mn==8 or mn==10 or mn==12:
    if dd>=1 and dd<=31:
        print("date is valid")
    else:
        print("date is invalid")
elif mn==4 or mn==6 or mn==9 or mn==11:
    if dd>=1 and dd<=30:
        print("date is valid")
    else:
        print("date is invalid")
elif mn==2:
    if dd>=1 and dd<=29:
        if yr%4==0 and yr%100!=0:
            print(dd,'-',mn,'-',yr,"valid")
        elif yr%400==0 and yr%100==0:
            print(dd,'-',mn,'-',yr,"valid")
        else:
            print(dd,'-',mn,'-',yr,"invalid")
else:
    print("date is invalid")            

# 7. given
#    price of LPG for domestic is 950 rs
#    price of LPG for commercail is 1450 rs
#    domestic LPG the user cannot take more than 2 qty
#    commercial LPG the user cannot take more than 6 qty
#    input the category (commercial OR domestic)
#    input the qty (apply the rules) 
#    display the bill amount
#    give discount of 5% is the LPG qty is more than 3 in case of commercial 
#    category

while True:
    category=input('''enter the category domestic or commercial: ''')
    if category=='domestic' or category=='commercial':
        while True:
            try:
                quantity=int(input("enter the quantity: "))
                break
            except:
                print("enter the integer value only")
        bill=bill1=0
        if category=="commercial":
            if quantity<=6:
                price=1450
                bill=price*quantity
                if (quantity>3):
                    bill=bill-(0.05*bill)
                    #Display bill after giving discount  to those who take more than 3qty
                    print("discount commercial LPG bill is: ",bill) 
                elif quantity<=3:
                    #bill for taking less than or equal to 3qty
                    print("commercial LPG bill is: ",bill)  
            else:
                print("commercial LPG quantity is more than 6 so cannot supply")
        elif category=="domestic":
            if quantity<=2:
                price=950
                bill=price*quantity
                print("domestic LPG bill is: ",bill)
            else:
                print("domestic LPG quantity is more than 2 so cannot supply")
        break
    else:
        print("enter the correct category")

# 8. input a number and display one of the following
#    it is a SINGLE digit number ::: if it is 1 to 9
#    it is DOUBLE digit number ::: if it is 10 to 99
#    and so on...
#    do it till SIX digit number
#    if number is above SIX digits then display this number is LARGE number
#    Note
#    if the user inputs a NEGATIVE number then - donot do the above processing
#    instead display :: cannot process NEGATIVE numbers

number=int(input("enter the number: "))
if number>=1 and number<=9:
    print("single digit number")
elif number>=10 and number<=99:
    print("two digit number")
elif number>=100 and number<=999:
    print("three digit number")
elif number>=1000 and number<=9999:
    print("four digit number")
elif number>=10000 and number<=99999:
    print("five digit number")
elif number>=100000 and number<=999999:
    print("six digit number")
else:
    if number<0:
        print("cannot process negative number")
    elif number>=1000000:
        print("number is large")






        
    




