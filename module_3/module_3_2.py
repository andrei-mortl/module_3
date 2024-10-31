def send_email(message, recipient, sender="university.help@gmail.com"):

    if sender == recipient:
        return 'Нельзя отправить письмо самому себе!'

    if sender == "university.help@gmail.com":
        return "Письмо успешно отправлено с адреса", sender,  "на адрес", recipient

    symbols = ('@' and '.com' or '.ru' or '.net')
    a1 = sender
    a2 = recipient
    if not a1.endswith(symbols) and not a2.endswith(symbols):
        return 'Невозможно отправить письмо с адреса', sender, 'на адрес', recipient

    else:
        return "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient

result1 = send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
result2 = send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
result3 = send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
result4 = send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print(result1)
print(result2)
print(result3)
print(result4)
