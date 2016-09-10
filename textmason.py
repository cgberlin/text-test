import sys

try:
    number = sys.argv[1] + "@messaging.sprintpcs.com"
    print(number)
except IndexError:
    print("somethings wrong")
count = 0
while (count <= 3):
        import smtplib
        count += 1
        print(count)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cgspamtext@gmail.com", "transcend123")

        msg = "test!!!"
        server.sendmail("cgspamtext@gmail.com", number, msg)
        server.quit()
