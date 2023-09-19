season = input()
km_season = float(input())
coast_km = 0
total_coast = 0
if km_season <= 5000:
    if season == 'Spring' or season == 'Autumn':
        coast_km = 0.75
    elif season == 'Summer':
        coast_km = 0.90
    elif season == 'Winter':
        coast_km = 1.05
elif 5000 < km_season <= 10000:
    if season == 'Spring' or season == 'Autumn':
        coast_km = 0.95
    elif season == 'Summer':
        coast_km = 1.1
    elif season == 'Winter':
        coast_km = 1.25
elif 10000 < km_season <= 20000:
    coast_km = 1.45
total_coast = km_season * coast_km * 0.90 * 4
print(f'{total_coast:.2f}')
