#COLLEGE CANTEEN TOKEN SYSTEM
 

def Price_List():
    print("Idli--> Rs 20")
    print("Dosa--> Rs 40")
    print("Fried Rice--> Rs 80")
    print("Juice--> Rs 30")
   
def Student_Order():
    Token=1
    Number=int(input("Enter the number of students who want to place order:"))  #Stores number of students placing order
    for i in range(Number):
        Student_Name=input("Enter student name:")
        Food_Item=input("Enter food item:")
        Quantity=int(input("Enter the number of plates to be ordered:"))
        
        #To calculate price
        Price=0
        if Food_Item=="Idli":
            Price+=Quantity*20
        elif Food_Item=="Dosa":
            Price+=Quantity*40
        elif Food_Item=="Fried Rice":
            Price+=Quantity*80
        elif Food_Item=="Juice":
            Price+=Quantity*30
    
        #To print order
        print(f"Order of {Student_Name}")
        print(f"Token{Token}-->{Student_Name}-->{Quantity}{Food_Item}-->{Price}")
        Token+=1

while True:
    print("---COLLEGE CANTEEN---")
    print("1.View Price List")
    print("2.Place Order")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        Price_List()
    elif choice==2:
        Student_Order()
    elif choice==3:
        print("Thank you for visiting college canteen!")
        break
    else:
        print("Incorrect choice")





    
                     
    
