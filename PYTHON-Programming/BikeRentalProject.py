# Display Available bikes
# Request a bike for rent (100Rs->1qty)
# Exit
class bikeShop:
    def __init__(self,stock):
        self.stock=stock

    def displayBike(self):
        print("Total Bikes",self.stock)
    
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero:-")
        elif q>self.stock:
            print("Enter the value (less than stock.)")
        else:
            print("Total Price",q*100)
            print("Total Bikes",self.stock)

while True:
    obj=bikeShop(100)
    print('''
1) Display Stocks.
2) Rent a Bike.
3) Exit.''')
    try:
        uc = int(input("Please enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if uc==1:
            obj.displayBike()
    elif uc==2:
            n=int(input("Entert the Quantity:-"))
            obj.rentForBike(n)
    elif uc==3:
        break
    else:
         print("You have entered a wrong choice. Please enter a valid number.")

    
