# 1. input the principle, rate and time
#    compute the simple interest and amount
#    SI = ( P x T x R ) / 100
#    Amount = SI + P
#    .......
#    should have (say) functions like this
#    input_data()
#    compute_interest()
#    display_amount()
#    display_simple_interest()

def input_data():
    P=float(input('enter the princilpe: '))
    R=float(input("enter the rate: "))
    T=int(input("enter the time: "))
    return P,R,T
a,b,c=input_data()
def display_simple_interest():
    SI = ( a * b * c ) / 100
    return SI
def display_amount():
    Amount = display_simple_interest() + a
    return Amount
def compute_interest():
    print('SI: ', display_simple_interest())
    print('amount: ',display_amount())
    return compute_interest
compute_interest()


# 3. set1 = { 100, 560,220, 565,121, 10, 15}
#    list1 = [890,560,-220, -565, 12,-10 , 14,22,15]
#    process the set1 , pick the element and search in the list1
#    if the element exists in the list1 (either poistive or negative)
#    example say  10 OR -10 then delete it from the list1
#    count how many got deleted.
#    Once the delete count exceeds 4 then STOP otherwise go ahead and process 
#    the set1


def process():
    set1 = { 100, 560,220, 565,121, 10, 15}
    list1 = [890,560,-220, -565, 12,-10 , 14,22,15]
    set=list(set1)
    c=0
    for i in set:
        num=i-(i*2)
        if num in list1:
            list1.remove(num)
            c=c+1
            if c>=4:
                break
        elif i in list1:
            list1.remove(i)
            c=c+1
            if c>=4:
                break
    print(list1)
    print(c)
    return list1,set1
process()


# 2. given to you a prod_dict = 
#             Price  quantity
#               /    /
#    { 1000: (72.55,10), 2000 : (56.25,5), 3000: (25.25,15) }
#    given prod_name = { 1000: 'Toothpaste', 2000 : 'Soap' , 3000 : 'Campor' }
#    the user is asked to enter the prod name
#    and let say the user inputs Soap
#    then display the amount accordingly
#    also display the quantity available
#    ask the user how much to buy ? if the buying qty inputted is 
#    less than or equal to available qty then go ahead with transaction
#    otherwise display 'Asked qty is NOT available'
#    on transaction being successful deduct the qty accordingly and update
#    Keep doing this till the user say - wish to quit ? YES

def product():
    prod_name = { 1000: 'toothpaste', 2000 : 'soap' , 3000 : 'campor' }
    prod_dict ={ 1000: (72.55,10), 2000 : (56.25,5), 3000: (25.25,15) }
    while True:
        p_name=input("enter the prod_name: ")
        key=item=0
        pn_list=list(prod_name.values())
        if p_name not in pn_list:
            print("product is not avaiable ")
            break       
        for k,v in prod_name.items():           
            if p_name==v:
                key=k
        for i,j in prod_dict.items():
            if key==i:
                item=j 
            prod_dict[i]=list(prod_dict[i])
        quantity=float(input("how much quantity is needed: "))
        if quantity==item[1]:
            print("can i process the bill")
            prod_dict[key][1]=prod_dict[key][1]-quantity
        elif quantity<=item[1] and quantity!=0:
            print("can i process the bill")
            prod_dict[key][1]=prod_dict[key][1]-quantity
        else:
            print("Asked qty is NOT available")
        print(key, ':' ,item)
        print(prod_dict)
        ask=input("do u need any other produce?")
        if ask=='no':
            break
    return product
product()
    
        



