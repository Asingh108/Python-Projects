import smtplib as s

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(subject,body,to_email):
# user email details--->
    from_email = "user@gmail.com"
    password = "User_password"

# creating the email--->
    msg = MIMEMultipart()
    msg['From'] = from_email #user email
    msg['To'] = to_email #a person email you wants to send mail
    msg['Subject'] = subject #represent subject of the mail

# Attach the email body--->
    msg.attach(MIMEText(body,"plain")) #body of the mail

#connect to server and send email--->
    try:
        server = s.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send the email: {e}")

#Example usage
send("Test Python", "I Love Python 3000", "example@gmail.com")
