from fbchat import *
def attack():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 80))
    for i in range(0, 100):
        s.sendall(b"Host: " + b"localhost" + b"\n")
        s.sendall(b"GET /" + b"payload" + b" HTTP/1.1\n\n")
    for i in range(10):
        print('Worker: %s' % i)

    s.close()

def spam_sms():
    from twilio.rest import Client
    account_sid = ""
    auth_tokem = ""
    client = Client(account_sid,auth_tokem)

    client.message.create(
        to="+your message",
        from_="+ to person",
        body="message"
    )

def fmap():
    
    client = Client("@gmail.com","")
    if not client.isLoggedIn():
        client.login()
    user =  client.searchForUsers('Arian Atapour')
    user = user[0]
    print("User's ID: {}".format(user.uid))
    print("User's name: {}".format(user.name))
    print("User's profile picture url: {}".format(user.photo))
    print("User's main url: {}".format(user.url))
    session_cookies = client.getSession()
    client.setSession(session_cookies)
    for i in range(0,100):
        client.sendMessage('TE SPAMEZ TAPA merge spammeru facut de mine',thread_id="",thread_type=fbchat.ThreadType.USER)

def smap():
    import smtplib

    # SMTP_SSL Example
    FROM = "@gmail.com"
    TO = "@gmail.com"
    msg = "hello"
    gmail_user = "@gmail.com"
    gmail_pwd = ""
    for i in range(0,30):
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        server_ssl.sendmail(FROM, TO, msg)
        # server_ssl.quit()
        print('successfully sent the mail')
    server_ssl.close()
