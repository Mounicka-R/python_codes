# 1) input any 5 numbers and store in set
#    find the highest number
#    find the lowest number
#    find the avg of all the numbers
#    display the set in DESC order of numbers

# class Number():
#     def store(self):
#         self.number_set=set()
#         c=0
#         while True:
#             self.n=int(input("enter the number: "))
#             c=c+1
#             if c==6:
#                 break
#             else:
#                 self.number_set.add(self.n)
#         print("number set is: ")
#         return self.number_set
#     def highest(self):
#         number_set1=self.number_set
#         h=0
#         for i in number_set1:
#             if i>h:
#                 h=i
#         print("highest number in set is: ")
#         return h
#     def lowest(self):
#         number_set2=self.number_set
#         low=9999999999
#         for i in number_set2:
#             if i<low:
#                 low=i
#         print("lowest number in set is: ")
#         return low
#     def average(self):
#         number_set3=self.number_set
#         avg=sum(number_set3)/len(number_set3)
#         print("average of the set is: ")
#         return avg
#     def descending(self):
#         number_set4=self.number_set
#         sorted(number_set4)
#         print("descending order of the set is: ")
#         return number_set4
# a=Number()
# print(a.store())
# print(a.highest())
# print(a.lowest())
# print(a.average())
# print(a.descending())


# 2) once 1 is working
#    convert the set to the list - call it list1
#    given list2 = [89,23,67,22,100,105,15]
#    process the list2 and add it into the list1
#    in the last 5 elements find the highest
#    in the first 6 elements find the lowest
#    find the avg of all the list1 elements
#    how many numbers are above the avg ?

# class Number():
#     def store(self):
#         self.number_set=set()
#         c=0
#         while True:
#             self.n=int(input("enter the number: "))
#             c=c+1
#             if c==6:
#                 break
#             else:
#                 self.number_set.add(self.n)
#         print("number set is: ")
#         return self.number_set
#     def set_list(self):
#         self.list1=list(self.number_set)
#         list2 = [89,23,67,22,100,105,15]
#         for i in list2:
#             self.list1.append(i)
#         print("list2 is added to list1: ")
#         return self.list1   
#     def highest(self):
#         list2=self.list1
#         last_5_element=list2[-5:]
#         highest_number=max(last_5_element)
#         print("highest value in last 5 element: ")
#         return highest_number
#     def lowest(self):
#         list3=self.list1
#         first_6_element=list3[:6]
#         lowest_number=min(first_6_element)
#         print("lowest value in first 6 element: ")
#         return lowest_number
#     def average(self):
#         list4=self.list1
#         self.avg=sum(list4)/len(list4)
#         print("average of the set is: ")
#         return self.avg
#     def above_average(self):
#         avg1=self.avg
#         list5=self.list1
#         c=0
#         for i in list5:
#             if i>avg1:
#                 c=c+1
#         print("count of number above average in list is: ")
#         return c
# a=Number()
# print(a.store())
# print(a.set_list())
# print(a.highest())
# print(a.lowest())
# print(a.average())
# print(a.above_average())


# 3) st1 = {'Java','Python','C'}
#    st2 = {'SQL','Java','C#','Python'}
#    to the st1 add those elements from st2 which is not there in st1
#    remove the skill 'Java' from both st1, st2
#    add the skills st3 = {'SQLServer','ASP.net','AWS'}
#    into both st1 and st2 using for loop
#    display the st2 in DESC order of sorting

# class Subject():
#     def __init__(self,st1,st2):
#         self.st1 =st1 
#         self.st2 =st2 
#     def add(self):
#         for i in self.st2:
#             if i not in self.st1:
#                 self.st1.add(i)
#         print("added st2 to st1: ",self.st1)
#     def remove_skill(self):
#         self.st1.remove("Java")
#         self.st2.remove("Java")
#         print("updated st1:",self.st1)
#         print("updated st2: ",self.st2)
#     def add_st3(self):
#         set1=self.st1
#         set2=self.st2
#         st3 = {'SQLServer','ASP.net','AWS'}
#         for j in st3:
#             set1.add(j)
#             set2.add(j)
#         print("updated st1 after adding st3 is: ",set1)
#         print("updated st2 after adding st3 is: ",set2)
#     def st2_descending(self):
#         set_2=list(self.st2)
#         set_2.sort(reverse=True)
#         print("st2 in descending order is: ",set_2)
# st1={'Java','Python','C'}
# st2={'SQL','Java','C#','Python'}
# a=Subject(st1,st2)
# a.add()
# a.remove_skill()
# a.add_st3()
# a.st2_descending()


        



