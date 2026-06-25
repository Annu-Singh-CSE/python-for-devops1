
# file sending email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

def send_email_python(sender_email,sender_password,receiver_email,subject,body,files):
    msg=EmailMessage()
    msg["From"]=sender_email
    msg["To"]=", ".join(receiver_email)
    msg["Subject"]=subject
    msg.set_content(body)

    for file_path in files:
        try:
            with open(file_path,"rb") as atach:
                msg.add_attachment(
                atach.read(),
                maintype="application",
                subtype="octet-stream",
                filename=file_path.split("/")[-1]
                )
        except Exception as e:
            print("Error :",e)

    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()
        print("Email Sent Successfully...")
    except Exception as e:
        print("Error :",e)


send_email_python(
        files=["stats.txt"],
        sender_email="annusingh12112003@gmail.com",
        receiver_email=["aditya67927@gmail.com","niteshkalangada888@gmail.com","nikhilranjan435@gmail.com"],
        sender_password="onxn jmwo xujy srhu",
        subject="Testing Email Sender Using Pure Python",
        body="Hello ! This email from python programming in IQ",
    )