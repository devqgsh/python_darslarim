# Xatolar bilan ishlash
# SyntaxError
# print "Hello World!"          EOFError Funksiyada xato
# print ("Hello World"          EOLError Shu qator oxirida xato bor

#IndetationError
#   print("Hello World")        indent- Shu qatorni boshida bo'sh joylar bor

# print("O\'ngacha sanaymiz")
# for n in range(1, 11):
# print(n)               expected an indented block after-Manashu joyda joy tashamagansan

# RuntimeError
# TypeError
# print("Hello World" + 5)     Shu yerda string va integer ni qo'shib bo'lmaydi

# NameError
# mevalar = ['olma', 'anor', 'banan', 'shaftoli']
# for meva in mvalar:
#     print(meva)                Malum bir ozgaruvhi yo funksiya nomi xato yozilgan

# ValueError
# son = int(input("Son kiriting: "))     10lik son uchun float yozing yoki Butun son kiriting deb so'rang
# if son >= 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")    Butun sonni musbat yoki manfiy ekanligini tekshiradi.Agar foydalanuvchi son o'rniga matn kiritsa, ValueError xatosi yuz beradi.

# IndexError
# mevalar = ['olma', 'anor', 'banan', 'shaftoli']   
# print(mevalar[5])     out of range- Shu yerda 5 index mavjud emas, 0 dan 3 gacha index bor.

# ZeroDivisionError
# x, y = 50, 50
# z = 250/(x-y)          nolga bo\'lish mumkin emas, x-y=0 bo'lgani uchun ZeroDivisionError xatosi yuz beradi.

# Mantiqiy xatolar (Logical Errors)
# radius = 5
# pi = 4.14           
# aylana_yuzi = pi * radius ** 2
# print(aylana_yuzi)           pi ning qiymati 3.14 bo'lishi kerak edi, lekin 4.14 deb yozilganligi sababli natija noto'g'ri chiqadi.

# son = float(input("Son kiriting: "))
# ildiz = son ** 1/2                                 (1/2) skobka ichida bo'lishi kerak edi, lekin skobka tashqarisida yozilganligi sababli natija noto'g'ri chiqadi.
# print (f'{son} ning ildizi {ildiz} ga teng')       yoki 0.5 deb yozish kerak

# mevalar = ['olma', 'anor', 'banan', 'shaftoli']
# for meva in mevalar:
#     print(meva)
#     print('Dastur tugadi')         dastur tugadi print qatori for siklidan tashqarida bo'lishi kerak edi, lekin sikl ichida yozilganligi sababli dastur faqat birinchi meva nomini chiqaradi va sikl tugagach, "Dastur tugadi" xabarini chiqaradi.