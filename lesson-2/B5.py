def matn_uzunlik_tekshirish(matn1, matn2):
    if len(matn1) == len(matn2):
        print("Berilgan ikkita matn uzunligi teng.")
    else:
        print("Berilgan ikkita matn uzunligi har xil.")

# Foydalanuvchidan ikkita matn kiritishni so'rash
matn1 = input("Birinchi matnni kiriting: ")
matn2 = input("Ikkinchi matnni kiriting: ")
matn_uzunlik_tekshirish(matn1, matn2)
