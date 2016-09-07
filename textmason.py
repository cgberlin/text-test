
count = 0
while (count <= 3):
        import smtplib
        count += 1
        print(count)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cgspamtext@gmail.com", "transcend123")

        msg = "let me know if this worked kthanx"
        server.sendmail("codyberlin@gmail.com", "7208783543@txt.att.net", msg)
        server.quit()
