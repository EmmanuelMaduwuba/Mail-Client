import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import *


fromaddr = "" #Fill in the sender's address here
toaddr = ""  #Fill in the recipient address here

password = input("password: ") #asks user for password 
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing email"
 
body = "If you are seeing this text in your email then the smtp was successful!"  #text that will appear in email
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "file.jpg"  #the image name
attachment = open("/home/emmanuel/Pictures/Screenshot from 2019-03-31 14-30-24.png", "rb") #absolute path of the image, you can replace it with yours
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename) #adding header to the attachment
 
msg.attach(part)  #combining the header with the message body
 
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #SSL Port used
server.set_debuglevel(1)
server.ehlo()
server.login(fromaddr, password) 
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()