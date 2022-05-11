# 3. Store 'n' names in the a set (till the user types STOP), 
#    sort the name set 
#    how many names are there which starts from R to U
#    display the last 2 char of the names from the set (use SLICING)
#    How many names are there with Last name
#    say the name can be Ravi Rao, Anish Kamath, Uday , Rashmi Bhat etc...

# class Names():
#     def set_name(self):
#         name_set=set()
#         while True:
#             self.name=input("enter the name: ")
#             if len(self.name.split(" "))>1:
#                 num=""
#                 for i in self.name.split(" "):
#                     num=num+i
#                 # print("num=",num)
#                 if num.isalpha():
#                     if self.name=="STOP":
#                         break
#                     else:
#                         name_set.add(self.name)   
#                 else:
#                     print('enter the alphabet only')
#             else:
#                 if self.name.isalpha():
#                     if self.name=="STOP":
#                         break
#                     else:
#                         name_set.add(self.name)   
#                 else:
#                     print('enter the alphabet only')
#         return name_set  
#     def sort_value(self):
#         set1=self.set_name()
#         self.list1=list(set1)
#         self.list1.sort()
#         print("sorted name list is: ",self.list1)
#     def name_starts(self):
#         self.list2=self.list1
#         c=0
#         for i in self.list2:
#             if i.startswith("R") or i.startswith("S") or i.startswith("T") or i.startswith("U") or i.startswith("r") or i.startswith("s") or i.startswith("t") or i.startswith("u"):
#                 c=c+1
#         print("names startswith r,s,t,u are: ",c)
#     def last_2_char(self):
#         self.list3=self.list1
#         for j in self.list3:
#             print("last two char of the names: ",j[-2:])  
#     def surename(self):
#         self.list4=self.list1
#         c1=0
#         for k in self.list4:
#             lst4=k.split(" ")
#             if len(lst4)>1:
#                 c1=c1+1     
#         print("count of surname in the set: ",c1)         
# a=Names()
# a.sort_value()
# a.name_starts()
# a.last_2_char()
# a.surename()



# 2) have any text file (motivational.txt) , 
#    created in notepad having few sentences
#    say this one....
#    *******
#    Sudha Murthy was hardworking and determined to succeed in her studies, 
#    which is why she emerged a topper in both her undergraduate and 
#    postgraduate studies. After graduation, Sudha Murthy was hired by 
#    TATA Engineering and Locomotive Company, also known as TELCO, 
#    and she was the first female engineer in the company.
#    At every stage in our lives, we come across immense challenges and 
#    various forms of discrimination. But that should not discourage 
#    us from performing our best. We should be determined and 
#    strive to achieve success despite the obstacles we 
#    face in life. And we should have the courage to fight and 
#    eradicate policies that may stifle the growth of our country. 
#    These are some of the lessons that we can learn from Sudha Murthy.
#    ************* 
#    open that file , find out how many words are there 
#    which word is having the max length (there can be many words of the same length)
#    have ALL those words
#    Display the LAST 10 words from the file

# class Word():
#     def read_file(self):
#         f=open("motivational.txt","r")
#         f1=f.read()
#         print(f1)
#         words=f1.split(" ")
#         print("number of words in the file: ",len(words))
#         c=0
#         max_len = len(max(words, key=len))
#         for word in words:
#             if len(word) == max_len:
#                 print("Longest word in the file: ",word)
#                 c=c+1
#         print("Maximum length word in this file: ",c)
#         print("Last 10 words from the file is: ",words[-10:])
# a=Word()
# a.read_file()

# 1) given
#   prod = { 100 : ['Laptop',45550,True], 200 : ['Mouse',2000,False] }
#   key is 100
#   value is list describing the item name, price and True indicates
#   available in store, False not available
#   write a function to add more products till the user type -1 to stop
#   write a function display_all to iterate and display all the items
#   which are AVAILABLE in the store
#   write a function display_item which accepts the item code and if that
#   item exists then display the details and if the item code is not there
#   display ITEM not found
#   have a function called item_not_available which has a dict
#   by name itm_not_in store = { } which holds all the items with the 
#   status False
#   the code should be menu driven.....
#   1. Add
#   2. Display all
#   3. display specific item
#   4. Move item NOT avialable
#   5. E X I T out of menu
#   enter your choice .....


# class Product():
#     def add(self):
#         self.prod={}
#         while True:
#             self.item_id=int(input("enter the key_id: "))
#             if self.item_id==-1:
#                 break
#             elif self.item_id in self.prod:
#                 print("enter the invalid key_id")
#             elif self.item_id not in self.prod:
#                 self.prod_name=input("enter the prod_name: ")
#                 self.price=float(input("enter the float price: "))
#                 self.true_indicator=input("enter true for avaiable false for not avaiable: ") 
#                 self.prod.update({self.item_id:[self.prod_name,self.price,self.true_indicator]})
#         print("prod",self.prod)
#     def display_all(self):
#         prod1=self.prod
#         for i,j in prod1.items():
#             if j[2]=='True':
#                 print("item_id avaiable in store: ",i)
#                 print("item detail avaiable in store: ",j)
#     def display_specific_item(self):
#         prod2=self.prod
#         self.user_item_id=int(input("enter the item id for the required item: "))
#         self.item_not_found=[]
#         if self.user_item_id in prod2:
#             print(prod2[self.user_item_id])
#             print("item is avaiable ")
#         else:
#             self.item_not_found.append(self.user_item_id)
#             print("item not found")
#         print("item not found in list: ",self.item_not_found)
#     def move_item_not_avaiable(self):
#         prod3=self.prod
#         for i,j in prod3.items():
#             if j[2]=='False':
#                 print("item_id not avaiable in store: ",i)
#                 print("item detail not avaiable in store: ",j)  
#     def menu(self):
#         while True:
#             self.enter=input(''' 1. Add
#   2. Display all
#   3. display specific item
#   4. Move item NOT avialable
#   5. E X I T out of menu
#   enter your choice .....''')
#             if self.enter=='1':
#                 self.add()
#             if self.enter=='2':
#                 self.display_all()
#             if self.enter=='3':
#                 self.display_specific_item()
#             if self.enter=='4':
#                 self.move_item_not_avaiable()
#             if self.enter=='5': 
#                 break        
# a=Product()
# a.menu()





