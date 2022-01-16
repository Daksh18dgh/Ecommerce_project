k = ''
def show_menu():
    print("                           MENU                   ")
    print("""---------------------------------------------------------------------------------
                                    My Bazaar
---------------------------------------------------------------------------------""")
    print("""Hello! Welcome to my Grocery store
These are the list of the following items available""")
    print("""-------------------------------------------------
    CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
------------------------------------------------- 
      0  | Tshirt      | Apparels     | 500
      1  | Trousers    | Apparels     | 600
      2  | Scarf       | Apparels     | 250
      3  | Smartphone  | Electronics  | 20,000
      4  | iPad        | Electronics  | 30,000
      5  | Laptop      | Electronics  | 50,000
      6  | Eggs        | Eatables     | 5
      7  | Chocolate   | Eatables     | 10
      8  | Juice       | Eatables     | 100
      9  | Milk        | Eatables     | 45
------------------------------------------------""")
    while True:
        global k
        print("Would you like to buy in bulk or regular? (y or Y for bulk / n or N for regular)")
        k = input("enter your answer:")
        if (k == "y" or k=="Y" or k=="N" or k=="n"):
            break

def get_regular_input():
    print("_____________________________________________________________________________________")
    print("                    ENTER ITEMS YOU WISH TO BUY                          ")
    print("_____________________________________________________________________________________")
    Input=list(map(int,input("enter the  item codes of product you want to buy(space -separated ):").split()))
    L1=[]
    for j in range(len(Input)):
        if(Input[j]>=0 and Input[j]<=9):
            L1=L1+ [Input[j]]
        else:
            print(" input is Invalid")
    Quantity=[0,0,0,0,0,0,0,0,0,0]
    for k in range(len(L1)):
        Quantity[L1[k]]=Quantity[L1[k]]+1
    return Quantity
def get_bulk_input():
    print("_________________________________________________________________________________________")
    print("                 ENTER  ITEM AND  QUANTITIES                                          ")
    print("_________________________________________________________________________________________")
    des=["tshirt","trouser","Scarf","Smartphone","iPad","Laptop","Eggs","Chocolate","Juice","Milk"]
    quantity=[0]*10

    while True:
        a = list( map(int, input("enter the  item code and Quantity of  product you want to buy(space separated):").split()))

        if (len(a) == 0):

            print("Your order has been finalsed")
            break
        elif(a[0]>=0 and a[0]<= 9 and a[1]>0):
            quantity[a[0]] += a[1]
            print("You added  "+str(a[1]),des[a[0]])


        elif((a[0]<0 or a[0]>9) and a[1]>0  ):
            print("code invalid. try again")

        elif((a[0] >= 0 and a[0] <= 9) and a[1] < 0):
            print("invalid quantity. try again ")

        elif(a[0]<=0 and a[1]<=0):
            print("both code and quantity are invalid . try again")

    return quantity

def print_order_details(quantity):
    print("______________________________________________________________________________________")
    print("                               ORDER DETAILS                                    ")
    print("______________________________________________________________________________________")
    c=0
    product=[['Tshirt',500],['Trousers',600],['Scarf',250],['Smartphone',20000],['iPad',30000],['Laptop',50000],['Eggs',5],['Chocolate',10],['Juice',100],['Milk',45]]
    for i in range(len(quantity)):
        if (quantity[i]>0):
            c+=1
            print("["+str(c)+"]"+product[i][0]+" x "+str(quantity[i])+"="+"Rs"+" "+str(product[i][1])+"*"+str(quantity[i])+"="+"  Rs ",quantity[i]*product[i][1 ])


def calculate_category_wise_cost(quantity):
    print("__________________________________________________________________________________________")
    print("                CATEGORY - WISE  COST                          ")
    print("__________________________________________________________________________________________")
    product = [['Tshirt', 500], ['Trousers', 600], ['Scarf', 250], ['Smartphone', 20000], ['iPad', 30000],['Laptop',50000],['Eggs',5],['Chocolate',10],['Juice',100],['Milk',45]]
    apparels_cost=0
    electronics_cost=0
    eatables_cost=0
    for i in range(len(quantity)):
        if(i==0 or i==1 or i==2):
            apparels_cost = apparels_cost+product[i][1]*quantity[i]
        elif(i==3 or i==4 or i==5):
            electronics_cost=electronics_cost+product[i][1]*quantity[i]
        elif(i==6 or i==7 or i==8 or i==9):
            eatables_cost=eatables_cost+product[i][1]*quantity[i]
    if (apparels_cost>0):
        print("Apparels = Rs ",apparels_cost)
    if (electronics_cost>0):
        print("Electronics = Rs ",electronics_cost)
    if (eatables_cost>0):
        print("Eatables = Rs ",eatables_cost)
    h=(apparels_cost,electronics_cost,eatables_cost)
    return h

