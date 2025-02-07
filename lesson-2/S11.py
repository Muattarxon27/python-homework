s=input("matnni kiriting")
contains_digit=any(char.isdigit()for char in s)
if contains_digit:
    print("Matnda raqam mavjud.")
else:
    print("Matnda hech qanday raqam yo'q.")
    