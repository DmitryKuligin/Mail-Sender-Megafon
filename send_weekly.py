from config import * 

ref = db.reference('/')

feedback = ref.get()

def send_message(email):
    # Settings
    mail_sender = f'{LOGIN}'
    mail_receiver = f'{email}'
    username = f'{LOGIN}'
    password = f'{PASSWORD}'
    server = smtplib.SMTP('smtp.gmail.com:587')


    # Content of mail
    subject = 'Письмо с новыми заявками'
    body = 'Еженедельная рассылка заявок'
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("./bot/Notes.csv", "r").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename='Notes.csv')
    msg.attach(part)

    # Sending mail
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()


def main():
    data = []

    for i in range(feedback['feedback']['count']):
            if feedback['feedback']['data'][i]['status'] == 1:

                data += [{
                    'name':feedback['feedback']['data'][i]['name'],
                    'email': feedback['feedback']['data'][i]['email'],
                    'comment': feedback['feedback']['data'][i]['comment'],
                    'time': feedback['feedback']['data'][i]['time_added']
                }]

                user = db.reference(f"{feedback['feedback']['data'][i]['status']}")
                user.update({
                    'status': 2
                })


    with open('./bot/Notes.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name','email','comment', 'time'])
        for line in data:
            writer.writerow(line)


    send_message(MAIL_TO)

if (__name__ == "__main__"):
    main()