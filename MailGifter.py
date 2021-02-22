# This code is under the MIT Licence
import smtplib
import random
import numpy as np


def send_email(subject, body, email_to):
    try:
        email = 'send mail'
        password = 'send pass'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email, password)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(email, email_to, message)
        server.quit()
    except:
        print("an error occurred sending ")


def send_christmas_email(your_name, email):
    send_email('חג מולד שמח!',
               f'{your_name}אתם צריכים לקנות מתנה ל-', email)


def random_pull_name(all_names):
    return random.choice(all_names)


def for_all_members(all_names, emails):
    names = all_names.copy()
    name_length = len(all_names)
    for i in range(name_length):
        temp_names = names.copy()
        try:
            temp_names = np.delete(names, all_names[i])
        except:
            pass
        your_name = random_pull_name(temp_names)
        print(your_name, emails[i])
        #send_christmas_email(your_name, emails[i])
        names = names[names != your_name]


if __name__ == "__main__":
    participants = np.array(['שחר', 'אופיר', 'קארין', 'דיאנה', 'רועי', 'אילה', 'אריאל וסרמן', 'איתמר', 'שליו', 'רון'])

    all_emails = ['shahar.b2901@gmail.com', 'ofirfirsa@gmail.com', 'Skarin4@gmail.com', 'shtbv100111@gmail.com',
                  'roy.arama1@gmail.com', 'hecht.ayala@gmail.com', 'arielthemer@gmail.com',
                  'shalevjef32@gmail.com', '9itamar9@gmail.com', 'ronron.shaham@gmail.com']
    for_all_members(participants, all_emails)

    print("finished successfully")
