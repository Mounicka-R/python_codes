##1
# sum=h=c=0
# low=99999
# for i in range(0,10):
#     n=int(input("enter the number:"))
#     if n>=100 and n<=999:
#         if n%5==0 and n%7==0:
#             sum=sum+n
#             c=c+1
#     if n>=1000 and n<=9999:
#         if n>h:
#             h=n
#         if n<low:
#             low=n
# print("count of 3digit number div by 5 and 7:",c)
# print("sum of 3digit number div by 5 and 7:",sum)
# print("highest 4digit number:",h)
# print("lowest 4 digit number:",low)



##2
# sum=c=h=count=0
# low=9999999
# num=int(input("how many numbers:"))
# while count<num:
#     n=int(input("enter the number:"))
#     count=count+1
#     if n>=175 and n<=423:
#         pass
#     elif n>=100 and n<=999:
#         if n%5==0 and n%7==0:
#             sum=sum+n
#             c=c+1
#     if n>=1000 and n<=9999:
#         if n>h:
#             h=n
#         if n<low:
#             low=n
# print("count of 3digit number div by 5 and 7:",c)
# print("sum of 3digit number div by 5 and 7:",sum)
# print("highest 4digit number:",h)
# print("lowest 4 digit number:",low)



##3
# n=int(input("enter start point:"))
# n1=int(input("enter stop point:"))
# s=int(input("enter the step:"))
# for i in range(n,n1,s):  # end_point - step
#     print(i,end=' ')
# print()
# for j in range(n1,n+s,-s): #end_point + step
#     print(j,end=' ')




##4
# sentence=input("enter the sentence:")
# word1='success'
# word2='joy'
# word3='vibrant'
# word4='reality'
# print(word1,' ',sentence.count(word1))
# print(word2,' ',sentence.count(word2))
# print(word3,' ',sentence.count(word3))
# print(word4,' ',sentence.count(word4))


##4
# sentence=input("enter the string:")
# word1='success'
# word2='joy'
# word3='vibrant'
# word4='reality'
# c=c1=c2=c3=0
# splits = sentence.split()
# for split in splits:
# 	if split==word1:
# 	    c=c+1
# 	if split==word2:
# 	    c1=c1+1
# 	if split==word3:
# 	    c2=c2+1
# 	if split==word4:
# 	    c3=c3+1
# print(word1," ",c)
# print(word2," ",c1)
# print(word3," ",c2)
# print(word4," ",c3)

# c=0
# for i in range(10,55,8):
#     print(i, end=' ')
#     c+=1
# print()
# i=1
# for j in range(55,10,-7):
#     while i<c:
#         print(j,end=' ')
#         i+=1
#         break


