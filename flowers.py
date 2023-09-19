number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
day_is_holiday = input()

price_chrysanthemums = 2
price_roses = 4.1
price_tulips = 2.5
total_sum = 0
total_number = number_of_tulips + number_of_roses + number_of_chrysanthemums
if season == 'Spring' or season == 'Summer':
    total_sum = number_of_chrysanthemums * price_chrysanthemums\
                + number_of_roses * price_roses\
                + number_of_tulips * price_tulips
elif season == 'Autumn' or season == 'Winter':
    price_chrysanthemums = 3.75
    price_roses = 4.5
    price_tulips = 4.15
    total_sum = number_of_chrysanthemums * price_chrysanthemums\
                + number_of_roses * price_roses\
                + number_of_tulips * price_tulips
if day_is_holiday == 'Y':
    total_sum = total_sum * 1.15
if number_of_tulips > 7 and season == 'Spring':
    total_sum = total_sum * 0.95
elif number_of_roses >= 10 and season == 'Winter':
    total_sum = total_sum * 0.90
if total_number > 20:
    total_sum = total_sum * 0.80
total_sum = total_sum + 2
print(f'{total_sum:.2f}')



