import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#please note go to https://myaccount.google.com/lesssecureapps and
#turn it off to allow gmail to send
sender_email_id = 'jeandreross@gmail.com'
receiver_email_id = ['calvertjustin1996@gmail.com', 'thapelo@lifechoices.co.za', 'abdullah.isaacs@gmail.com']
password = input("Enter your password:")
subject="Greetings"
msg=MIMEMultipart()
msg['From']=sender_email_id
msg['To']="," .join(receiver_email_id )
msg['Subject']=subject
body = "This is a tester!"
body = body + "I hope this works!"
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()

