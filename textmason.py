
count = 0
while (count <= 10):
        import smtplib

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("codyberlin@gmail.com", "vagrant22")

        msg = "lame!"
        server.sendmail("codyberlin@gmail.com", "7208783543@txt.att.net", msg)
        server.quit()
