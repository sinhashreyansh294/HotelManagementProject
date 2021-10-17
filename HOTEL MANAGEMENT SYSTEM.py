import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import random as rad
class hotelfarecal:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, Customer_Name='', Customer_Address='', Check_IN='', checkout_date='', rno=0,q=0,b=0,w=0, UCB=""):
        print ("*******************WELCOME TO UCB BILLING PORTAL****************************")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.q=q
        self.b=b
        self.name=Customer_Name
        self.address=Customer_Address
        self.cindate=Check_IN
        self.coutdate=checkout_date
        self.w=rad.randint(11111111,88888888)
        self.rno=rno
        self.rno=rad.randint(101,999)
        self.UCB= {'Customer Name': [],'Amount': []}

    def reset(self):
            self.rt=''
            self.s=0
            self.p=0
            self.r=0
            self.t=0
            self.a=1800
            self.name=''
            self.address=''
            self.cindate=''
            self.coutdate=''
                        
            self.q=0
            self.b=0
            
        
        
    def inputdata(self):
        self.name=input("  Enter the Name of the Customer :   ")
        if ((self.name>='a' and self.name<= 'z') or (self.name>='A' and self.name<='Z')):
            print("  The Customer Name is :  ", self.name)
        else:
            print("  ERROR: Do not use any Alpha Numeric Value")
            quit()
        Age = int(input("\n  Enter the Customer Age : "))
        print("  Customer age is : ",Age) 
        Members = int(input("\n  Enter the Number of Guests : "))
        self.address=input("\n  Enter the Customer's Address : ")
        print("  Customer Address is : ",self.address)
        self.cindate = datetime.today()
        print("\n  Your Check In Date Is :    ",self.cindate)
        self.coutdate = input("\n  Enter the Check Out date : ")
        date = datetime.strptime(self.coutdate, "%Y-%m-%d")
        for datecheck in 'date':
                 if self.cindate > date:
                     print("  Error: Wrong Input.")
                     quit()
        
    def roomrent(self):
        print ("  We have the following rooms for you:-")
        print("  1)ROOM TYPE: DOUBLE BED ROOM --> COST= Rs. 10,000")
        print("  2)ROOM TYPE: SINGLE SUITE --> COST=Rs.30,000")
        print("  3)ROOM TYPE: DOUBLE SUITE --> COST=Rs. 50,000")
        print("  4)ROOM TYPE: DUPLEX SUITE --> COST=Rs. 70,000")
        print("  5)ROOM TYPE: LUXURY SUITE --> COST=Rs. 1,00,000")
        x = int(input("  Enter your Room Occupancy Choice : "))
        if (x==1):
            
            
            print ("  you have opted room type DOUBLE BED ROOM")
            n = int(input("  Please Enter Number of Nights of Stay : "))
            self.s=10000*n
            print("  Total Cost of Room Rent is :",self.s)
            print("  Your Room Number is :     ", self.rno)
            print ("\n\n  COMPLIMENTARY SERVICES : DOUBLE BED ROOM ")
            print("  1. COMPLIMENTARY WIFI. ")
            print("  2. COMPLEMENTARY WATER BOTTLES. ")
            print("  3. COMPLEMENTARY TOILETERIES. ")
            print("  4. Press 4 to get back to LOBBY. ")
            ch = 0
            ID = "ER4U2968"
            while(1):
                    ch = int(input("  ENTER YOUR CHOICE FOR COMPLIMENTARY SERVICES : "))
                    if ( ch==1 ) :
                            
                            print ( "  Your Wifi ID is :", ID)
                            print ("  * Your Wi Fi Password is :",self.w)
                    elif ( ch==2 ):
                        print( "  * Please check your Room for Water Bottles.")
                    elif ( ch==3 ) :
                        print( "  * Please contact Room Service by dialling 4 from your room telephone. ")
                    elif( ch==4 ) :
                        print( "  ********Thank You for your Co-Operation.**********")
                        break
                    else:
                        print("   Please try a Desired INPUT......")
                        break
                
        elif (x==2):
            

            print ("  You have opted room type SINGLE SUITE")
            n = int(input("  Please Enter Number of Nights of Stay : "))
            self.s=30000*n
            print("  Total Cost of Room Rent is :",self.s)
            print("  Your Room Number is :     ", self.rno)
            print ("\n\n  COMPLIMENTARY SERVICES : Single Suite ")
            print("  1. COMPLIMENTARY WIFI. ")
            print("  2. COMPLEMENTARY WATER BOTTLES. ")
            print("  3. COMPLEMENTARY TOILETERIES. ")
            print("  4. COMPLEMENTARY SWIMMING POOL.")
            print("  5. Press 5 to get back to LOBBY. ")
            ch = 0
            ID = "ER4U2968"
            while(1):
                    ch = int(input("  ENTER YOUR CHOICE FOR COMPLIMENTARY SERVICES : "))
                    if ( ch==1 ) :                     
                            print ( "  Your Wifi ID is :", ID)
                            print ("  * Your Wi Fi Password is :",self.w)
                    elif ( ch==2 ):
                        print( "  * Please check your Room for Water Bottles.")
                    elif ( ch==3 ) :
                        print( "  * Please contact Room Service by dialling 4 from your room telephone. ")
                    elif ( ch==4 ) :
                        print("   Swimming Pool Timings : 08:00 a.m - 06:00 p.m")
                    elif( ch==5 ) :
                        print( "  ********Thank You for your Co-Operation.**********")
                        break
                    else:
                        print("   Please try a Desired INPUT......")
                        break
        elif (x==3):
            
            print ("  You have opted room type DOUBLE SUITE")
            n = int(input("  Please Enter Number of Nights of Stay : "))
            self.s=50000*n
            print("  Total Cost of Room Rent is :",self.s)
            print("  Your Room Number is :     ", self.rno)
            print ("\n\n  COMPLIMENTARY SERVICES : DOUBLE SUITE ")
            print("  1. COMPLIMENTARY WIFI. ")
            print("  2. COMPLEMENTARY WATER BOTTLES. ")
            print("  3. COMPLEMENTARY TOILETERIES. ")
            print("  4. GYM & SWIMMING POOL. ")
            print("  5. Press 5 to get back to LOBBY. ")
            ch = 0
            ID = "ER4U2968"
            while(1):
                    ch = int(input("  ENTER YOUR CHOICE FOR COMPLIMENTARY SERVICES : "))
                    if ( ch==1 ) :                     
                            print ( "  Your Wifi ID is :", ID)
                            print ("  * Your Wi Fi Password is :",self.w)
                    elif ( ch==2 ):
                        print( "  * Please check your Room for Water Bottles.")
                    elif ( ch==3 ) :
                        print( "  * Please contact Room Service by dialling 4 from your room telephone. ")
                    elif ( ch==4 ) :
                        print("   Gym Timings : 06:00 a.m  - 11:00 p.m")
                        print("   Swimming Pool Timings : 08:00 a.m - 06:00 p.m")
                    elif( ch==5 ) :
                        print( "  ********Thank You for your Co-Operation.**********")
                        break
                    else:
                        print("   Please try a Desired INPUT......")
                        break
        elif (x==4):
            
            print ("  You have opted room type DUPLEX SUITE")
            n = int(input("  Please Enter Number of Nights of Stay : "))
            self.s=70000*n
            print("  Total Cost of Room Rent is :",self.s)
            print("  Your Room Number is :     ", self.rno)
            print ("\n\n  COMPLIMENTARY SERVICES : DUPLEX SUITE ")
            print("  1. COMPLIMENTARY WIFI. ")
            print("  2. COMPLIMENTARY WATER BOTTLES. ")
            print("  3. COMPLIMENTARY TOILETERIES. ")
            print("  4. GYM & SWIMMING POOL. ")
            print("  5. AIRPORT TRANSFERS. ")
            print("  6. Press 6 to get back to LOBBY. ")
            ch = 0
            ID = "ER4U2968"
            while(1):
                    ch = int(input("  ENTER YOUR CHOICE FOR COMPLIMENTARY SERVICES : "))
                    if ( ch==1 ) :                     
                            print ( "  Your Wifi ID is :", ID)
                            print ("  * Your Wi Fi Password is :",self.w)
                    elif ( ch==2 ):
                        print( "  * Please check your Room for Water Bottles.")
                    elif ( ch==3 ) :
                        print( "  * Please contact Room Service by dialling 4 from your room telephone. ")
                    elif ( ch==4 ) :
                        print("   Gym Timings : 06:00 a.m  - 11:00 p.m")
                        print("   Swimming Pool Timings : 08:00 a.m - 06:00 p.m")
                    elif ( ch==5 ) :
                        print("   Contact Reception Desk for Airport transfers.")
                    elif( ch==6 ) :
                        print( "  ********Thank You for your Co-Operation.**********")
                        break
                    else:
                        print("   Please try a Desired INPUT......")
                        break
                    
            
        elif (x==5):
            
            print ("  You have opted room type LUXURY SUITE")
            n = int(input("  Please Enter Number of Nights of Stay : "))
            self.s=100000*n
            print("  Total Cost of Room Rent is :",self.s)
            print("  Your Room Number is :     ", self.rno)
            print ("\n\n  COMPLIMENTARY SERVICES : DOUBLE BED ROOM ")
            print("  1. COMPLIMENTARY WIFI. ")
            print("  2. COMPLEMENTARY WATER BOTTLES. ")
            print("  3. COMPLEMENTARY TOILETERIES. ")
            print("  4. GYM & SWIMMING POOL. ")
            print("  5. AIRPORT TRANSFERS. ")
            print("  6. BREAKFAST & DINNER. ")
            print("  7. Press 7 to get back to LOBBY. ")
            ch = 0
            ID = "ER4U2968"
            while(1):
                    ch = int(input("  ENTER YOUR CHOICE FOR COMPLIMENTARY SERVICES : "))
                    if ( ch==1 ) :                     
                            print ( "  Your Wifi ID is :", ID)
                            print ("  * Your Wi Fi Password is :",self.w)
                    elif ( ch==2 ):
                        print( "  * Please check your Room for Water Bottles.")
                    elif ( ch==3 ) :
                        print( "  * Please contact Room Service by dialling 4 from your room telephone. ")
                    elif ( ch==4 ) :
                        print("   Gym Timings : 06:00 a.m  - 11:00 p.m")
                        print("   Swimming Pool Timings : 08:00 a.m - 06:00 p.m")
                    elif ( ch==5 ) :
                        print("   Contact Reception Desk for Airport transfers.")
                    elif ( ch==6):
                        print("   Your Breakfast & Dinner is included. ")
                        print("   Please contact the restaurant for timings. ")
                    elif( ch==7 ) :
                        print( "  ********Thank You for your Co-Operation.**********")
                        break
                    else:
                        print("   Please try a Desired INPUT......")
                        break
        else:
            print("  Please Enter a Valid OUTPUT.")
            quit()
            
    
            
        
    def restaurentbill(self):
        print("  *****RESTAURANT MENU*****")
        print("\n  ************************MENU***********************************")
        print("\n  ___________________________STARTER_________________________________________")
        print("  _1. SPRING ROLLS - Rs.285 ")
        print("  _2. CRISPY VEGETABLES IN SALT 'N' PEPPER - Rs.650")
        print("  _3.  CRISPY LOTUS STEM - Rs.350")
        print("  _4. MOZARELLA CORN BALLS - Rs.400")
        print("  _5. BAKED NACHOS WITH SALASA - Rs. 600")
        print("\n  __________________________MEDITERIAN CUISINE_____________________________________")
        print("  _6.  OPEN FACED SMOKE MACKEREL SANDWICHES - Rs. 1100")
        print("  _7.  BULGUR SALAD WITH LIGHTLY ROASTED VEGETABLES- Rs. 850")
        print("  _8.  GREEN LENTIL HUMMUS- Rs. 400")
        print("  _9.   SEA BASS WITH TOMATO AND BLACK SALSA - Rs. 1875")
        print("  _10. RASBERRY AND FIG CAKE - Rs. 2075")
        print("\n  __________________________INDIAN CUISINE_________________________________________")
        print("  _11. CHICKE VINDALOO CURRY - Rs. 1000")
        print("  _12. ROGAN JOSH(RED LAMB) - Rs. 1785")
        print("  _13. CHICKPEA CURRY - Rs. 1600")
        print("  _14. SPINACH AND COTTAGE CHEESE - Rs. 760")
        print("  _15. VEGGIE BALL IN A THICK SAUCE - Rs. 890")
        print("\n  __________________________HAUTE CUISINE AND DESERTS______________________________")
        print("  _16. PELIT FOUR - Rs. 500")
        print("  _17. CREME BRULEE - Rs. 650")
        print("  _18. BONBONS - Rs.190")
        print("  _19. PATE DE FOIE GRAS - Rs. 280")
        print( "\n  PRESS 20 TO GET BACK TO LOBBY.....")
        
        while (1):
            c=int(input("  Please Select your Meal :"))
            if (c==1):
                
                d=int(input("  Enter the quantity:"))
                self.r=self.r+285*d
                
            elif (c==2):
                
                d=int(input("  Enter the quantity:"))
                self.r=self.r+650*d
            elif (c==3):
                
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+350*d
            elif (c==4):
                
                  d=int(input("  Enter the quantity:"))
                  self.r=self.r+400*d
            elif (c==5):
                
                  d=int(input("  Enter the quantity:"))
                  self.r=self.r+600*d
            elif (c==6):
                
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+1100*d
            elif (c==7):
                
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+850*d
            elif (c==8):
                
                  d=int(input("  Enter the quantity:"))
                  self.r=self.r+400*d
            elif (c==9):
                
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+1875*d
            elif (c==10):
                
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+2075*d
            elif (c==11):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+1000*d
            elif (c==12):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+1785*d
            elif (c==13):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+1600*d
            elif (c==14):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+760*d
            elif (c==15):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+890*d
            elif (c==16):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+500*d
            elif (c==17):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+650*d
            elif (c==18):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+190*d
            elif (c==19):
             
                 d=int(input("  Enter the quantity:"))
                 self.r=self.r+280*d
                 print ("  Total food Cost=Rs",self.r,"\n")
            elif (c==20):
                break
            else:
                print("  Enter a Desired Input. ")
                quit()
    def laundrybill(self):
        print ("    ******LAUNDRY MENU*******")
        print ("  1.SUITS - Rs. 300")
        print("  2. SHIRTS - Rs. 100")
        print("  3. SUIT PANTS - Rs. 250")
        print("  4. JEANS - Rs 100")
        print("  5. NIGHTSUITS - Rs. 100")
        print("  \nPRESS 6 TO BACK TO LOBBY......")
        while (1):
            e=int(input("  Enter your choice:"))
            if (e==1):
                
                f=int(input("  Enter the quantity:"))
                self.t=self.t+300*f
            elif (e==2):
                
                f=int(input("  Enter the quantity:"))
                self.t=self.t+100*f
            elif (e==3):
                
                f=int(input("  Enter the quantity:"))
                self.t=self.t+250*f
            elif (e==4):
                
                f=int(input("  Enter the quantity:"))
                self.t=self.t+100*f
            elif (e==5):
                
                f=int(input("  Enter the quantity:"))
                self.t=self.t+100*f
            elif (e==6):
                
                break;
            else:
                print ("  PLEASE TRY A DESIRED INPUT.")
                quit()
        print ("  Total Laundary Cost=Rs",self.t,"\n")
    def tourantr(self):#tour
        print ("  ******TOUR&TRAVELS*******")
        print ("  1. AIRPORT PICKUP/DROP----->Rs. 4000")
        print("  2. SIGHTSEEING TOUR----->Rs. 10,000")
        print("  3. EIGHT HOURS PACKAGE ---> Rs7000")
        print("  4. OUTSTATION PACKAGES ----> Rs. 20,000")
        print("  5. Escorted Tour ------> Rs. 30,000")
        print("  6. PRESS 6 TO GET BACK TO LOBBY.")
        while (1):
            g=int(input("  Enter your choice:"))
            if (g==1):
                
                self.p=self.p+4000
                print("  AIRPORT PICKUP/DROP : ",self.p)
            elif (g==2):
                
                self.p=self.p+10000
                print("  SIGHTSEEING TOUR" ,self.p)
            elif (g==3):
                
                self.p=self.p+7000
                print("  EIGHT HOURS PACKAGE",self.p)
            elif (g==4):
                
                self.p=self.p+20000
                print("  OUTSTATION PACKAGES" ,self.p)
            elif (g==5):
                
                self.p=self.p+30000
                print("  Escorted Tour",self.p)
            elif (g==6):
                                print("  Exiting The Program.")
                                break;
            else:
                print ("  PLEASE ENTER A VALID INPUT")
                quit()
        print ("  Total Tour Bill=Rs",self.p,"\n")
    def spa(self):
        print("  **********SPA SERVICES***********")
        print("  1. Head Massage(with special Aroma Oil) ---> Rs. 2,000")
        print("  2. Foot SPA ---> Rs. 1,500")
        print("  3. Back Massage -----> Rs. 5,000")
        print("  4. Brightening Facial ----> Rs. 4,500")
        print("  5. Aqua Massage -----> Rs. 5,000")
        print("  6. Aroma Therapy -----> Rs. 7,000")
        print("  7. French Pedicure ------> Rs. 2,500")
        print("  8. French Manicure -------> Rs. 3,000")
        print("  9. Jacuzzi Bath  -----> Rs. 5,000")
        print("  10. Sauna Bath ----> Rs. 4,500")
        print("\n  Press 11 to Exit to Lobby. ")
        while (1):
            g=int(input("  Enter your choice:"))
            if (g==1):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+2000*h
                print("  Head MAssage : ",self.q)
            elif (g==2):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+1500*h
                print("  Foot SPA : ",self.p)
            elif (g==3):    
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+5000*h
                print("  Back Massage : ",self.q)
            elif (g==4):
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+4500*h
                print("  Brightening Facial : ",self.q)
            elif (g==5):
            
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+5000*h
                print("  Aqua Massage : ",self.q)
            elif (g==6):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+7000*h
                print("  Aroma Therapy : ",self.q)
            elif (g==7):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+2500*h
                print("  French Pedicure : ",self.q)
            elif (g==8):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+3000*h
                print("  French Manicure : ",self.q)
            elif (g==9):
                self.q=0
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+5000*h
                print("  Jacuzzi Bath : ",self.q)
            elif (g==10):
                
                h=int(input("  Enter the Number of Hours: "))
                self.q=self.q+4500*h
                print("  Sauna Bath : ",self.q)
            elif (g==11):
                
                print("  Exiting The Program.")
                break
                print ("  Total Tour Bill=Rs",self.q,"\n")
            else:
                print ("  PLEASE ENTER A VALID INPUT")
                quit()
    def business(self):
        print("  **************Business Services******************")
        print("  1. Executive Lounges Rs ----> Rs. 9,000")
        print("  2. Meeting\Cornference Rooms -----> Rs. 10,000 ")
        print("  3. Fax\Printing\Copying Services.-------> Rsb. 50")
        print("  4. Computers with Internet access. ------> Rs. 4,000")
        print("  5. Secreterial Services. ------> Rs. 8,000")
        print("\n  PRESS 6 TO BACK TO LOBBY......")
        while (1):
            e=int(input("  Enter your choice:"))
            if (e==1):
                
                f=int(input("  Enter the Number of Hours:"))
                self.b=self.b+9000*f
            elif (e==2):
                
                f=int(input("  Enter the Number of Hours:"))
                self.b=self.b+10000*f
            elif (e==3):
                
                f=int(input("  Enter the Number of Quantity:"))
                self.b=self.b+50
            elif (e==4):
                
                f=int(input("  Enter the Number of Hours:"))
                self.b=self.b+4000*f
            elif (e==5):

                f=int(input("  Enter the Number of Hours:"))
                self.b=self.b+8000*f
            elif (e==6):
                
                break;
            else:
                print ("  PLEASE TRY A DESIRED INPUT.")
                quit()
        print ("  Total Cost of Business Services=Rs",self.b,"\n")
        
                
        
        
    def display(self):
        print ("  ****************HOTEL BILL************************")
        print ("  Customer's details:-")
        print ("  Customer's name:",self.name)
        nam = self.name
        print ("  Customer's address:",self.address)
        print ("\n  Check in date:",self.cindate)
        print ("  Check out date", self.coutdate)
        print ("\n  Room no.",self.rno)
        print ("\n\n  Your Room rent is:",self.s)
        print("  Step 1", self.s);
        print ("\n  Your Food bill is:",self.r)
        print("  Step 2", self.r);
        print("\n  Your Spa Services charge:",self.q)
        print("  Step 3", self.q);
        print("\n\n  Your Business Service charges are",self.b)
        print("  Step 4", self.b);
        print ("  Your laundary bill is:",self.t)
        print("  Step 5", self.t);
        print ("  Your Tour and Travels is:",self.p)
        print("  Step 6", self.p);
        self.rt=self.s+self.t+self.p+self.r+self.q+self.b
        print("  Step 7", self.rt);
        print ("\n\n  Your sub total bill is:",self.rt)
        print ("  Additional Service Charges is",self.a)
        print("  Step 8", self.a);
        print ("\n  Your grandtotal bill is:",self.rt+self.a,"\n")
        gran = self.rt+self.a
        print("  Step 9", gran);
        self.rno+=1
        print("\n\n\n  *************THANK YOU FOR CHOOSING US HOPE YOU LIKE OUR SERVICE***************")
        self.UCB["Customer Name"].append(nam)
        self.UCB["Amount"].append(gran)
        
        df = pd.DataFrame(self.UCB)
        print(df)
        df.to_csv (r'C:\Users\sinha\OneDrive\Desktop\Book1.csv', mode ='a', index = False, header=True)

    def gra(self):
        df = pd.DataFrame(self.UCB)
        print('df-', df)      
        while(1):
            print("1. SPENT RATE  LINE GRAPH OF CUSTOMERS.")
            print("2. SPENT RATE BAR GRAPH OF CUSTOMERS.")
            print("3. SPENT RATE HORIZONTAL BAR GRAPH OF CUSTOMERS.")
            print("4. SPENT RATE HISTOGRAM OF CUSTOMERS.")
            ch = int(input("Enter Your Choice : "))
            if (ch == 1):
                    plt.style.use('dark_background')
                    df.plot('Customer Name', 'Amount',linestyle='-.',color='yellow',linewidth=2,marker="o",markerfacecolor='yellow',markersize=7)
                    plt.legend(loc='lower right')
                    plt.ylabel('AMOUNT SPENT',fontweight='bold',color='white')
                    plt.xlabel('CUSTOMER NAME',fontweight='bold',color='white')
                    plt.title('SPENT RATE  LINE GRAPH OF CUSTOMERS',fontweight='bold')
                    plt.grid(True,alpha=0.20)
                    plt.grid
                    plt.show()
            elif (ch == 2):
                    plt.style.use('dark_background')
                    width = 0.35
                    df.plot.bar('Customer Name', 'Amount',linestyle='dashed', linewidth =3,color = 'c')
                    plt.grid(color='w', linewidth='0.2')
                    plt.ylabel('AMOUNT SPENT',fontweight='bold',color='white')
                    plt.xlabel('CUSTOMER NAME',fontweight='bold',color='white')
                    plt.title('SPENT RATE BAR GRAPH OF CUSTOMERS',fontweight='bold',color='white')
                    plt.show()
            elif ( ch == 3):
                    plt.style.use('dark_background')
                    width = 0.35
                    df.plot.barh('Customer Name', 'Amount',linestyle='dashed', linewidth =3,color = 'c')
                    plt.grid(color='w', linewidth='0.2')
                    plt.ylabel('AMOUNT SPENT',fontweight='bold',color='white')
                    plt.xlabel('CUSTOMER NAME',fontweight='bold',color='white')
                    plt.title('SPENT RATE HORIZONTAL BAR GRAPH OF CUSTOMERS',fontweight='bold',color='white')
                    plt.show()
                
            elif (ch == 4):
                plt.style.use('dark_background')
                n_bins = 30
                df.plot.hist( 'Amount',n_bins, histtype='step', stacked=True, fill=False)
                plt.show()
       
              
