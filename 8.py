#1
def do_count(num):
    if num == 0:
        return num
    n = do_count(num-1)+1
    print(n)
    return  n


do_count(10)

#2
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def found_key(site, key, level=-1):
    if level == 0:
        return None
    if key in site:
        return site[key]
    for v_site in site.values():
        if isinstance(v_site, dict):
            result = found_key(v_site, key, level - 1)
            return result
    else:
        return None


key = input('Введите искомый ключ: ')
check = input('Хотите ввести максимальную глубину? Y/N: ')
if check.lower() == 'n':
    print(f'Значение ключа: {found_key(site, key)}')
else:
    level = int(input('Введите максимальную глубину: '))
    print(f'Значение ключа: {found_key(site, key, level)}')

#3
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def found_key(site, key, value):
    if key in site:
        site[key] = value
        return site
    for v_site in site.values():
        if isinstance(v_site, dict):
            result = found_key(v_site, key, value)
            if result:
                return site
    else:
        return None


num = int(input('Сколько сайтов: '))
goods = {}
for _ in range(2):
    name = input('Введите название продукта для нового сайта: ')
    keys = {'title': f'Куплю/продам {name} недорого', 'h2': f'У нас самая низкая цена на {name}'}
    for i in keys:
        found_key(site, i, keys[i])
    site_copy = copy.deepcopy(site)
    goods[name] = site_copy
    for good in goods:
        print(good)
        print(f'Сайт для {goods[good]}:')

#4
def sum(*args, count=0):
    if isinstance(args[0], list):
        for arg in args[0]:
            if isinstance(arg, list):

                count = sum(arg, count=count)
                return count
            else:
                count += arg
    else:
        for arg in args:
            count += arg
        return count


print(sum(1, 2, 3, 4, 5))
print(sum([[1, 2, [3]], [1], 3]))

#5
def f(*args, f = 0):
    print(f)
f('a',f=4)