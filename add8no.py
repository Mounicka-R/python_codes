# Input 8 numbers. 
#    add all the numbers, display the total and avg.
#    add the first number and the last number and display the sum
#    display the middle number ie. in the eight it is fourth number which you input
#    if the numbers to input was 11 then 11/2 5.5 rounded to 5 will be the middle
#  number

total=0
count=0
first=0
last=0
middle=0
n=int(input("enter how many number:"))
while count<n:
    a=int(input("enter the number:"))
    if count==0:
        first=a
    if count==n-1:
        last=a
    count=count+1
    if count==int(n/2):
        middle=a
    total=total+a
avg=total/count
sum=first+last
print("sumof values:",total)
print("average values:",avg)
print("sum of first and last value:",sum)
print("middle number:",middle)


