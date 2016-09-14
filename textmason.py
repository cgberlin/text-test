import sys
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("cgspamtext@gmail.com", "transcend123")

try:
    number = sys.argv[1]
    msg = sys.argv[2]
    carrier = sys.argv[3]
    amountToText = int(sys.argv[4])
    print(number)
except IndexError:
    print("somethings wrong")
if carrier == "att":
    carrier = "@txt.att.net"
    print(carrier)
elif carrier == "sprint":
    carrier = "@messaging.sprintpcs.com"
    print(carrier)
elif carrier == "verizon":
    carrier = "@vtext.com"
    print(carrier)
elif carrier == "tmobile":
    carrier = "@tmomail.net"
    print(carrier)
else:
    print("err")
count = 0
if amountToText <= 300:
    while (count <= amountToText):
        count += 1
        print(count)
        server.sendmail("cgspamtext@gmail.com", number + carrier, msg)
else:
    print("too many texts")
server.quit()
