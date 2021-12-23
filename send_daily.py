from config import * 

ref = db.reference('/')

feedback = ref.get()


#Fuction to send mail
def send_message(email, daily):

    # Settings
    mail_sender = f'{LOGIN}'
    mail_receiver = f'{email}'
    username = f'{LOGIN}'
    password = f'{PASSWORD}'
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Content of mail
    subject = 'Письмо от Megafon'
    body = f'Новые заявки за сутки:\n\n{daily}'
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # Sending mail
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver, msg.as_string())
    server.quit()




def main():
    daily = ''

    for i in range(feedback['feedback']['count']):
            if feedback['feedback']['data'][i]['status'] == 0:
                daily += f"Имя: {feedback['feedback']['data'][i]['name']}\nПочта: {feedback['feedback']['data'][i]['email']}\nКомментарий: {feedback['feedback']['data'][i]['comment']}\nВремя отправки заявки: {feedback['feedback']['data'][i]['time_added']}\n\n"
                
                user = db.reference(f"{feedback['feedback']['data'][i]['status']}")
                user.update({
                    'status': 1
                })
    send_message(MAIL_TO, daily)


if (__name__ == "__main__"):
    main()