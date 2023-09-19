bufget = float(input())
season = input()
class_car = ''
rent_car = 0
type_car = ''
if bufget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        type_car = 'Cabrio'
        rent_car = bufget * 0.35
    elif season == 'Winter':
        type_car = 'Jeep'
        rent_car = bufget * 0.65
elif 100 < bufget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        type_car = 'Cabrio'
        rent_car = bufget * 0.45
    elif season == 'Winter':
        type_car = 'Jeep'
        rent_car = bufget * 0.80
elif bufget > 500:
    class_car = 'Luxury class'
    type_car = 'Jeep'
    rent_car = bufget * 0.90

print(class_car)
print(f'{type_car} - {rent_car:.2f}')