def main():
    a=hotelfarecal()
    while(1):
        print(" _________________________________________________________________________________________")
        print("\n\n\n  1. CUSTOMER INITIALS.")
        print("  2. ROOM OCCUPANCY.")
        print("  3. RESTAURANT SERVICES.")
        print("  4. SPA SERVICES.")
        print("  5. BUSINESS SERVICES.")
        print("  6. LAUNDARY SERVICES.")
        print("  7. TOUR & TRAVELS SERVICES.")
        print("  8. TOTAL BILL.")
        print("  9. PLOTTING OF EXPENSE GRAPH.")
        print("  10. EXIT THE PORTAL.")
        b=int(input("\n  PLEASE ENTER THE SERVICE YOU WANT TO OPT FOR : "))
        if (b==1):
                a.reset()
                a.inputdata()   
        elif (b==2):
                
                a.roomrent()
        elif (b==3):
                
                a.restaurentbill()
        elif (b==4):
                
                a.spa()
        elif (b==5):
                
                a.business()
        elif (b==6):
                
                a.laundrybill()
        elif (b==7):
                
                a.tourantr()
        elif (b==8):
                a.display()
        elif (b==9):
                a.gra()
        elif (b==10):
                quit()
        else:
                print("PLEASE TRY A VALID INPUT.")
                break
main()

