# Задание 1
# Пользователь вводит строку, которая состоит из слов, разделенных пробелами.
# Определите и выведите на экран, сколько в ней слов. Используйте для решениязадачи функцию count()

random_words = input('Введите строку: ')
print(random_words.count(' '))

print('\n' + '=' * 25 + '\n')

# Задание 2
# Пользователь вводит, отдельно (на разных строках), строку s и один символ ch. Необходимо выполнить поиск в строке s всех символов ch.

stroka = input('Введите строку: ')
num = 0

while True:
    index = stroka.find('ch', num + 1)
    num = index
    if index != -1:
        print(index, end= ' ')
    else: 
        break

print('\n' + '=' * 25 + '\n')

# Задание 3

while True:
    stroka = input('Введите строку: ')
    
    if len(stroka) < 5:
        print('Wrong, try again...')
        continue
    else:
        print('третий символ этой строки: ' + stroka[2])
        print('предпоследний символ этой строки: ' + stroka[-1])
        print('первые пять символов этой строки: ' + stroka[:5])
        print('всю строку, кроме последних двух символов: ' + stroka[:-2])
        print('все символы c четными индексами: ' + stroka[2::2])
        print('все символы c нечетными индексами: ' + stroka[1::2])
        print('все символы в обратном порядке: ' + stroka[::-1])
        print('все символы строки через один в обратном порядке, начиная c последнего: '+ stroka[-1::-2])
        print(f'выведите длину данной строки: {len(stroka)}')
        break

print('\n' + '=' * 25 + '\n')

# Задание 4
# Пользователь вводит строку. Замените в этой строке все появления буквы h на букву H, 
# кроме первого и последнего вхождения данной буква в строку.

stroka = input('Введите строку: ')
print(stroka[:1] + stroka[1:-1].replace('h', 'H') + stroka[:-2:-1])




