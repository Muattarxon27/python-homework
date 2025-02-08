def tekshirish(foydalanuvchi_nomi, parol):
    if not foydalanuvchi_nomi:
        print("Foydalanuvchi nomi bo'sh bo'lishi mumkin emas.")
        return
    if not parol:
        print("Parol bo'sh bo'lishi mumkin emas.")
        return
    print("Kirish muvaffaqiyatli!")

# Foydalanuvchi ma'lumotlarini olish
foydalanuvchi_nomi = input("Foydalanuvchi nomini kiriting: ")
parol = input("Parolni kiriting: ")

# Ma'lumotlarni tekshirish
tekshirish(foydalanuvchi_nomi, parol)