##2
# sum=c=h=0
# low=9999999
# data1=(45,55,[23,66,99],(100,-190),-19,-22,(-89,50,-44))
# for i in data1:
#     if type(i)==int:
#         if (i>=10 and i<=99):
#             sum=sum+i
#             c=c+1
#             if i>h:
#                 h=i
#             if i<low:
#                 low=i
#     elif type(i)==list or type(i)==tuple:
#         for j in i:
#             print(j)
#             if (j>=10 and j<=99):
#                 sum=sum+j
#                 c=c+1
#                 if j>h:
#                     h=j
#                 if j<low:
#                     low=j
# print('total',sum)
# print('avg',(sum/c))
# print('highest',h)
# print('lowest',low)


##3
# data1=[12,55,78,90,25,66,100]
# data2=('ganesh','suresh','mohan','ajay')
# ln=len(data1)
# emp_dict={}
# for i in range(0,len(data2)):
#     emp_dict.update({data1[i]:data2[i]})
# for j in range(len(data2),len(data1)):
#     emp_dict.update({data1[j]:'None'})
# print(emp_dict)
# for k in range(len(data2),len(data1)):
#     emp_dict[data1[k]]='will be assigned later'
# print(emp_dict)

    

# data1=[12,55,78,90,25,66,100]
# data2=('ganesh','suresh','mohan','ajay')
# ln=len(data1)
# emp_dict={}
# for i in range(len(data1)):
#     try:
#         emp_dict.update({data1[i]:data2[i]})
#     except:
#         emp_dict.update({data1[i]:None})
# print(emp_dict)
# for j in range(len(data2),len(data1)):
#     emp_dict[data1[j]]='will be assigned later'
# print(emp_dict)


##1
data1={23,56,'234','A100',True,'Harish','290',12.45,False,'B200'}
data=list(data1)
print(data)
data2=[]
for i in data:
        if type(i)==int:
            data2.append(i)
        if type(i)==float:
            i=int(i)
            data2.append(i)
for j in data:   
    try:
        if type(j)==str:
            j=int(j)
            data2.append(j)
    except ValueError:
        pass
data2.sort()
print(data2)
print('sum of values:',sum(data2))
print('avg:',(sum(data2)/(len(data2))))
print('largest number in the list',data2[-1])
print('lowest value in list',data2[0])



    
