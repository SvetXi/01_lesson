from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S23", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79361234567"),
    Smartphone("Huawei", "P50 Pro", "+79461234567"),
    Smartphone("OnePlus", "10 Pro", "+79561234567"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
