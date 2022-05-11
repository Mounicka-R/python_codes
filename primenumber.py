# use for loop , while loop if need be generate 
# all the PRIME numbers in the given range
#(say)  150 to 646
Number = 150
while(Number <= 646):
    count = 0
    i = 2
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1  




