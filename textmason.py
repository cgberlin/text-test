
count = 0
while (count <= 3):
        import smtplib
        count += 1
        print(count)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cgspamtext@gmail.com", "transcend123")

        msg = "let me know if this worked kthanx"
        server.sendmail("cgspamtext@gmail.com", "4242234443@messaging.sprintpcs.com", msg)
        server.quit()
