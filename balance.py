# Currency denomination are
# GIVEN 2000 500  200 100 50 20 10 5
# input the article price say 880
# customer pays 2000 Rs
# balance is 2000 - 880 =  1120
# 1120 can be paid in what ways ? display like this...
# 500 x 2 =  1000
# 200 x 0 =     0
# 100 x 1 =   100
# 50 x 0 =     0
# 20 x 1 =    20
# 10 x 0 =     0
#     -------------------
#             1120

price=float(input("enter the article price:"))
customer=float(input("enter the customer pay:"))
bal=customer-price
print("balance",bal)
if(bal//500):
    q=int(bal//500)
    r=bal%500
    count=500*q
    print("500 x ",q,'=',count)
    if(r!=0):
        bal=r
if(bal//200):
    q=int(bal//200)
    r=bal%200
    count1=200*q
    print("200 x ",q,'=',count1)
    if(r!=0):
        bal=r
if(bal//100):
    q=int(bal//100)
    r=bal%100
    count2=100*q
    print("100 x ",q,'=',count2)
    if(r!=0):
        bal=r
if(bal//50):
    q=int(bal//50)
    r=bal%50
    count3=50*q
    print("50 x ",q,'=',count3)
    if(r!=0):
        bal=r
if(bal//20):
    q=int(bal//20)
    r=bal%20
    count4=20*q
    print("20 x ",q,'=',count4)
    if(r!=0):
        bal=r
if(bal//10):
    q=int(bal//10)
    r=bal%10
    count5=10*q
    print("10 x ",q,'=',count5)
    if(r!=0):
        bal=r
if(bal//5):
    q=int(bal//5)
    r=bal%5
    count6=5*q
    print("5 x ",q,'=',count6)    
    if(r!=0):
        bal=r