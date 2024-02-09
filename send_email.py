import smtplib, ssl

host = 'smtp.gmail.com'
port = 465

password = 'kkgldrsmpiabcwwk'
username = 'jkalamaszek@gmail.com'

receiver = 'jkalamaszek@gmail.com'
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as serve:
    serve.login(username, password)
    serve.sendmail(username, receiver, message)