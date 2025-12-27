# Daily Sales Report Generation and Emailing
# import necessary libraries

import os
import datetime
import smtplib
from email.message import EmailMessage

# Collecting sales data from user

product=int(input("How many product you have sold today"))
Products={}
for i in range(product):
    name=input("Enter the product name:")
    price=float(input("Enter the product price:"))
    quantity=int(input("Enter the quantity sold:"))
    Products[name]={'price':price,'quantity':quantity}
totalsales=0
for i in Products:
    sales=Products[i]['price']*Products[i]['quantity']
    totalsales=totalsales+sales
    i=1

# Generating the sales report and writing to a text file
time=datetime.date.today()
with open("Daily_Sales_report.txt",'w') as fs:
    fs.write(f"Daily Sales Report\n")
    fs.write("-----------------------------------------------------\n")
    for i in Products:
        fs.write(f"Product Name: {i}\n")
        fs.write(f"Price: ${Products[i]['price']}\n")
        fs.write(f"Quantity Sold: {Products[i]['quantity']}Pcs.\n")
        sales=Products[i]['price']*Products[i]['quantity']
        fs.write(f"Total Sales for {i}: ${sales}\n")
        fs.write("------------------------------------------------------\n")

    fs.write(f"Total Sales: ${totalsales}\n")
    fs.write("------------------------------------------------------\n")
    fs.write(f"Report Generated on:{time}\n")
    fs.write("------------------------------------------------------\n") 
    
# Sending the sales report via email

with smtplib.SMTP('smtp.gmail.com',587) as s:
    s.starttls()
    s.login('Your Email Address','Your App Password Here') # Replace with your email and app password
    msg=EmailMessage()
    msg['Subject']='Daily Sales Report'
    msg['From']='Sender_Email_Address'  # Replace with the sender's email address
    msg['To']='Recipient_Email_Address'  # Replace with the recipient's email address
    msg.set_content("Please find the attached daily sales report.")

    with open("Daily_Sales_report.txt",'rb') as d:
        filedata=d.read()
        naam=d.name

    msg.add_attachment(filedata, maintype='text', subtype='plain', filename=naam)
    s.send_message(msg)
print("Email sent successfully with the attachment.")