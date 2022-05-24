

from unicodedata import name
from flask import Flask, render_template,request
import requests
import smtplib
from email.message import EmailMessage

my_email ="akashudayhulekal@gmail.com"
password ="pokemonpikachu"
other_email ="akashuhulekal@gmail.com"

app=Flask(__name__)


data_1=requests.get("https://api.npoint.io/ed99320662742443cc5b")
data_1.raise_for_status
data=data_1.json()

@app.route("/")
def main_page():

    return render_template("index.html",data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


    

@app.route("/post/<num>")
def post_page(num):
    return render_template("post.html",data=data,number=num)  
 


     

@app.route("/contact")
def contact_page():
    return render_template("contact.html")  



@app.route("/contacts",methods=["GET", "POST"])
def receive_data():
        if request.method == "POST":
            data = request.form
            name_1=data["name"]
            email_1=data["email"]
            phone_1=data["phone"]
            message_1=data["message"]
            msg = EmailMessage()
            msg.set_content(f"Name:{name_1} email:{email_1} message:{message_1} phone:{phone_1}")

            msg['Subject'] ='from your website'
            msg['From'] ="akashudayhulekal@gmail.com"
            msg['To'] ="akashuhulekal@gmail.com"

                # Send the message via our own SMTP server.
            with smtplib.SMTP('smtp.gmail.com', port=587) as server:
                server.starttls()
                server.login(my_email, password=password)
                server.send_message(msg)
                server.close()
            return render_template("contact.html", message="Successfully sent your message.")
        else:
            return render_template("contact.html")
   
        

 


  









if __name__=="__main__":
    app.run(debug=True)    

