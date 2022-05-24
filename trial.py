import smtplib
from email.message import EmailMessage

my_email ="akashudayhulekal@gmail.com"
password ="pokemonpikachu"
other_email ="akashuhulekal@gmail.com"



msg = EmailMessage()
msg.set_content(f"sasa")

msg['Subject'] ='from your website'
msg['From'] ="akashudayhulekal@gmail.com"
msg['To'] ="akashuhulekal@gmail.com"

    # Send the message via our own SMTP server.
with smtplib.SMTP('smtp.gmail.com', port=587) as server:
    server.starttls()
    server.login(my_email, password=password)
    server.send_message(msg)
    server.close()