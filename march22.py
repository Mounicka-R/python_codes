##4
# d=['sunjay','vinay']
# vowels='aeiou'
# c=0
# for i in d:
#     new=[]
#     for j in i:
#         if j not in vowels:
#             new.append(j)
#             c+=1
#     print(i,new)
# print(c)

##2
# n=int(input('enter the number:'))
# for i in range(10,0,-1):
#     print(n,'*',i,'=',n*i)

##5
# a=1
# while a%5!=0:
#     a=a+3
# b=1
# while a%2!=b:
#     b=b+a
#     a=a+b
#     break
# print(a,b)

##1
# marks=[]
# count=0
# n=int(input("enter how many number:"))
# while count<n:
#     a=int(input("enter the number:"))
#     count=count+1
#     if count==n+1:
#         break
#     else:
#         marks.append(a)
# print(marks)
# marks.sort()
# print("highest marks",marks[-1])
# print("lowest marks",marks[0])
# sum1=sum2=0
# c1=c2=c=0
# ln=len(marks)
# for i in marks:
#     if i<50 and i>=0:
#         sum1=sum1+i
#         print(i,"student is fail")
#         c1=c1+1
#     elif i>=50 and i<=100:
#         sum2=sum2+i
#         print(i,"student is pass")
#         c2=c2+1
#     elif i==-1:
#         print(i,"student is not present for test")
#         c=c+1
# d=c1+c2+c
# if ln==d:
#     sum=sum1+sum2
# d1=ln-c
# class_avg=sum/d1
# print("sum",sum)
# print("avg",class_avg)

##3
# count=sum=0
# for i in range(200,1945):
#     if i%5==0 and i%6==0 and i%7==0:
#         print(i)
#         count=count+1
#         sum=sum+i
#         if count==10:
#             break
# print('sum:',sum)






# c=0
# for k in range(1,3):
#     name=input("enter the name:")
#     print(name,':',end=" ")
#     for i in name:
#         if  not(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i==' ') :
#             c+=1
#             print(i,end=" ")
#     print()
#     print(c)


# h=sum1=sum2=0
# low=99999
# total=0
# for i in range(0,3):
#     n=int(input("enter the number:"))
#     if n>=50:
#         print("student is pass")
#         sum2=sum2+n
#     elif n<50 and n>0:
#         print("student is fail")
#         sum1=sum1+n
#     elif n==-1:
#         print("student did not attend test") 
#     if n>h:
#         h=n
#     if n<low and n>0:
#         low=n
#     total=sum1+sum2 
# print('total',total)
# print("highest",h)
# print("lowest",low)





