
def send_mail(message,recipent,sender="university.help@gmail.com"):
    if "@" not in sender and recipent or not sender.endswith((".com",".ru",".net")) or not recipent.endswith((".com",".ru",".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipent}")
        return
    elif sender == recipent:
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipent}")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipent}")

send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


