employees_num = int(input('Введите число сотруднников, которые отправляются домой:  '))
sum = 0
distance_list = []
price_list = []
for i in range(employees_num):
    distance = int(input('Введите расстояние до дома {0}-го сотрудника в км: '.format(i+1)))
    distance_list.append(distance)
for i in range(employees_num):
    price = int(input('Введите тариф {0}-го такси за 1 км:  '.format(i+1)))
    price_list.append(price)
c_distance_list = distance_list[:]
c_price_list = price_list[:]
index_list_d = []
index_list_p = []

max_distance = 0
for i in range(employees_num):
    index = c_distance_list.index(max(c_distance_list))
    index_list_d.append(index)
    c_distance_list[index] = 0
for i in range(employees_num):
    index = c_price_list.index(min(c_price_list))
    index_list_p.append(index)
    c_price_list[index] = 10**10

print('Такси для клиента 1, 2, 3, ...:')
for i in range(employees_num):
    taxi_num = index_list_p[index_list_d.index(i)]
    print(taxi_num+1)
for i in range(employees_num):
    sum += distance_list[index_list_d[i]]*price_list[index_list_p[i]]
print('Необходимо всего заплатить:')
W1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
W3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
W4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
W5 = ["тысяча", "тысячи", "тысяч"]
W6 = ["рубль", "рубля", "рублей"]

a1 = sum // 100000
a2 = (sum // 10000) % 10
a3 = (sum // 1000) % 10
a4 = (sum // 100) % 10
a5 = (sum // 10) % 10
a6 = sum % 10

poz = ""
if a1 != 0:
    i1 = a1 - 1
    poz += W4[i1] + " "

if a2 == 1 and a3 == 0:
    poz += W3[0] + " "

if a2 != 1:
    if a2 != 0:
        i2 = a2 - 1
        poz += W3[i2] + " "

if a3 != 0:
    if a2 == 1:
        i3 = a3 - 1
        poz += W2[i3] + " " + W5[2] + " "
    else:
        i3 = a3 - 1
        poz += W1b[i3] + " "
        if a3 == 1:
            poz += W5[0] + " "
        elif 1 < a3 < 5:
            poz += W5[1] + " "
        else:
            poz += W5[2] + " "

if (a3 == 0) and (a2 or a1 != 0):
    poz += W5[2] + " "

if a4 != 0:
    i4 = a4 - 1
    poz += W4[i4] + " "

if a5 == 1 and a6 == 0:
    poz += W3[0] + " "

if a5 != 1:
    if a5 != 0:
        i5 = a5 - 1
        poz += W3[i5] + " "

if a6 != 0:
    if a5 == 1:
        i6 = a6 - 1
        poz += W2[i6] + " " + W6[2]
    else:
        i6 = a6 - 1
        poz += W1a[i6] + " "
        if a6 == 1:
            poz += W6[0] + " "
        elif 1 < a6 < 5:
            poz += W6[1] + " "
        else:
            poz += W6[2] + " "

if (a6 == 0) and (a5 or a4 or a3 or  a2 or a1 !=0):
    poz += W6[2]

poz = poz.capitalize()
print(poz)

