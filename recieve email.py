import imaplib
import email
from email.message import EmailMessage
from email.header import decode_header
import os

def login(email1, pswd):
    #connect to server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    #login to server
    mail.login(f'{email1}', f'{pswd}')
    mail.select('INBOX')
    return mail

def decodehead(mailheader):

    #if its empty just return it empty
    if not mailheader:
        return ""
    
    #splits it into parts with its different encodings and gives a tuple as [(part, encoding), (part, encoding)]
    decoded_parts= decode_header(mailheader)
    decoded_str=""

    
    #decodes the parts, if no encoding given utf-8 by default, if its a string it just is added
    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            decoded_str += part.decode(encoding or 'utf-8', errors='ignore')
        else:
            decoded_str += part 
    return part

def extract_email_info(msg):
    subject = decodehead(msg.get('Subject'))
    from_ = decodehead(msg.get('From'))

    body=""

    attachments=[]

    if msg.is_multipart():
        





#returns two values, result and data in email ids server side in byte strings.
result, data = mail.search(None, 'UNSEEN')

data=data[0].split()

for i in data:
    rawmail = mail.fetch(i.decode(), "(RFC882)") 



