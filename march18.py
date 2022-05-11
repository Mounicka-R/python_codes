## find the frequency of the number 
# data1=[100,250,300,450,125,250,400,300,300,100,250,650]
# ln=len(data1)
# data2=list(set(data1))
# data3=[]
# for i in data1:
#     count=0
#     if i not in data3:
#         for j in data1:
#             if i==j:
#                 count+=1
#                 data3.append(i)
#         if count>1:
#             print(i," ",count)
# print("repeated number in list is:",data3)
# print("unique number in list is:",data2)

## find the frequency of the number 
# data1=[100,250,300,450,125,250,400,300,300,100,250,650]
# freq={}
# for i in data1:
#     v=freq.get(i)
#     if v==None:
#         v=1
#         freq.update({i:v})
#     else:
#         v=v+1
#         freq.update({i:v})
# print(freq)
# for k,v in freq.items():
#     print(k,' ',v) 

## find the person who is getting the highest and lowest salary.
# n=n1=None
# salary=[('sunil',26500),('anil',35000)]
# h=0
# low=99999
# for i in salary:
#     if i[1]>=h:
#         h=i[1]
#         n=i[0]
#     if i[1]<=low:
#         low=i[1]
#         n1=i[0]
# print('highest sal is',h,'drawn by',n)
# print('lowest sal is',low,'drawn by',n1)

## process the data1 and find the total of all the element between 200 to 350 
## and find the average in the range find the highest number.
# data1={125,600,335,444,90,86,120,250,37,89,150,125}
# sum=c=h=0
# for i in data1:
#     if i>=200 and i<=350:
#         sum+=i
#         c+=1
#         if i>h:
#             h=i
# print('total is',sum,'avg is',(sum/c),'highest is',h)

# data2={1000:(12,45,66),2500:(100,37,78,22),3000:(50,60)}
# data3=list(data2.values())
# print(data3)
# sum=c=h=sh=0
# low=sdlow=tlow=9999999
# for i in data3:
#     if i[1]:
#         sum+=i[1]
#         c+=1
#     if i[1]>h:
#         sh=h
#         h=i[1]
#     elif i[1]>sh:
#         sh=i[1]
#     if(i[1]<low):
#         tdlow=sdlow
#         sdlow=low
#         low=i[1]
#     elif(i[1]<low):
#         tdlow=sdlow
#         sdlow=i[1]
#     elif(i[1]<low):
#         tdlow=i[1]
# print('sum',sum)
# print('avg',(sum/c))
# print("highest:",h)
# print('second highest:',sh)
# print('lowest:',low)
# print('second low:',sdlow)
# print('third low:',tdlow)

## add all the values processing data2. find the average.find the second highest and third lowest
# data2={1000:(12,45,66),2500:(100,37,78,22),3000:(50,60)}
# total=c=0
# lst=[]
# for k,v in data2.items():
#     total=total+sum(v)
#     c=c+len(v)
#     for j in v:
#         lst.append(j)
# print(lst)
# slist=sorted(lst)
# print("third lowest",slist[2])
# ln=len(slist)
# print("second highest",slist[ln-2])
# print("total",total,'avg',(total/c))

## process the string and find out how many 'sunil' are there 
## Replace all 'sunil' with 'ganesh kumar'
# main_str='hello how are you doing sunil?how is work sunil?'
# fn='sunil'
# rp='ganesh kumar'
# c=main_str.count(fn)
# pos=0
# for i in range(0,c):
#     r=main_str.index(fn,pos)
#     s1=main_str[:r]
#     s1=s1+rp
#     s2=main_str[r+len(fn):]
#     s1=s1+s2
#     pos=r+1
# print('original string is:',main_str)
# print('new string is:',s1)



## process a file given to you story.txt
## find out how many words are there in that file
## find out how many character are there in the file(excluding the space)
## print the first and last word of the file
# with open("story.txt", "w") as f:
#     f.write("how are you \n")
#     f.write('hi sir \n')
#     f.write('what are you doing?')
# with open("story.txt", "r") as f:
#     a = f.read()
#     lst=a.split(' ') 
# print('number of word are',len(lst))
# print('first word :',lst[0])
# print('last word:',lst[-1])

# c=open('stay.txt','w')
# c.write('good morning \n')
# c.write('how are you')
# c.close()
# c=open('stay.txt','r')
# a=c.read()
# print(a)
# lst=a.split(' ') 
# print('no of word are',len(lst))
# print('first word :',lst[0])
# print('last word:',lst[-1])






