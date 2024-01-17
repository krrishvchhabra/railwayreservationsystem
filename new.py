import random
import mysql.connector as ch
conn=ch.connect(host='localhost',user="root",passwd='passwd',database='train')
#if conn.is_connected()==1:
#    print("connected")
#else:
#    print("not connected")

cur=conn.cursor()
i=0
def adminmenu():
                print("Enter 1 to add Train details")

                m=int(input("Enter your choice: "))
                if (m==1):
                            train()
def railsmenu():
                print("Railway Reservation")
                print("1.Train Detail")
                print("2.Reservation of Ticket")
                print("3.Cancellation of Ticket")
                print("4.Display PNR status")
                print("5.Quit")
                
                n=int(input("Enter your choice: "))
                if(n==1):
                                train_detail()
                elif(n==2):
                                reservation()
                elif(n==3):
                                cancel()
                elif(n==4):
                                displayPNR()
                elif(n==5):
                                return("Exit")
                else:
                                print("Wrong Choice")

def train_detail():
    l=[]
    a=str(input("Enter your Starting Point: "))
    b=str(input("Enter your Destination: "))
    l.append(a)
    l.append(b)
    sql="select train_no,cost,via,time_of_departure,date_available from train_detail where starting_point=%s and destination=%s"
    cur.execute(sql,l)
    f=cur.fetchall()
    l=len(f)
    if l>0:
        print("Information for trains available is represented as Train Number, Ticket Price, Via, Departure Time, and Departure Date respectfully\n")
        for j in range(0,l):
            print(j+1,":",f[j])
    elif l==0:
        print("No such trains available.")
    print(railsmenu())

def reservation():
    print("1. Enter your Information as follows:")
    l=[]
    l1=[]
    x=random.randint(100000000,999999999)
    l.append(x)
    a=str(input("Enter Passenger's Name: "))
    l.append(a)
    b=str(input("Enter your age: "))
    l.append(b)
    c=str(input("Enter your Gender (M/F/O): "))
    l.append(c)
    d=str(input("Enter Train Number: "))
    l.append(d)
    l1.append(d)
    e="select starting_point,destination from train_detail where train_no=%s"
    cur.execute(e,l1)
    f=cur.fetchall()
    print(f)
    w=f[0]
    xa=w[0]
    t=w[1]
    print(xa)
    print(t)
    l.append(xa)
    l.append(t)
    g="insert into user_information(unique_id,uname,age,gender,train_no,starting_point,destination)values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(g,l)
    conn.commit()
    print("Information Uploaded")
    Z="select cost from train_detail where train_no=%s"
    cur.execute(Z,l1)
    n=cur.fetchall()
    nox=n[0]
    noxy=nox[0]
    print("Ticket Amount: ",noxy)
    print("GST(5%): ",0.05*noxy)
    fn=noxy+0.05*noxy
    print("Amount to be paid: ",fn)
    mn=str(input("Would you Like to Confirm your Seat (Y/N): "))
    l3=[]
    l4=[]
    pop="Reserved"
    dop="Not Reserved"
    l3.append(pop)
    l4.append(dop)
    l5=l3+l1
    l6=l4+l1
    
    if mn.upper()=="Y":
        mysql="update user_information set reservation=%s where train_no=%s"
        cur.execute(mysql,l5)
        conn.commit()
        print("Your Ticket is Confirmed")
        print("Your Unique ID is : ",x)
    elif mn.upper()=="N":
        print("Your Ticket is not Reserved")
        print("Your Unique ID is : ",x)
        mysql="update user_information set reservation=%s where train_no=%s"
        cur.execute(mysql,l6)
        conn.commit()
    else:
        print("Wrong Option")
        print("\n*10",railsmenu())
    print("\n*10",railsmenu())

def cancel():
    l=[]
    a=int(input("Enter UNIQUE ID Provided at the time of Ticket Booking: "))
    l.append(a)
    b="delete from user_information where unique_id=%s"
    cur.execute(b,l)
    conn.commit()
    print("YOUR TICKET IS CANCELLED")
    print("YOUR REFUND WILL BE PROCESSED WITHIN 48 HOURS. A CANCELLATION FEE OF 25% OF THE TICKET VALUE WILL BE DEDUCTED.")
    print("\n*10",railsmenu())
    
def displayPNR():
    l=[]
    a=int(input("Enter UNIQUE ID Provided at the time of Ticket Booking: "))
    l.append(a)
    sql="select * from user_information where unique_id=%s"
    cur.execute(sql,l)
    f=cur.fetchall()
    print("Your Current Reservation Status is:",f)
    print("\n*10",railsmenu())
    
def train():
    print("Train Details")
    ch='Y'
    while (ch.upper()=='Y'):
                    l=[]
                    tnum=int(input("Enter Train Number: "))
                    l.append(tnum)
                    ac1=float(input("Enter Ticket Cost: "))
                    l.append(ac1)
                    ac2=str(input("Enter Starting Point: "))
                    l.append(ac2)
                    ac3=str(input("Enter Destination: "))
                    l.append(ac3)
                    slp=str(input("Enter via: "))
                    l.append(slp)
                    e=str(input("Enter Time of Departure: "))
                    l.append(e)
                    f=str(input("Enter Boarding Date: "))
                    l.append(f)
                    sql="insert into train_detail values(%s,%s,%s,%s,%s,%s,%s)"
                    print(sql,l)
                    cur.execute(sql,l)
                    conn.commit()
                    print("Insertion Completed")
                    print("Do you want to insert more Train Details?")
                    ch=input("Enter Y/N: ")
    print('\n' *10)

    print("===================================================================")

print("1. Admin Login")
print("2. General Login")
xyz=int(input("Enter Login Choice: "))
if xyz==1:
    xo=""
    while xo!="passwd":
        xo=str(input("Enter Admin Password: "))
        if xo=="passwd":
            adminmenu()
if xyz==2:
        railsmenu()