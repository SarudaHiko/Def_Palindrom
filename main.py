def de(text):
    text = text.lower()
    text = text.replace(' ', '')
    if text == text[::-1]:
        print('Ваш текст является палиндромом')
    # elif text == '':
    #     print('Ничего не введено')
    #     de(input('Введите любой текст: \n'))
    else:
        print('Ваш текст не является палиндромом')


de(input('Введите любой текст: \n'))
