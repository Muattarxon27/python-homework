s=input("Biror matnni kiriting").lower()
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
vowel_count=0
consonant_count=0
for char in s:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
        print("unli harflar soni: ", vowel_count)
        print("undosh harflar soni:", consonant_count)

