import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 587
    
    username = "" # Enter your email here
    password = "" # Enter your password here
    
    receiver = "" 
    context = ssl.create_default_context()
    
    with smtplib.SMTP(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)