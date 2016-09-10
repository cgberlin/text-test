
count = 0
while (count <= 100):
        import smtplib
        count += 1
        print(count)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cgspamtext@gmail.com", "transcend123")

        msg = "GAY!!!"
        server.sendmail("cgspamtext@gmail.com", "9168127651@txt.att.net", msg)
        server.quit()
