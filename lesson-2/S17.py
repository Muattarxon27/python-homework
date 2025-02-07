text=input("Matnni kiriting: ")
symbol=input("Almashtirish belgisini kiriting: ")
vowels="aeiouAEIOU"
new_text="".join(symbol if char in vowels else char for char in text)
print("Natija: ", new_text)
