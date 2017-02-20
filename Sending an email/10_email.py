import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Hello, it\'s me from feature!!!')
msg['Subject'] = 'I learn Python!'

content = 'Hello, it\'s me from feature!!!'

mail = smtplib.SMTP('smtp.gmail.com', 587)  # or 465 (google said :Сервер исходящей почты), but not working thou :)

mail.ehlo()

mail.starttls()  # Transport Layer Security

mail.login('pavlo.olshansky@gmail.com', 'enter_your_pass_here')  # !!!!!!

mail.sendmail('pavlo.olshansky@gmail.com', 'oleholshanskyi@gmail.com', msg.as_string())  # roman.olshansky123@gmail.com
mail.close()

'''
TO SEND FILES: EXAMPLE
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()
