#  Given the price list 
#    1) Tea/Coffee     Rs 15 per cup
#    2) Snacks type I  Rs 30 per plate
#    3) Snacks type II Rs 42 per plate
#    4) Executive Meals Rs 85 per plate
#    5) Spl Meals       Rs 120 per plate
#    ask the user what is needed
#    The input can be like this
#    item the user will type the item number : then qty required and so on
#    finally :B means Bill the items ordered
#    no. item no.
#    |   | 
#    2:3:1:4:B
#      |   |
#      |  how much qty
#      |  needed 
#     how much 
#     qty
   
#    At that time the bill should be generated
  
#    store the customer mobile number and the bill amount in the set
#    like this (just shown the set contains tuple)
#    Also ask the customer catg which could be D for Defence S for Sr Citizen
#    if it neither then he/she is regular customer.
#    'D' means the customer is Defence personel and they get 10% discount on the bill
#    'S' means the customer is Senior Citizen and they get 4% discount on the bill
#                 tuple             tuple              tuple
#    hotel = { (9667789090,350),(9131402245,450,'D'),(9131402666,225,'S') }
#    Keep on inputing and storing in the tuple and then into the set till the user says
#    EXIT to stop
#    then iterate the set and display the ouput like this....
#    Mob No.    Bill amt   Customer catg
#    9667789090  350        Regular
#    9131402245  450        Defence
#    9131402666  225        Sr. Citizen
#    ....

total_bill=0
y=0
bill,bill1,bill2,bill3,bill4=0,0,0,0,0
ph_no=set()
y=set()
cat=set()

while True:
    while True:
        itemno=int(input("enter the item.no:"))
        quant=float(input("enter the quantatity:"))
        if(itemno==0 and quant==0):
            break
        if(itemno==1):
            price=15 
            bill=quant*price
            print("coffe/tea per cup price is:",price)
        if(itemno==2):
            price1=30
            bill1=quant*price1
            print("Snacks type I per plate price is:",price1)
        if(itemno==3):
            price2=42
            bill2=quant*price2
            print("Snacks type II per plate price is:",price2)
        if(itemno==4):
            price3=85
            bill3=quant*price3
            print("Executive Meals per plate price is:",price3)
        if(itemno==5):
            price4=120
            bill4=quant*price4
            print("Spl Meals per plate price is:",price4)
            
    total_bill=(bill+bill1+bill2+bill3+bill4)   
    ph_no=input("enter the ph_number:")
    if(len(ph_no)==10):
        print("enter ph_no is valid")
    else:
        print("enter ph_no is invalid")
    cat=input("enter the category:")
    if(cat=="d"):
        y=total_bill-(total_bill*0.10)
        print("10 percentage discount on the bill as he/she is defence person:",y)
    elif(cat=="s"):
        y=total_bill-(total_bill*0.04)
        print("4 percentage discount on bill as he/she is Senior Citizen:",y)
    elif(cat=="regular"):
        y=total_bill
        print("he/she is regular customer",y)
    print(ph_no)
    print("itemno1 bill:",bill) 
    print("itemno2 bill:",bill1)
    print("itemno3 bill:",bill2)
    print("itemno4 bill:",bill3)
    print("itemno5 bill:",bill4)
    print("Total bill amount:",total_bill)
    hotel_bill={}
    hotel_bill.update({'ph_no:':ph_no})
    hotel_bill.update({'y:':y})
    hotel_bill.update({'cat:':cat})
    print(hotel_bill)
    
    c=input("enter exit to quit:")
    if(c=='exit'):
        break
    