import smtplib

from email.message import EmailMessage

psw= input("Enter your app password:\t")
mail= input("Enter your email:\t")

def get_message(fr0m, to, subject, mssg):
   messg = EmailMessage()
   messg['From'] = f"{fr0m}"
   messg['To'] = f"{to}"
   messg['Subject'] = f"{subject}"
   messg.set_content(f"{mssg}")
   return messg

def get_data(fr0m):
   sub= input("Enter the subject of your Email:\t")
   to= input("Enter the Email address of who you want to send the mail to:\t")
   contents = input("Enter the contents of your message:\t")
   data=[fr0m, to, sub, contents]
   return data

def server_connect(x):
   server = smtplib.SMTP('smtp.gmail.com', '587')
   server.starttls()
   server.login(f'{mail}', f'{psw}')
   server.send_message(x)
   server.quit()
   print("Mail Successfully sent!")

ch=1
while ch==1:
   data=get_data(mail)
   x=get_message(data[0], data[1], data[2], data[3])
   server_connect(x)

   ch=int(input('Would you like to send another email? (1- yes, 2- no):\t'))
   if ch==2:
      break
