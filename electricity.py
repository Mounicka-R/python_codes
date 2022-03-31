# Given the electricity bill rates 
# input the initial meter reading
# input the final meter reading
# input the category
# final - initial is the unit consumed, based on that calculate the 
# bill. ONLY In domestic catg if the residence has Solar installation then
# give 10% discount on the bill which is above 2000/-

# for Domestic catg
# 0 to 1000    1.75 per unit 
# 1001 to 2500	  2.50 per unit 
# 2501 to 4500   3.70 per unit 
# 4501 onwards   5.25 per unit

# for Commercial catg
# 0 to 2200    2.75 per unit 
# 2201 to 4500	  3.75 per unit 
# 4501 to 7000   4.90 per unit 
# 7001 onwards   6.40 per unit
# add 15.5% GST for the bill generated.
# in commercial catg if the unit consumed is above 8000 then put a fine amount of
# 5% on the bill amount after computing the GST.



initial=float(input("enter the initial meter reading:"))
final= float(input("enter the final meter reading:"))
category=input("enter the category:")
residence=input("solar installion:")
unit= final - initial
a=0
b=0
dunit=0
fine=0
if (category=="domestic"):
    if(0<=unit<=1000):
        a=unit*1.75
    if(1001<=unit<=2500):
        a=unit*2.50
    if(2501<=unit<=4500):
        a=unit*3.70
    if(unit>4501):
        a=unit*5.25
    if(residence=="yes"):
        if(a>=2000):
            dunit=a-(a*0.1)
elif (category=="commerical"):
    if(0<=unit<=2200):
        b=unit*2.75
    if(2201<=unit<=4500):
        b=unit*3.75
    if(4501<=unit<=7000):
        b=unit*4.90
    if(unit>=7001):
        b=unit*6.40
gst1=a+(a*0.155)
gst=b+(b*0.155)
if(unit>=8000 and (category=="commerical")):
    fine=gst+(gst*0.05)
print("unit:",unit)
print("total amount of domestic bill is:",a)
print("Solar installation 10 percentage discount on the bill:",dunit)
print("with gst domestic bill is:",gst1)
print("total amount of commerical bill is:",b)
print("with gst commerical bill is:",gst)
print("fine for commerical if unit is more than 8000 unit:",fine)



