# 1. enter a string say Indian Administrative Service
#    o/p should be IAS
#    hint use split, list to do this.
#    Note if the string is one word - Hello
#    then o/p should be Hello

# string=input("enter the string:")
# l=string.split(" ")
# for i in range(len(l)):
#     if len(l)==1:
#         print(string)
#     else:
#         p=(l[i][:1])
#         p1=p.upper()
#         print(p1,end="")



# a=input("enter the string:")
# l=a.split(" ")
# if len(l)==1:
#     if a.isalpha():
#         print(a)
# else :
#     for i in l:
#         if i.isalpha():
#             print(i[0].upper(),end='')


# 2. use dict for this , OOPS concept should be implemented
#    here
#    input roll,name,avg. roll is the Key and value
#    is name,avg and result - say as list
#    compute the result based on avg as following :
#    1-39 - Fail
#    40-49 - Pass
#    50-59 - Second class
#    60-74- First class
#    75-89 - distinction
#    90 and above - High Distinction
#    have methods like 
#    input_data()
#    process_avg()
#    display_all_details()
#    etc
#    Find out how many candidates secures more than class
#    avg.
#    display the student details who has highest and second highest
#    avg

# def input_data():
#     dict={}
#     while True:
#         roll=int(input("enter the roll number: "))
#         name=input("enter the name: ")
#         avg=float(input("enter the avg: "))
#         if roll==0:
#             break
#         else:
#             dict.update({roll:[name,avg]})
#     print(dict)
#     avg1=[]
#     nm=[]
#     for v in dict.values():
#         avg1.append(v[1])
#         nm.append(v[0])
#     return avg1,nm
# a,b=input_data()
# def process_data():
#     for i in a:
#         if i>=1 and i<=39:
#             print(i,":" ,"fail")
#         if i>=40 and i<=49:
#             print(i,":","pass")
#         if i>=50 and i<=59:
#             print(i,":","second class")
#         if i>=60 and i<=74:
#             print(i,":","first class")
#         if i>=75 and i<=89:
#             print(i,":","distinction")
#         if i>=90:
#             print(i,":","high distinction")
#     return i 
# result=process_data()
# a.sort()
# print("the student details who has highest score: ",max(a))
# print("the second highest is: ",a[len(a)-2])
# average=(sum(a)/len(a))
# c=0
# for i in a:
#     if i>average:
#         c=c+1
# print("more than class avg: ",c)




# 3. Once 2 is working, make changes to accomodate this..
#    if the avg inputted as NEGATIVE then
#    such avg is ignored as the candidate is considered 
#    as ABSENT for the exam
#    handle this scenario


# def input_data():
#     dict={}
#     while True:
#         roll=int(input("enter the roll number: "))
#         name=input("enter the name: ")
#         avg=float(input("enter the avg: "))
#         if roll==0:
#             break
#         else:
#             dict.update({roll:[name,avg]})
#     print(dict)
#     avg1=[]
#     for v in dict.values():
#         if v[1]>0:
#             avg1.append(v[1])
#     return avg1
# a=input_data()
# def process_data():
#     for i in a:
#         if i>=1 and i<=39:
#             print("fail")
#         if i>=40 and i<=49:
#             print("pass")
#         if i>=50 and i<=59:
#             print("second class")
#         if i>=60 and i<=74:
#             print("first class")
#         if i>=75 and i<=89:
#             print("distinction")
#         if i>=90:
#             print('high distinction')
#         if i<0:
#             print("student didnot attend the test")
#     return i 
# result=process_data()
# a.sort()
# print("the student details who has highest score: ",max(a))
# print("the second highest is: ",a[len(a)-2])
# average=(sum(a)/len(a))
# c=0
# for i in a:
#     if i>average:
#         c=c+1
# print("more than class avg: ",c)





