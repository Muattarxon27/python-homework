def uchta_son_tekshirish(son1, son2, son3):
    if son1 != son2 and son1 != son3 and son2 != son3:
        print("Barcha uchta son bir-biridan farq qiladi.")
    else:
        print("Ba'zi sonlar bir-biriga teng.")

# Foydalanuvchidan uchta son kiritishni so'rash
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))
uchta_son_tekshirish(son1, son2, son3)
