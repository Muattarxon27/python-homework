# Ikkita son yig‘indisini tekshirish
def yigindi_tekshirish(son1, son2):
    if son1 + son2 > 50.8:
        print("Berilgan ikkita son yig‘indisi 50.8 dan katta.")
    else:
        print("Berilgan ikkita son yig‘indisi 50.8 dan kichik yoki teng.")

# Foydalanuvchidan ikkita son kiritishni so‘rash
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
yigindi_tekshirish(son1, son2)
# Sonning 10 va 20 oralig‘ida ekanligini tekshirish
def oraliq_tekshirish(son):
    if 10 <= son <= 20:
        print("Berilgan son 10 va 20 orasida joylashgan.")
    else:
        print("Berilgan son 10 va 20 orasida emas.")

# Foydalanuvchidan son kiritishni so‘rash
son = int(input("Son kiriting: "))
oraliq_tekshirish(son)