text=input("Matnni kiriting: ")
char_to_remove=input("Olib tashlanadigan belgini kiriting: ")
char_to_remove=char_to_remove[0]
new_text=text.replace(char_to_remove, "")
print("Natijani: ", new_text)