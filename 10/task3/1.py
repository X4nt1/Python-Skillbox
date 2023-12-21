def found_error():
    if len(list_people) != 3:
        raise IndexError('НЕ присутствуют все три поля')
    elif not list_people[0].isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    elif '@' not in list_people[1] or '.' not in list_people[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и точку')
    elif int(list_people[2]) > 99 or int(list_people[2]) < 10:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


with open('registrations.txt', 'r', encoding='utf-8') as peoples:
    for i_peoples in peoples:
        try:
            list_people = i_peoples.split()
            found_error()
            with open('registrations_good.log', 'a', encoding='utf-8') as good:
                good.write(i_peoples)
        except (IndexError, NameError, SyntaxError, ValueError) as error:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
                bad.write(f'{i_peoples[:-1]}     {error} \n')




