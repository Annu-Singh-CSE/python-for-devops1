# #!/usr/bin/env python3

# import os
# import smtplib
# from email.mime.text import MIMEText
# from dotenv import load_dotenv

# load_dotenv()

# SENDER_EMAIL = os.getenv("SENDER_EMAIL")
# SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
# RECEIVER_EMAIL = ["nikhilranjan435@gmail.com"]

# msg = MIMEText("This is a testing Email for SSH MONITORING")
# msg["Subject"] = "Test ANNU - SSH MONITOR SETUP"
# msg["From"] = SENDER_EMAIL
# msg["To"] = ",".join(RECEIVER_EMAIL)

# try:
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)
#         server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
#         print("[OK] Test Email Working...")
# except Exception as e:
#     print(f"[ERROR] Email failed: {e}")




#foe system log generate

#!/usr/bin/env python3
import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

LOG_FILE="/var/log/auth.log"
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = ["nikhilranjan435@gmail.com"]

def build_email_body(username,ip_address,method,timestamp):
    return f"""
    User : {username}
    From IP : {ip_address}
    Method :{method}
    time : {timestamp}
    """

def send_email(username,ip_address,method,timestamp):
    subject=f"SSH Login Alert {username} Logged in......."
    body=build_email_body(username,ip_address,method, timestamp)
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=SENDER_EMAIL
    msg["To"]=",".join(RECEIVER_EMAIL)


    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print(f"[OK] mail sent for {username} - {ip_address} to {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"[ERROR] Email failed : {e}")

def check_log_for_login(line):
    if "Accepted" not in line:
        return

    words=line.split()

    try:
        accepted_index=words.index("Accepted")
        method =words[accepted_index+1]
        username=words[accepted_index+3]
        ip_address=words[accepted_index+5]
    except Exception as e:
        return
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_email(username,ip_address,method,timestamp)

def watch_log():
    print(f"I am watching .......{LOG_FILE}")
    with open(LOG_FILE,"r") as f:
        f.seek(0,2)


        while True:
            line=f.readline()
            if not line:
                time.sleep(1)
                continue
            check_log_for_login(line)

if __name__ == "__main__":
    watch_log()


sudo vim /etc/systemd/system/ssh-monitor.service   

[Unit]
Description = SSH LOGIN MONITORING SERVICE
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu
ExecStart=/usr/bin/python3 /home/ubuntu/ssh_monitor.Py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target


sudo systemctl dae mon-reload
sudo systemctl enable ssh-monitor.service
sudo systemctl start ssh-monitor.service
sudo systemctl status ssh-monitor.service
sudo systemctl stop ssh-monitor.service
sudo journalctl -u ssh-monitor.service -f (-f all ek saath dikhayega) // LOG CHECK KRNE KE LIYE



