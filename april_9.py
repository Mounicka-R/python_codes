# 2. Display all the numbers in the range say 345 to 590
#    (range could be anything ...)
#    Find out how many numbers are not divisible by 7
#    how many prime numbers are there in that range
#    how many numbers are divisible by BOTH 3 as well as 4
#    add the FIRST and the LAST number of the range and print the sum


# class Number():
#     def __init__(self,n,n1):
#         self.n=n
#         self.n1=n1
#     def range(self):
#         lst=[]
#         for i in range(self.n,self.n1+1):
#             lst.append(i)
#         return lst
#     def div_7(self):
#         c=0
#         lst1=self.range()
#         for j in lst1:
#             if j%7!=0:
#                 c=c+1
#         print("count of number not divisible by 7:")
#         return c
#     def prime_number(self):
#         count=0
#         lst2=self.range()
#         for k in lst2:
#             flag=True
#             for v in range(2,k):
#                 if k%v==0:
#                     flag=False
#                     break
#             if flag==True:
#                 count=count+1
#         print("number of prime number in this range: ")
#         return count
#     def div_3_4(self):
#         div=[]
#         lst3=self.range()
#         for l in lst3:
#             if l%3==0 and l%4==0:
#                 div.append(l)
#         print("number divisible by 3 and 4 is: ")
#         return div
#     def first_last(self):
#         first=0
#         last=0
#         lst4=self.range()
#         first=lst4[0]
#         last=lst4[-1]
#         sum=first+last
#         print("sum of first and last number is: ")
#         return sum
# try:
#     n=int(input("enter the range1: "))
#     n1=int(input("enter the range2: "))
#     if n>n1:
#         n,n1=n1,n
#     a=Number(n,n1)
#     print(a.range())
#     print(a.div_7())
#     print(a.prime_number())
#     print(a.div_3_4())
#     print(a.first_last())
# except ValueError as ve:
#     print("enter integer value only")
# except (TypeError, ZeroDivisionError):
#     print("enter integer value only")
# except IndexError as ie:
#     print("enter the lowest range first")
    
    


# 3. given a list

#    data_1 = [12,-13,-99,155,788,-199,455,-14,23,89,
#               100,49,80,221,-444,120,-333]

#    process the list (use the data_1)
#       add all the 3 digits non-negative numbers
#       find the avg of those numbers
#       how many two digits NEGATIVE numbers are there
#       remove the numbers stored in two variables a=-14 , b=221
#       add the FIRST and the LAST numbers in the list and display the sum
#       convert the list to tuple , iterate and display
#       convert the tuple to the set, iterate and display

# class Data():
#     def __init__(self,data_1):
#         self.data_1=data_1
#     def add(self):
#         count=0
#         sum=0
#         for i in self.data_1:
#             if i>=100 and i<=999:
#                 sum=sum+i
#                 count=count+1
#         print("average of 3 digit number is: ",(sum//count))
#         print("sum of 3 digit number is: ",sum)
#     def digit_2(self):
#         count1=0
#         for j in self.data_1:
#             if j<=-10 and j>=-99:
#                 count1=count1+1
#         print("two digit number in data_1: ",count1)
#     def remove(self):
#         a=-14
#         b=221
#         for k in self.data_1:
#             if k==a:
#                 self.data_1.remove(k)
#             if k==b:
#                 self.data_1.remove(k)
#         print("updated list of data_1: ",self.data_1)     
#     def first_last(self):
#         first=self.data_1[0]
#         last=self.data_1[-1]
#         sum=first+last
#         print("sum of first and last number: ",sum)
#     def convert_list(self):
#         tuple_data=tuple(self.data_1)
#         print("iterated tuple value: ")
#         for l in tuple_data:
#             print(l)
#         print("converted list data to tuple: ",tuple_data)
#     def convert_tuple(self):
#         set_data=set(tuple(self.data_1))
#         print("iterated set value: ")
#         for m in set_data:
#             print(m)
#         print("converted tuple data to set: ",set_data)
# try:
#     data_1 = [12,-13,-99,155,788,-199,455,-14,23,89,100,49,80,221,-444,120,-333]
#     a=Data(data_1)
#     a.add()
#     a.digit_2()
#     a.remove()
#     a.first_last()
#     a.convert_list()
#     a.convert_tuple()
# except (TypeError,ZeroDivisionError):
#     print("only integer value in list is accepted")
# except NameError as ne:
#     print("define the variable first")


# 1. enter the inital meter reading 
#    enter the final meter reading
#    enter D for Domestic or C for commercial
#    ask whether the bill payment is done after the due
#    date ? if yes then Fine is applied else no fine
#    calc
#    for the domestic category - ask whether Solar pannels are there
#    for water heating - if yes then give a discount in the bill of 2%
#    otherwise no discount.

#    Domestic category
#         units
#        1 to 1000     1.90/unit
#      1001 to 2500    2.85/unit
#      2501 ...        4.10/unit
#     fine 5% of the bill amt
 
#     commercial category      
#      1 to 2000       2.25/unit
#     2001 to 5000     3.75/unit
#     5001 to 8000     4.90/unit
#     8001 ...         6.15/unit
#     fine is 10% of the bill amt


# class Meter():
#     def __init__(self,initial,final,category,bill_due):
#         self.initial=initial
#         self.final=final
#         self.category=category
#         self.bill_due=bill_due
#     def category1(self):
#         unit=self.final-self.initial
#         bill=0.0
#         if self.category=="D":
#             self.solar_pannel=input("solar pannel is there or no: ")
#             if unit>=1 and unit<=1000:
#                 bill=unit*1.90
#             elif unit>=1001 and unit<=2500:
#                 bill=unit*2.85
#             elif unit>=2501:
#                 bill=unit*4.10
#             if self.solar_pannel=='yes':
#                 bill=bill-(0.02*bill)
#             if self.bill_due=='yes':
#                 bill=bill+(0.05*bill)
#         elif self.category=="C":
#             if unit>=1 and unit<=2000:
#                 bill=unit*2.25
#             elif unit>=2001 and unit<=5000:
#                 bill=unit*3.75
#             elif unit>=5001 and unit<=8000:
#                 bill=unit*4.90
#             elif unit>=8001:
#                 bill=unit*6.15
#             if self.bill_due=='yes':
#                 bill=bill+(0.10*bill)
#         return bill
# try:
#     initial=float(input("enter the initial meter reading: "))
#     final=float(input("enter the final meter reading: "))
#     category=input("enter the category C for commerical, D for Domestic: ")
#     bill_due=input("bill payed before due date (no) or after due data (yes): ")
#     a=Meter(initial,final,category,bill_due)
#     print(a.category1())
# except ValueError as ve:
#     print("Enter only float value")




        

