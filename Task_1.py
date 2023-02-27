import timeit

def prime_numbers(s):
    number = 4
    k = 2
    while k < 500:
        f = True
        possible_divisor = 2
        while possible_divisor <= number**0.5:
            if number % possible_divisor == 0:
                f = False
                break
            else:
                possible_divisor += 1
        if f:
            k += 1
            s += str(number)
        number += 1
    return s

def naive(s, pattern):
    k = 0
    for i in range(len(s) - len(pattern) + 1):
        f = True
        for j in range(len(pattern)):
            if s[i + j] != pattern[j]:
                f = False
                break
        if f:
            k += 1
    return k

def RK(s, pattern):
    k = 0
    x = 10
    m = len(pattern) - 1
    H_pattern = 0
    for i in range(len(pattern)):
        H_pattern += int(pattern[i])*x**(m - i)
    for i in range(len(s) - len(pattern) + 1):
        f = True
        H = 0
        for j in range(len(pattern)):
            H += int(s[i + j])*x**(m - j)
        if H == H_pattern:
            for j in range(len(pattern)):
                if s[i + j] != pattern[j]:
                    f = False
                    break
            if f:
                k += 1
    return k

def BM(s, pattern):
    k = 0
    i = len(pattern) - 1
    while i < len(s):
        f = True
        f_counter = True
        for j in range(len(pattern)):
            if s[i - j] != pattern[-j - 1]:
                f_counter = False
                for g in range(j + 1, len(pattern)):
                    if s[i - j] == pattern[-g - 1]:
                        i += g - j
                        f = False
                        break
                if f:
                    i += len(pattern) - j
                break
        if f_counter:
            k += 1
            i += 1
    return(k)

def KMP(s, pattern):
    k = 0
    i = 0
    j = 0
    p_pattern = p(pattern)
    while i < len(s):
        if s[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            k += 1
            j = p_pattern[j-1]
        elif i < len(s) and s[i] != pattern[j]:
            if j != 0:
                j = p_pattern[j-1]
            else:
                i += 1
    return k
 

def p(pattern):
    p_pattern = [0]*len(pattern)
    i = 1
    end = 0
    while i < len(pattern):
        if pattern[i] == pattern[end]:
            end += 1
            p_pattern[i] = end
            i += 1
        else:
            if end != 0:
                end = p_pattern[end - 1]
            else:
                p_pattern[i] = 0
                i += 1
    return p_pattern
                    

s = '23'
s = prime_numbers(s)

numbers_count = [0]*90

print('Самое частовстречающееся двузначное число в строке:')
max_count = 0
max_number = 0
for i in range(10, 100):
    k = naive(s, str(i))
    if k > max_count:
        max_count = k
        max_number = i
print(f'По наивному алгоритму: {max_number}. Оно встретилось {max_count} раз(а)')

max_count = 0
max_number = 0
for i in range(10, 100):
    k = RK(s, str(i))
    if k > max_count:
        max_count = k
        max_number = i
print(f'По алгоритму Рабина-Карпа: {max_number}. Оно встретилось {max_count} раз(а)')

max_count = 0
max_number = 0
for i in range(10, 100):
    k = BM(s, str(i))
    if k > max_count:
        max_count = k
        max_number = i
print(f'По алгоритму Бойера-Мура: {max_number}. Оно встретилось {max_count} раз(а)')

max_count = 0
max_number = 0
for i in range(10, 100):
    k = KMP(s, str(i))
    if k > max_count:
        max_count = k
        max_number = i
print(f'По алгоритму Кнута-Морриса-Пратта: {max_number}. Оно встретилось {max_count} раз(а)')

print()
print('Подсчёт времени работы различных алгоритмов при поиске 90 различных подстрок-двухзначных чисел:')
print()
print('Наивный алгоритм:')
time = timeit.default_timer()
for i in range(10, 100):
    naive(s, str(i))
print(timeit.default_timer() - time)

print()
print('Алгоритм Рабина-Карпа:')
time = timeit.default_timer()
for i in range(10, 100):
    RK(s, str(i))
print(timeit.default_timer() - time)

print()
print('Алгоритм Бойера-Мура:')
time = timeit.default_timer()
for i in range(10, 100):
    BM(s, str(i))
print(timeit.default_timer() - time)

print()
print('Алгоритм Кнута-Морриса-Пратта:')
time = timeit.default_timer()
for i in range(10, 100):
    KMP(s, str(i))
print(timeit.default_timer() - time)

    

