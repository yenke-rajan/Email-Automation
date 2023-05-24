#importing library for sending emails with our gmail account
import smtplib

#creating function
def SendEmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    #variable named as server
    #using gmail as host
    #587 is port used to send emails
    
    server.starttls()
    #initiating tls mode from gmail server
    
    server.login('Gmail','Password')
    #logging in to our gmail account
    #passing email and password as parameters
    
    server.sendmail('SenderMail', 'ReceiverMail', 'message')
    #sending the mail
    
    server.close()

SendEmail()