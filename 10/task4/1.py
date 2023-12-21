name = input('Введите имя пользователя: ')
while True:
    print('1. Посмотреть текущий текст чата.\n2. Отправить сообщение (затем вводит сообщение).')
    check = int(input('Выберите действие '))
    if check == 1:
        try:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                for message in chat:
                    print(message)
        except FileNotFoundError:
            print('Чат еще пустой')
    elif check == 2:
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as chat:
            chat.write(f'{name}: {message}\n')
    else:
        print('Введите корректную команду!')



