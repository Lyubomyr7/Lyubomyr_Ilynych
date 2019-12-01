# 1.  Спробуйте переписати наступний код через map.
# Він приймає список реальних імен і замінює їх хеш-прізвищами,
# використовуючи  більш надійний метод-хешування.

# names = ['Sam', 'Don', 'Daniel']
# # for i in range(len(names)):
# #     names[i] = hash(names[i])
# # print(names)
#
# names1 = map(hash,names)
# print(list(names1))



# 2.  Вивести список кольору “red”, який найчастіше зустрічається в даному списку
# [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ]
# використовуючи функцію filter.

# color = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow" ]
#
# color1 = filter( lambda n:n=="red" ,color)
# print(list(color1))
#


# 3. Всі ці числа в списку мають стрічковий тип даних,
#  наприклад  [‘1’,’2’,’3’,’4’,’5’,’7’], перетворити цей список  в список,
# всі числа якого мають тип даних integer:
# 1)  використовуючи метод  append
# 2)  використовуючи метод  map

#number = ["1","2","3","4","5","7"]
# number_append =[]
# #!!!!!!!!!!!!!! Append!!!!!!!!!!!!!!
# for i in number:
#     i=int(i)
#     number_append.append(i)
# print(number_append)
# #!!!!!!!!!!!!! Map !!!!!!!!!!!!!!!!!!!!!!!
#number_int = map(int,number)
#print(list(number_int))


# 4. Перетворити список, який містить милі ,
# в список, який містить кілометри (1 миля=1.6 кілометра)
#    a) використовуючи функцію map
#    b) використовуючи функцію map та lambda
# miles= [1.6, 2.7, 5.5, 1.2 ]
#
# """ Map"""
# def mile(mil):
#     return mil*1.6
# miles_map = map(mile,miles)
# print(list(miles_map))
#
# """Map and lambda"""
# miles_map_lambda = map(lambda n:n*1.6,miles)
# print(list(miles_map_lambda))


# 5. Знайти найбільший елемент в списку  використовуючи функцію reduce
# from functools import reduce
# elements = [2, 4, 8, 1]
# reduce_max =reduce(lambda x,y: max(x,y), elements)
# print(reduce_max)


# 6. Перепишіть наступний код, використовуючи map,
# reduce і filter. Filter приймає функцію і колекцію.
# Повертає колекцію тих елементів, для яких функція повертає True.

people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}]
height_total = 0
height_count = 0
# for person in people:
#     if 'height' in person:
#         height_total += person['height']
#         height_count += 1
# print(height_total)

def per(person):
    if 'height' in person:
        return person['height']

people_height = filter(per,people)
list(people_height)





