import sys

try:
    number = sys.argv[1]
    msg = sys.argv[2]
    print(number)
except IndexError:
    print("somethings wrong")
count = 0
while (count <= 30):
        import smtplib
        count += 1
        print(count)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("cgspamtext@gmail.com", "transcend123")
        
        server.sendmail("cgspamtext@gmail.com", number + "@txt.att.net", msg)
        server.sendmail("cgspamtext@gmail.com", number + "@messaging.sprintpcs.com", msg)
        server.sendmail("cgspamtext@gmail.com", number + "@vtext.com", msg)
        server.quit()
