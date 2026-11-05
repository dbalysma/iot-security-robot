# [2026] Recovered from an email of 15 June 2023. Only the account addresses and the app password
# below were replaced with REDACTED before publishing; nothing else was changed.
from time import sleep
import time
import os
import smtplib
from datetime import datetime
import datetime
from picamera import PiCamera
import picamera
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

SMTP_USERNAME = 'REDACTED'
SMTP_PASSWORD = 'REDACTED'  # [2026] app password removed                                       #Password given from GOOGLE App Passwords

SENDER_EMAIL = 'REDACTED'
RECIPIENT_EMAIL = 'REDACTED'

def take_photo(folder_path):
    camera = picamera.PiCamera()
    
    try:
        #camera = PiCamera()
        camera.start_preview()
        sleep(2)

        today_date = datetime.date.today()
        current_time = time.strftime('%H:%M:%S')

        file_name = f"{current_time}.jpg"
        file_path = os.path.join(folder_path, file_name)
        
        camera.capture(file_path)
        print("Image Captured on:", today_date, "at", current_time, "and saved too", file_path)
    
        return file_path
    
    finally:
        camera.stop_preview()
        camera.close()


def send_email(file_path, message):
    msg = MIMEMultipart()
    msg['From'] = 'REDACTED'
    msg['To'] = 'REDACTED'
    msg['Subject'] = 'Movement Detected From your Robot'
    
    with open(file_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename = os.path.basename(file_path))
        msg.attach(img)
        msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SMTP_USERNAME, 'REDACTED')  # [2026] app password removed
    server.send_message(msg)
        
    print("Email successfully sent!")

def main():
    
    folder_path = "/home/dylan/MobileSec/Logs"
    file_path = take_photo(folder_path)
    message = "Hi, There was motion was detected in the area. Here's the picture taken."
    
    send_email(file_path, message)

if __name__ == "__main__":
    main()