# 1) display all the numbers as shown
#   -15 -14 -13 -12 -11 -10
#   add all the numbers
#   display the total also (outside the loop)

add=0
for i in range(-15,-9,1):
    print(i,end=" ")
    add=add+i
print("\ntotal of the number:",add)

# 2. input a string and display the following
#    in title case
#    in upper case
#    in lower case
#    in reverse
#    how many char are there in it.

name=input("enter the name: ")
rev=name[::-1]
count=0
for i in name:
    if i.isalpha():
        count=count+1
print("reveresed name: ",rev)
print("upper case name is: ",name.upper())
print("lower case name is: ",name.lower())
print("title of name is: ",name.title())
print("number of character in name is: ",count)

# 3. input a number and display the following way
#    4 7 10 13 16 19 22
#    after that use another for loop and display as below
#    22 17 12 7 2

for i in range(4,23,3):
    print(i,end=' ')
print()
for j in range(22,0,-5):
    print(j,end=' ')

# 4. input a string and display all the char in the second half of the string
#    if input is 
#                 |----->display all from half----->
#    hello bangalore welcome all

string=input("enter the string: ")
st=string[int(len(string)/2):]
print(st)




