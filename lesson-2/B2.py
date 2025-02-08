# Ikkita son tengligini tekshirish
def tenglik_tekshirish(son1, son2):
    if son1 == son2:
        print("Berilgan ikkita son teng.")
    else:
        print("Berilgan ikkita son teng emas.")

# Foydalanuvchidan ikkita son kiritishni so'rash
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
tenglik_tekshirish(son1, son2)
