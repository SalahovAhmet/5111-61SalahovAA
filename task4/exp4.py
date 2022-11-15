vowels = 'aeiou'
question = input("Введите букву латинского алфавита: ")
if vowels.upper().__contains__(question.upper()):
    print('Гласная')
elif question == 'y' or question == 'Y':
    print('И гласная, и согласная')
else:
    print('Вы ввели согласную букву')
