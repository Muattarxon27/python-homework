# Matndan avtomobil nomlarini topish
def extract_car_names(txt):
    car_brands = ["Maserati", "BMW", "Audi", "Toyota", "Tesla", "Ford", "Honda"]
    from itertools import permutations
    possible_words = {''.join(p) for p in permutations(txt)}
    found_brands = [brand for brand in car_brands if brand in possible_words]
    return found_brands

# Foydalanuvchidan matn kiritishni so‘rash
txt = input("Matnni kiriting: ")
cars = extract_car_names(txt)
print("Topilgan avtomobil brendlari:", cars)