def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print("_______________________________________________________________________________________")
    print("             Tax                            ")
    print("_______________________________________________________________________________________")
    tax1=apparels_cost*0.10
    tax2=electronics_cost*0.15
    tax3=eatables_cost*0.05
    totaltax= tax1 +tax2+tax3
    Totalcost=apparels_cost+electronics_cost+eatables_cost+tax1+tax2+tax3
    if(apparels_cost>0):
        print("[APPAREL] Rs "+str(apparels_cost)+"*"+"0.10 = Rs ",int(tax1))
    if(electronics_cost>0):
        print("[ELECTRONICS] Rs " + str(electronics_cost) + "*" + "0.15 = Rs ", int(tax2))
    if (eatables_cost>0):
        print("[EATABLES] Rs " + str(eatables_cost) + "*" + "0.05 = Rs ", int(tax3))
    print("TOTAL TAX = Rs ",int(totaltax))
    print("TOTAL COST = Rs ",int(Totalcost))
    return (int(Totalcost), int(totaltax))


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print("____________________________________________________________________________________________")
    print("               DISCOUNT                       ")
    print("_____________________________________________________________________________________________")

    l=0
    m=0
    n=0
    x=0
    q=0
    w=0
    if(apparels_cost>=2000):
        print("[APPAREL] Rs "+str(apparels_cost)+" - "+str(apparels_cost*0.1)+" = Rs ",int(apparels_cost*0.90))
        l+=int(apparels_cost*0.10)

    if(electronics_cost>=25000):
        print("[ELECTRONICS] Rs " + str(electronics_cost) +" - "+str(electronics_cost*0.1)+ " = Rs ", int(electronics_cost*0.90))
        m+=int(electronics_cost*0.10)

    if (eatables_cost>=500):
        print("[EATABLES] Rs " + str(eatables_cost) +  " - "+str(eatables_cost*0.1)+ " = Rs ",int(eatables_cost*0.90) )
        n+=int(eatables_cost*0.10)

    print("TOTAL DISCOUNT = Rs ",int(l+m+n))
    print("TOTAL COST = Rs ",int(apparels_cost+electronics_cost+eatables_cost-(int(l+m+n))))
    return (int(apparels_cost-l),int(electronics_cost-m),int(eatables_cost-n))

def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


#function for applying coupon code:
def apply_coupon_code(total_cost):
    print("________________________________________________________________________________________________")
    print("               COUPON CODE                ")
    print("________________________________________________________________________________________________")
    coupon_dis  = 0
    while True:
        g = input("Enter coupon code(else leave blank):")
        if (g == "HELLE25" or g == "CHILL50"):
            if (g == "HELLE25"):
                if (total_cost >= 25000):
                    total_cost = total_cost - 5000
                    coupon_dis = 5000
                    print("[HELLE25] min( 5000, Rs" + str(total_cost) + "*0.25)= Rs 5000")
                    print("""

TOTAL COUPON DISCOUNT= Rs 5000""")
                    print("TOTAL COST = Rs ", int(total_cost))
                    print("Thank you for shopping!")
                    break

                elif (total_cost <= 25000):
                    print("No coupon applied")
                    print("Thank you for shopping!")
                    coupon_dis = 0
            elif (g == "CHILL50"):
                if (total_cost >= 50000):
                    total_cost = total_cost - 10000
                    coupon_dis = 10000
                    print("[CHILL50] min( 10000, Rs" + str(total_cost) + "*0.50)= Rs 10000")
                    print("""

        TOTAL COUPON DISCOUNT= Rs 10000""")
                    print("TOTAL COST = Rs ", int(total_cost))
                    print("Thank you for shopping!")
                    break
                elif(total_cost<50000):
                    print("No coupon applied")
                    print("Thank you for shopping!")
                    coupon_dis = 0
                    break

        elif (g == ""):
            print("No Coupon code Applied")
            print("Thank you for shopping!")
            coupon_dis = 0
            break


        else:
            print("Invalid coupon code. Try again")
    return (total_cost,coupon_dis)






def main():

    show_menu()
    if(k=="y" or k=="Y"):
        quantity = get_bulk_input()
    else:
        quantity = get_regular_input()
    print_order_details(quantity)
    kl = calculate_category_wise_cost(quantity)
    m = calculate_discounted_prices(kl[0],kl[1],kl[2])
    cost_tax = calculate_tax(m[0],m[1],m[2])
    apply_coupon_code(cost_tax[0])
if __name__ == '__main__':
    main()

