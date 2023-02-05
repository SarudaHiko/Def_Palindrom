def de(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        print('Ваш текст является палиндромом')
    else:
        print('Ваш текст не является палиндромом')


de(input('Введите любой текст: \n'))
