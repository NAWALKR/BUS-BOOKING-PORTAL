
import mysql.connector
from datetime import date
import random
import string
""".................Asansol to Kolkata Bus Booking Code..............."""

def bus1(connection,cur):
    pname = input("Enter passenger name :")
    page = int(input("Enter passenger age :"))
    pcon = int(input("Enter thr contact number :"))
    date_components =input('Enter the boarding date (YYYY-MM-DD):').split('-')
    year, month, day = [ int(item) for item in date_components ]
    boarding_date = date(year,month,day)
    depart ="Asansol"
    arrival ="kolkata"    
    ticket_number = ''.join(random.choices(string.ascii_uppercase+string.digits,k=7))
    query = "insert into bus1(passenger_name,passenger_age,contact,booking_date,departure,arrival,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
    values =(pname,page,pcon,boarding_date,depart,arrival,ticket_number)
    cur.execute(query,values)
    connection.commit()
    print("Bus booking successfully")
    
    print("............................................................")
    print("Booking details")
    print("............................................................")
    print("Passenger Name",pname)
    print("passenger age",page)
    print("contact",pcon)
    print("boarding date",boarding_date)
    print("departing place",depart)
    print("arriving place",arrival)
    print("ticket number",ticket_number)
    print("............................................................")
    
""".................Asansol to Kolkata Bus Booking Code................."""
def bus2(connection,cur):
    pname = input("Enter passenger name :")
    page = int(input("Enter passenger age :"))
    pcon = int(input("Enter thr contact number :"))
    date_components =input('Enter the boarding date (YYYY-MM-DD):').split('-')
    year, month, day = [ int(item) for item in date_components ]
    boarding_date = date(year,month,day)
    depart ="Asansol"
    arrival ="Dhanbad"    
    ticket_number = ''.join(random.choices(string.ascii_uppercase+string.digits,k=7))
    query = "insert into bus2(passenger_name,passenger_age,contact,booking_date,departure,arrival,ticket_number) values(%s,%s,%s,%s,%s,%s,%s)"
    values =(pname,page,pcon,boarding_date,depart,arrival,ticket_number)
    cur.execute(query,values)
    connection.commit()
    print("Bus booking successfully")
    
    print("............................................................")
    print("Booking details")
    print("............................................................")
    print("Passenger Name", pname)
    print("passenger age", page)
    print("contact", pcon)
    print("boarding date", boarding_date)
    print("departing place", depart)
    print("arriving place", arrival)
    print("ticket number", ticket_number)
    print("............................................................")
    
    
"..................................ASASNSOL TO KOLKATA UPDATE PORTAL..................................."
def Bus1Update(connection,cur):
        ticket_number = input("enter your ticket number ")
        query = "select exists(select 1 from bus1 where ticket_number = %s)"
        cur.execute(query,(ticket_number,))
        result = cur.fetchone();
        if(result[0]==1):
            print("Ticket Number Exists")
            pname = input("Enter passenger name :")
            page = int(input("Enter passenger age :"))
            pcon = int(input("Enter thr contact number :"))
            date_components =input('Enter the boarding date (YYYY-MM-DD):').split('-')
            year, month, day = [ int(item) for item in date_components ]
            boarding_date = date(year,month,day)
            depart ="Asansol"
            arrival ="kolkata"   
            updateQuery = "update bus1 set passenger_name = %s, passenger_age = %s, contact = %s, booking_date = %s, departure = %s, arrival = %s where ticket_number = %s "
            values =(pname,page,pcon,boarding_date,depart,arrival,ticket_number)
            cur.execute(updateQuery,values);
            connection.commit();
            
            print("DATA UPDATED SUCCESSFULLY")
            
            print("...............................................................................")
            print("Update booking Details")
            print("...........................................................................")
            print("Passenger Name", pname)
            print("passenger age", page)
            print("contact", pcon)
            print("boarding date", boarding_date)
            print("departing place", depart)
            print("arriving place", arrival)
            print("ticket number", ticket_number)
            print("............................................................")
    
        else:
            print("Ticket Not Found In The Database")
    
" ...............................ASASNSOL TO DHANBAD UPDATE PORTAL........................................."

