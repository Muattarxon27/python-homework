def son_tekshirish(son):
    if son > 0 and son % 2 == 0:
        print("Berilgan son musbat va juft.")
    else:
        print("Berilgan son musbat juft emas yoki manfiy.")

# Foydalanuvchidan son kiritishni so'rash
son = int(input("Son kiriting: "))
son_tekshirish(son)
