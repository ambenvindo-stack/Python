#import email
import smtplib
import os

email_id = os.environ.get('ambenvindo@gmail.com')
email_pass = os.environ.get("626M3xAK")

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  #587 is port number
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    # ehlo is an alternative to helo for services that support the smtp services extensions
    # in any case helo or ehlo is must command for the smtp clien tp commerce a mail transfer

    smtp.login(email_id,email_pass)

    subject = 'Fight against Corinavirus'   #subject which comes in email
    body = "Hey,  hi let's fight against coronavirus by staying at home"

    msg = f'Subject : {subject}\n\n\n{body}'
    smtp.sendmail(email_id, 'ambenvindo@gmail.com', msg)

    # format here is sender's mail id --- receiver's mail id, =--- msg

