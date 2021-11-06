
alfavit_UA = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ1234567890*()/ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*/'
krok = int(1)       #крок на який проходитеме зміщення
while True:

    message = input("Повідомлення для шифрування: ").upper()
    itog = ''
    lang = input('Виберіть мову UA/EN: ')


    if lang == 'UA':
        for i in message:
            mesto = alfavit_UA.find(i)
            new_mesto = mesto + krok
            if i in alfavit_UA:
                itog += alfavit_UA[new_mesto]
            else:
                itog += i
    print(itog)