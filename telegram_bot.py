username = str(input('Как к вам обращаться? '))
current_year = 2023
print(f'Здравствуйте, {username}.')
while True:
    print('1) Записаться на вступительные экзамены\n' '2) Получить подробную информацию на почту')
    user_choice_1 = int(
        input('Введите число соответствующее вашему ответу... '))
    if user_choice_1 == 1:
        print('1) Информаика\n' '2) Математика\n' '3) Литература')
        print(f'{username}, выберите предмет тестирования.')
        test_subject = int(
            input('Введите число соотвествующее вышему выбору... '))
        if test_subject == 1:
            test_date_day = int(input(f'Выберите дату когда вам будет удобно сдать ваше тестирование по предмету Информатика\n'
                                      'День(01-31):'))
            test_date_month = int(input(f'Месяц(01-12):'))
            test_date_year = int(input(f'Год(2023-2025):'))
            if test_date_day == 12 and test_date_month == 11 and test_date_year == 2023:
                print(
                    'Это время уже занято. Попробуйте другое записаться в другое число.')
                continue
            elif test_date_day > 0 and test_date_day < 32 and test_date_month > 0 and test_date_month < 13 and test_date_year > 2022 and test_date_year < 2026:
                print(
                    f'Готово! Вы зарегистрированы на тестирование {test_date_day}.{test_date_month}.{test_date_year} по предмету: Информатика')
                break
            else:
                print('Введите корректную дату')
                continue
        elif test_subject == 2:
            test_date_day = int(input(f'Выберите дату когда вам будет удобно сдать ваше тестирование по предмету Математика\n'
                                      'День(01-31):'))
            test_date_month = int(input(f'Месяц(01-12):'))
            test_date_year = int(input(f'Год(2023-2025):'))
            if test_date_day == 12 and test_date_month == 11 and test_date_year == 2023:
                print('Это время уже занято')
                continue
            elif test_date_day > 0 and test_date_day < 32 and test_date_month > 0 and test_date_month < 13 and test_date_year > 2022 and test_date_year < 2026:
                print(
                    f'Готово! Вы зарегистрированы на тестирование {test_date_day}.{test_date_month}.{test_date_year} по предмету: Математика')
                break
            else:
                print('Введите корректную дату')
                continue
        elif test_subject == 3:
            test_date_day = int(input(f'Выберите дату когда вам будет удобно сдать ваше тестирование по предмету Литература\n'
                                      'День(01-31):'))
            test_date_month = int(input(f'Месяц(01-12):'))
            test_date_year = int(input(f'Год(2023-2025):'))
            if test_date_day == 12 and test_date_month == 11 and test_date_year == 2023:
                print('Это время уже занято')
                continue
            elif test_date_day > 0 and test_date_day < 32 and test_date_month > 0 and test_date_month < 13 and test_date_year > 2022 and test_date_year < 2026:
                print(
                    f'Готово! Вы зарегистрированы на тестирование {test_date_day}.{test_date_month}.{test_date_year} по предмету: Литература')
                break
            else:
                print('Введите корректную дату')
                continue
        else:
            print(
                'Вы выбрали не существующий вариант или ввели текст вместо цифры. Попробуйте сначала.')
            continue
