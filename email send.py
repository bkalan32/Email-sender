from email.message import EmailMessage
from theone import password
import ssl
import smtplib

email_sender = '@gmail.com'
email_password = password

email_receiver = 'hocoho1561@fsouda.com'

subject = "You're a millionaire"
body = """
Stay discplined.  The world is yours already.
"""
# Instance
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
            

