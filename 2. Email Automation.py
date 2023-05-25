#email automation 

#importing library for sending emails with our gmail account
import smtplib

#asking user to enter email address of receiver
to=input("Enter the email of receiver: ")

#asking for message to send
message=input("Enter the message: ")

#creating function
def SendEmail(to, message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    #variable named as server
    #using gmail as host
    #587 is port used to send emails
    
    server.starttls()
    #initiating tls mode from gmail server
    
    server.login('sender_email','password')
    #logging in to our gmail account
    #passing email and password as parameters
    
    server.sendmail('sendermail', to, message)
    #sending the mail
    
    server.close()
    #server is closed
   
SendEmail(to, message)
    #recommended to use new gmail for testing purposes