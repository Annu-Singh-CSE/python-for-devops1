import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_python(sender_email,sender_password,receiver_email,subject,body):
    msg=MIMEMultipart()
    msg["From"]=sender_email
    msg["To"]=receiver_email
    msg["Subject"]=subject

    msg.attach(MIMEText(body,"plain"))

    try:
        server=smtplib.SMTP("smtp.gmail.com",587) # 578 ka use krkr tls use kiye h
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()
        print("email sent succesfully.....................")
    except Exception as e:
        print("Error :",e)    

send_email_python(
  sender_email="annusingh12112003@gmail.com",
  receiver_email="niteshkalangada888@gmail.com",
  sender_password="onxn jmwo xujy srhu",  #It take also google app account copy 
  subject="Testing Email Sender Using Pure Python",
  body="Hello ! This Email From Python Programming"   
)        


