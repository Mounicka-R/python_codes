# 1.
# names=('uday','shankar','hari','gopal')
# n='gopal'
# name=list(names)
# for i in name:
#     if i==n:       
#         name.remove(n)
# print(name)


# 2.
# data1=(12,45,67,22,44,12,12,89,100)
# ln=len(data1)
# data=set(data1)
# print(data)
# print('unique values is',len(data))


#4.
# data2='kiran,shankar rao,akash,kiran chopra,gopal kamath'
# lit=data2.split(',')
# print(lit)
# lit.sort()
# for i in lit:
#     if i.endswith('a') or i.endswith('n'):
#         print(i)
    

#5.
# empid=(100,250,330,19,671)
# emp_names=['anand','ganesh']
# employ={}
# lent=len(emp_names)
# for i in range(0,lent):
#     employ.update({empid[i]:emp_names[i]})
# print(employ)


#1
# def inp():
#     while True:
#         n=int(input('enter the number:'))
#         if n>999 and n<10000:
#             break
#     return n

# n1=inp()
# n2=inp()
# print('sum',(n1+n2))

#2
# data1=(100,133,-118,-456,667,900,12,55,68)
# data2=['123','566','-588','7809']
# odd=set()
# even=set()
# neg=set()
# for i in data1:
#     if i>0:
#         if i%2==0:
#             even.add(i)
#         else:
#             neg.add(i)
# for j in data2:
#     i=int(j)
#     if i>0:
#         if i%2==0:
#             even.add(i)
#         else:
#             neg.add(i)
# numb_dict={}
# numb_dict.update({'even:':even})
# numb_dict.update({'odd:':odd})
# numb_dict.update({'negative:':neg})
# print(numb_dict)



# def digit_4():
#     n = 0
#     while True:
#         try:
#             n=int(input('enter a 4 digit number '))
#             if n > 999 and n < 10000:
#                 break
#             else:
#                 print ('Please reenter. 4 Digit number ....')
#         except ValueError:
#             print ('Please reenter. ONLY 4 Digit number please....')
#     return n

# print ('-----Main BLOCK start here -----------')
# numb = []


# how = int(input('how many 4 digit numbers you wish to input ? '))
# for i in range(0,how):
#     result = digit_4()
#     print ('well the input is VALID ')
#     numb.append(result)

# print ('total is ',sum(numb))
# print ('-------Main BLOCK ends here ----------')



# Data1 = (100,133,120,125-118,-456,667,900,12,55,68,-500)
# Data2 = ['123','566','-588','7809','Abhijit','A345','666','-777','400','401']
# # seperate the data as ODD , EVEN and NEGATIVE
# even=set()
# odd=set()
# neg=set()
# for i in Data1:
#     if i > 0:
#         if i % 2 == 0:
#             even.add(i)
#         else:
#             odd.add(i)
#     else:
#         neg.add(i)
# print ('processing of Data1 is SUCCESSFUL ')
# for i in Data2:
#     try:
#         i = int(i)
#         if i > 0:
#             if i % 2 == 0:
#                 even.add(i)
#             else:
#                 odd.add(i)
#         else:
#             neg.add(i)
#     except ValueError:
#         pass
# print ('processing of Data2 is SUCCESSFUL ')
# #print ('EVEN ',even)
# #print ('ODD ',odd)
# #print ('NEGATIVE ',neg)
# numb_dict= {}
# numb_dict.update({"EVEN":even})
# numb_dict.update({"ODD":odd})
# numb_dict.update({"NEGATIVE":neg})
# print ('from dictionary ....')
# print (numb_dict)
# print()
# for k,v in numb_dict.items():
#     print (k,' ',v)



