import random
import mysql.connector as ch
conn=ch.connect(host='localhost',user="root",passwd='passwd',autocommit=True)
cur=conn.cursor()
cur.execute("CREATE DATABASE train")
cur.execute("USE train")
cur.execute("CREATE TABLE train_detail(train_no INT(10) not null,cost INT(10),starting_point VARCHAR(50),destination VARCHAR(60),via VARCHAR(90),time_of_departure VARCHAR(40),date_available VARCHAR(88),av_seats INT(10),bk_seats INT(10))")
cur.execute("CREATE TABLE user_information(unique_id int PRIMARY KEY,uname VARCHAR(40) not null,age INT(90),gender VARCHAR(50),train_no INT(90),starting_point VARCHAR(50),destination VARCHAR(60),reservation VARCHAR(20))")

def adminmenu():
                print("Enter 1 to add Train Details")
                print("Enter 2 to modify Train Details")
                print("Enter 3 to cancel Train")
                print("Enter 4 to go to Main Menu")

                m=int(input("Enter your choice: "))
                if (m==1):
                            train()
                if (m==2):
                            trainmodify()
                if (m==3):
                            traincancel()
                if (m==4):
                            menu()
def railsmenu():
                print("Railway Reservation")
                print("Enter 1 to fetch Train Details")
                print("Enter 2 to Reserve Ticket")
                print("Enter 3 to Cancel Ticket")
                print("Enter 4 to Display PNR status")
                print("Enter 5 to go to Main Menu")
                
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
                                menu()
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
    print("\n*10",railsmenu())

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
    l2=["Reserved"]
    l3=["Waitlisted"]
    l4=l2+l1
    l5=l3+l1
    l6=[]
    l7=[]
    chaval="select av_seats,bk_seats from train_detail where train_no=%s"
    cur.execute(chaval,l1)
    q=cur.fetchall()
    qq=q[0]
    av_seats=qq[0]
    bk_seats=qq[1]
    
    if bk_seats<av_seats:
        upd1="update user_information set reservation=%s where train_no=%s"
        cur.execute(upd1,l4)
        l6.clear()
        l7.clear()
        nbk_seats=bk_seats+1
        l6.append(nbk_seats)
        l7=l6+l1
        upd2="update train_detail set bk_seats=%s where train_no=%s"
        cur.execute(upd2,l7)
        print("Your Ticket has been Booked and is Reserved")
        print("Your Unique ID is: ",x)
    elif bk_seats>=av_seats and bk_seats<(av_seats*1.25):
        upd1="update user_information set reservation=%s where train_no=%s"
        cur.execute(upd1,l4)
        l6.clear()
        l7.clear()
        nbk_seats=bk_seats+1
        l6.append(nbk_seats)
        l7=l6+l1
        upd2="update train_detail set bk_seats=%s where train_no=%s"
        cur.execute(upd2,l7)
        print("Your Ticket has been Booked and you have placed in Waiting List")
        print("Your Unique ID is: ",x)
    elif bk_seats>=(1.25*av_seats):
        print("Tickets for your selected Train are not available. Kindly try booking in other Trains.")
        print("\n*10",railsmenu())
    print("\n*10",railsmenu())

def cancel():
    l=[]
    l8=[]
    a=int(input("Enter UNIQUE ID Provided at the time of Ticket Booking: "))
    l.append(a)
    b="select train_no from user_information where unique_id=%s"
    cur.execute(b,l)
    q=cur.fetchall()
    l.insert(0,"Booking Cancelled")
    q1=q[0]
    tno=q1[0]
    tno=[tno]
    can="delete from user_information where unique_id=%s"
    can="update user_information set reservation=%s where unique_id=%s"
    cur.execute(can,l)
    e=""
    c="select bk_seats from train_detail where train_no=%s"
    cur.execute(c,tno)
    t=cur.fetchall()
    t1=t[0]
    bk_seats=t1[0]
    nbk_seats=bk_seats-1
    l8.append(nbk_seats)
    tno1=tno[0]
    l8.append(tno1)
    d="update train_detail set bk_seats=%s where train_no=%s"
    cur.execute(d,l8)
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
    f1=f[0]
    f2=f1[7]
    if len(f)==1:
        print("Your Current Reservation Status is:",f2)
    if len(f)==0:
            print("PNR not found")
    print("\n"*10,railsmenu())
    
