# Sonning 3 va 5 ga bo‘linishini tekshirish
def bolinuvchanlik_tekshirish(son):
    if son % 3 == 0 and son % 5 == 0:
        print("Berilgan son 3 va 5 ga bo‘linadi.")
    else:
        print("Berilgan son 3 va 5 ga bo‘linmaydi.")

# Foydalanuvchidan son kiritishni so‘rash
son = int(input("Son kiriting: "))
bolinuvchanlik_tekshirish(son)
