def delcp(x):
    arr = ",<>.[]?!/*&^%$@()_-=+:;|"
    for i in arr:
        x = x.replace(i, ' ')
    while "  " in x:
        x = x.replace("  ", " ")
    return x

f = open('text.txt')
text = f.read()
text = delcp(text)
text = text.lower()
text = text.split()

f = open('wiki.txt')
wiki = f.read()
wiki = delcp(wiki)
wiki = wiki.lower()
wiki = wiki.split()

count = 0
p = 0
while p < len(text)-3:
    flag = False
    k = 0
    while k < len(wiki)-3:
        pattern = ''.join(text[p:p+3])
        if pattern == ''.join(wiki[k:k+3]):
            print(pattern, ''.join(wiki[k:k+3]))
            count += len(pattern)
            flag = True
            k += 3
            break
        else:
            k += 1
    if flag == True:
        p += 3
    else:
        p += 1

print(f'Процентное сожержание плагиата в тексте составляет {int(count/len("".join(text))*100)} %.')
        

