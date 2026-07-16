#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from datetime import datetime,timedelta

HISTORY_FILE="/home/ubuntu/.bash_history"
SENDER_EMAIL="annusingh12112003@gmail.com"
SENDER_PASSWORD="onxn jmwo xujy srhu"
RECEIVER_EMAIL=["niteshkalangada8@gmail.com"]
HOURS_BACK=24

def get_commands():
    cutoff=datetime.now() - timedelta(hours=HOURS_BACK)
    commands=[]
    current_timestamp=None
    with open(HISTORY_FILE,"r",errors="ignore") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            if line.startswith("#"):
                try:
                    epoch_value=int(line[1:])
                    current_timestamp=datetime.fromtimestamp(epoch_value)
                except ValueError:
                    current_timestamp=None
            else:
                if current_timestamp and current_timestamp >= cutoff:
                    commands.append((current_timestamp,line))
                current_timestamp=None
                
    return commands

def make_email_body(commands):
    if not commands:
        return "No Commands found in 24 HOURS "
    lines =[f"-----Total Commands: {len(commands)}\n------"]
    for i , (time,cmd) in enumerate(commands,start=1):
        lines.append(f" * {i}. [{time.strftime("%H:%M:%S")}] {cmd} ")
    return "\n".join(lines)

def send_email(commands):
    subject=f"========Daily Commands Summary========="
    body=make_email_body(commands)
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=SENDER_EMAIL
    msg["To"]=", ".join(RECEIVER_EMAIL)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
            server.login(SENDER_EMAIL,SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL,RECEIVER_EMAIL,msg.as_string())
            print(f"[OK] Mail sent to {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"[ERROR] Email Failed : {e}")

if __name__name=="__main__":
    commands=get_commands()
    send_email(commands)