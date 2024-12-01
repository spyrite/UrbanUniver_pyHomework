sender_default = 'university.help@gmail.com'


def send_email(message, recipient, *, sender=sender_default):
    if not email_is_correct(recipient) or not email_is_correct(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
    if recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
        return
    if sender == sender_default:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return


def email_is_correct(email):
    domain_global = '.' + email.split('.')[-1]
    conditions = ['@' in email, domain_global == '.com' or domain_global == '.net' or domain_global == '.ru']
    if all(conditions):
        return True
    return False


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
