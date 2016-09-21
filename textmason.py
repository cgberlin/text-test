import sys
import smtplib

try:
    number = sys.argv[1]
    msg = sys.argv[2]
    carrier = sys.argv[3]
    amountToText = int(sys.argv[4])
    userGmail = sys.argv[5]
    userPassword = sys.argv[6]
    theirEnteredPass = sys.argv[7]
    print(number)
except IndexError:
    print("somethings wrong")
if theirEnteredPass == "LASAGNA":
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(userGmail, userPassword)

else:
    print('fail')
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
        try:
            server.sendmail(userGmail, number + carrier, msg)
        except smtplib.something.senderror, errormsg:
            raise SendError("Couldn't send message: most likely overtried")
else:
    print("too many texts")
server.quit()
