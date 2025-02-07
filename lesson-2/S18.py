text=input("Matnni kiriting: ")
start_word=input("Qaysi so'z bilan boshlanishini tekshiramiz ")
end_world=input("Qaysi so'z bilan tugashini tekshiramiz ")
if text.startswith(start_word) and text.endswith(end_word):
    print("Matn aynan shu so'z bilan boshlanadi va tugaydi!")
else:
    print("Matn bu so'z bilan boshlanmaydi va tugamaydi.")
    