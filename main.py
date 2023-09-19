import math
while True:
    try:
        diameter = float(input("Введіть діаметер кола:"))
        break
    except ValueError as e:
        print("Введіть правиельний формат діаметру")

choice = input("оберіть 'площа' або 'перемитер'(ведіть '1' або '2'):")
if choice == '1':
    radius = diameter / 2
    area = math.pi * (radius **2 )
    print(f"лоща кола з діаметром {diameter} дорівнює {area:.2f} квадратних довжини.")
elif choice == '2':
    circumrefernce = math.pi * diameter
    print(f"лоща кола з діаметром {diameter} дорівнює {circumrefernce:.2f} одиниць довжини.")
else:
    print("Неправельний вибір. будь ласка, введіть 'площа' або 'периметр'")
