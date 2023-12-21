numbers_file = open('numbers.txt', 'r', encoding = 'utf-8')
numbers = numbers_file.read().split()
summ = 0
for numb in numbers:
    summ += int(numb)
numbers_file.close()
sum_file = open('answer.txt', 'w')
sum_file.write(str(summ))
sum_file.close()