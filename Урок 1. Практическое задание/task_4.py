"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

users = {
    'Vasyan': [12345, True],
    'Denis': [111, False],
    'Anna': ['password', False],
    'Max': ['login', True]
 }

def checkAuth ():
    userName = input('Пожалуйста введите логин: ')

    if userName not in users.keys():
        return print('Пользователь с таким логином не найден')
    else:
        print('привет: ', userName)

    profile = users[userName]
    passwd = input('Пожалуйста введите пароль: ')

    pwdCheck = False


    if str(profile[0]) != passwd:
        for i in range(2):
            passwd = input('Неверный пароль, пожалуйста введите пароль заново: ')
            if passwd != str(profile[0]):
                continue
            else:
                pwdCheck = True
                break
    else:
        pwdCheck = True

    if pwdCheck:
        print('Авторизация пройдена')
        print('====================')
        print('Проверка статуса учетной записи....')

        if profile[1]:
            print("Учетная запись активна, добро пожаловать!")
        else:
            print("Учетная запись неактивна, просьба пройти процедуру активации")
    else:
        print('с 3х раз не вспомнил пароль....')
        print('ПОШЕЛ ВОН C МОЕГО САЙТА!')

checkAuth()