def train():
    print("Train Details")
    ch='Y'
    while (ch.upper()=='Y'):
                    l=[]
                    tnum=int(input("Enter Train Number: "))
                    l.append(tnum)
                    cost=float(input("Enter Ticket Cost: "))
                    l.append(cost)
                    start=str(input("Enter Starting Point: "))
                    l.append(start)
                    end=str(input("Enter Destination: "))
                    l.append(end)
                    via=str(input("Enter via: "))
                    l.append(via)
                    t=str(input("Enter Time of Departure: "))
                    l.append(t)
                    d=str(input("Enter Boarding Date: "))
                    l.append(d)
                    av=int(input("Enter Number of Available Seats: "))
                    l.append(av)
                    l.append(0)
                    sql="insert into train_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    print(l)
                    cur.execute(sql,l)
                    print("Insertion Completed")
                    print("Do you want to insert more Train Details?")
                    ch=input("Enter Y/N: ")
    print('\n' *10,adminmenu())

def traincancel():
    print("Train Cancellation")
    n=int(input("Enter Train Number: "))
    l=[]
    l1=["Train Cancelled"]
    l.append(n)
    l1.append(n)
    s="select starting_point,destination,cost,via,time_of_departure,date_available,av_seats from train_detail where train_no=%s"
    cur.execute(s,l)
    q=cur.fetchall()
    print(q)
    yn=input("Are you sure you want to cancel the train? (y/n): ")
    if yn.upper()=="Y":
            s1="delete from train_detail where train_no=%s"
            cur.execute(s1,l)
            s2="update user_information set reservation=%s where train_no=%s"
            cur.execute(s2,l1)
            print("Train has successfully been cancelled.")
            print('\n' *10,adminmenu())
    else:
            print("Train cancellation not successful")
            print('\n' *10,adminmenu())          

def trainmodify():
    print("Train Modification")
    n=int(input("Enter Train Number: "))
    l=[]
    l.append(n)
    sp="select * from train_detail where train_no=%s"
    cur.execute(sp,l)
    qnp=cur.fetchall()
    print(qnp)
    print("Enter 1 for Starting Point")
    print("Enter 2 for Destination")
    print("Enter 3 for Via")
    print("Enter 4 for Fare")
    print("Enter 5 for Date of Departure")
    print("Enter 6 for Time of Departure")
    print("Enter 7 for Available Seats")
    nq=int(input("Which Field do you want to Modify?: "))
    if nq==1:
            q=input("Enter new Starting Point: ")
            l.insert(0,q)
            s="update train_detail set starting_point=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==2:
            q=input("Enter new Destination: ")
            l.insert(0,q)
            s="update train_detail set destination=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==3:
            q=input("Enter new Via: ")
            l.insert(0,q)
            s="update train_detail set via=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==4:
            q=int(input("Enter new Fare: "))
            l.insert(0,q)
            s="update train_detail set cost=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==5:
            q=input("Enter new Date of Departure: ")
            l.insert(0,q)
            s="update train_detail set date_available=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==6:
            q=input("Enter new Time of Departure: ")
            l.insert(0,q)
            s="update train_detail set time_of_departure=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    if nq==7:
            q=int(input("Enter new Number of Available Seats: "))
            l.insert(0,q)
            s="update train_detail set av_seats=%s where train_no=%s"
            cur.execute(s,l)
            print("Details updated successfully")
    print("\n"*10,adminmenu())

def menu():
    print("Enter 1 for Admin Login")
    print("Enter 2 for General Login")
    print("Enter 3 to Quit")
    xyz=int(input("Enter Login Choice: "))
    if xyz==1:
        xo=""
        while xo!="passwd":
            xo=str(input("Enter Admin Password: "))
            if xo=="passwd":
                adminmenu()
    if xyz==2:
            railsmenu()
    elif xyz==3:
            return("Quit")

menu()
