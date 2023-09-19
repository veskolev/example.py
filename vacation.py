bufget = float(input())
season = input()
accommodation = ''
sum_vacanion = 0
location = ''
if bufget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        sum_vacanion = bufget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        sum_vacanion = bufget * 0.45
elif 1000 < bufget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        sum_vacanion = bufget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        sum_vacanion = bufget * 0.60
elif bufget > 3000:
    accommodation = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        sum_vacanion = bufget * 0.90
    elif season == 'Winter':
        location = 'Morocco'
        sum_vacanion = bufget * 0.90
print(f'{location} - {accommodation} - {sum_vacanion:.2f}')