def Bus2Update(connection,cur):
        ticket_number = input("enter your ticket number")
        query = "select exists(select 1 from bus2 where ticket_number = %s)"
        cur.execute(query,(ticket_number,))
        result = cur.fetchone();
        if(result[0]==1):
            print("Ticket Number Exists")
            pname = input("Enter passenger name :")
            page = int(input("Enter passenger age :"))
            pcon = int(input("Enter thr contact number :"))
            date_components =input('Enter the boarding date (YYYY-MM-DD):').split('-')
            year, month, day = [ int(item) for item in date_components ]
            boarding_date = date(year,month,day)
            depart ="Asansol"
            arrival ="Dhanbad"   
            updateQuery = "update bus2 set passenger_name = %s, passenger_age = %s, contact = %s, booking_date = %s, departure = %s, arrival = %s, where ticket_number = %s "
            values =(pname,page,pcon,boarding_date,depart,arrival,ticket_number)
            cur.execute(updateQuery,values);
            connection.commit();
            print("DATA UPDATED SUCCESSFULLY")
            
            print("...............................................................................")
            print("Update booking Details")
            print("...........................................................................")
            print("Passenger Name", pname)
            print("passenger age", page)
            print("contact", pcon)
            print("boarding date", boarding_date)
            print("departing place", depart)
            print("arriving place", arrival)
            print("ticket number", ticket_number)
            print("............................................................")
        
            
            
        else:
            print("Ticket Not Found In The Database")
            
">>>>>>>>>>>>>>>>>>>>>asansol to kolkata delete<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
            
def Bus1Delete(connection,cur):
    ticket_number =input("enter your ticket number  ")
    query = "select exists(select 1 from bus1 where ticket_number = %s)"
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        deleteQuery = "delete from bus1 where ticket_number = %s"
        cur.execute(deleteQuery,(ticket_number,))
        connection.commit()
        print("deleted successfully")
    
    else:
        print("ticket not found")
        
"<<<<<<<<<<<<<<<<<<<<asansol to dhanbad delete portal>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

def Bus2Delete(connection,cur):
    ticket_number =input("enter your ticket number  ")
    query = "select exists(select 1 from bus2 where ticket_number = %s)"
    cur.execute(query,(ticket_number,))
    result = cur.fetchone();
    if(result[0]==1):
        deleteQuery = "delete from bus2 where ticket_number = %s"
        cur.execute(deleteQuery,(ticket_number,))
        connection.commit()
        print("deleted successfully")
    
    else:
        print("ticket not found")
        
        

        
        
# python mysql connection code
def main():
    connection = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='bus_booking'
        
    )
    cur=connection.cursor()
    if(cur):
        print("CONNECTION ESTABLISHED SUCCESSFULLY")
    else:
        print("CONNECTION ESTABLISHED FAIL")
    
    choice=0
    
    while(choice<=2):
        print(".............WELCOME TO PYTHON TRAVEL AGENCY...............")
        print("1. Asansol to Kolkata")
        print("2. Asansol to Dhanbad")
        print(".............UPDATE PORTAL......................")
        print("3. Asansol to Kolkata Update Booking Details")
        print("4. Asansol to Kolkata Update Booking Details")
        print("5. Asansol to Kolkata delete Details")
        print("6. Asansol to dhanbad delete Details")
        
        print("7. Exit Application")
        choice=int(input("ENTER YOUR JOURNEY CHOICE"))
        
        if(choice==1):
            print("This is booking portal for Asansol to Kolkata")
            bus1(connection, cur)
            
        elif(choice ==2):
            print("This is booking portal for Asansol to Dhanbad")
            bus2(connection, cur)
            
        elif(choice ==3):
            print("This is update booking portal for Asansol to Kolkata")
            Bus1Update(connection, cur)
                  
        elif(choice ==4):
            print("This is update booking portal for Asansol to Dhanbad")
            Bus2Update(connection, cur)
            
        elif(choice ==5):
            print("This is delete portal for Asansol to Dhanbad")
            Bus1Delete(connection, cur)
            
        elif(choice ==6):
            print("This is delete portal for Asansol to Kolkata")
            Bus2Delete(connection, cur)
        
             
        else:
            print("THANKS FOR VISITING US")
main()
