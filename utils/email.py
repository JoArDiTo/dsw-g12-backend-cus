import smtplib
from config import email, pwd

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, pwd)

from_correo = email