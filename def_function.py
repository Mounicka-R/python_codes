# 1) create user defined function to do the following:
#    ask the user the cost price of the article
#    ask the category of the article
#    which could be :-
#     A   then the profit percentage is 8%
#     B   then the profit percentage is 6.5%
#     C   then the profit percentage is 5.5%
#    selling price = cost price + (cost price * profit percentage)

def selling_price(cost_price,category):
    if category=='A':
        profit_percentage=8/100
    elif category=='B':
        profit_percentage=6.5/100
    elif category=='C':
        profit_percentage=5.5/100
    selling_price1=cost_price+(cost_price * profit_percentage)
    return selling_price1
cost_price=float(input("enter the cost of the arcticle:"))
category=input("""enter the category:
A. profit percentage 8%
B. profit percentage 6.5%     
C. profit percentage 5.5%\n""")
print(selling_price(cost_price,category))


# 2) input names till the user types STOP to EXIT
#    add the names to the set
#    if the name inputted already exist then display the 
#    message as the name is already there hence NOT added again
#    process how many names have Kumar or Rao as surname
#    remove the following people name lets say it is provided in a '
#    another set rem_name={'Ashok','Lalit','Pankaj','Anand','Asha','Usha'}
#    how many names were removed from the name set you created

def name():
    names=set()
    c=0
    rem_name={'Ashok','Lalit','Pankaj','Anand','Asha','Usha'}
    Found=0
    while True:
        name = input("Enter the name : ")
        if name == "STOP":
            break
        elif name in names:
            print("name is already there hence NOT added again")
        else:
            if 'kumar' in name.split(" ") or 'rao' in name.split(" "):
                c=c+1
            if name not in rem_name:
                names.add(name)
            else:
                Found=Found+1
    print(names)
    print('how many kumar and rao is present:',c)
    print("how many is remove from names set: ",Found)
name()

# 3) create a dict called prod
#    which has key prod_id and prod_name and price are the values
#    as shown below
#    prod = { 1000: ['Laptop',55000], 2000: ['Mouse',1500],....}
#    add the prod id and the prod details in a list of prod info
#    the flow should be like this
#    enter the prod id?
#    check if the prod id exists?
#    NO not existing - then input the prod name and price and add them to 
#    a list
#    that list is added as the value for the corresponding key in the dict
#    YES - existing - then display the message that the prod id already exists
#    finally when done with adding then find out
#    the follwing details :-
#    prod details - which is the costliest item
#    prod details - which is the cheapest item
#    how many products are above the rate of 12500?

def prod_key_value():
    prod={}
    while True:
        prod_id=int(input('enter the prod_id:'))
        if prod_id==0:
            break
        elif prod_id in prod:
            print("enter the invalid prod_id")
        elif prod_id  not in prod:
            prod_name=input("enter the prod_name:")
            price=float(input("enter the price:"))
            prod.update({prod_id:[prod_name,price]})
    p_price=[]
    p_name=[]
    c=0
    for k,v in prod.items():
        p_price.append(v[1])
        p_name.append(v[0])
    for i in p_price:
        if i>=12500:
            c=c+1
    p_price_max=max(p_price)
    p_price_min=min(p_price)
    if p_price_max in p_price:
        pos_price=p_price.index(p_price_max)
        name=p_name[pos_price]
    if p_price_min in p_price:
        pos_price1=p_price.index(p_price_min)
        name1=p_name[pos_price1]
    print(p_price)
    print(p_name)
    print("the costliest item is ",name, ':' ,p_price_max)
    print("the cheapest item is ",name1, ':',p_price_min)
    print("how many products are above the rate of 12500?: ",c)
    return prod
print(prod_key_value())


