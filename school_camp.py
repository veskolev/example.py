season = input()
type_group = input()
number_students = int(input())
number_nights = int(input())
coast_students = 0
total_coast = 0
type_sport = ''
if season == 'Winter':
    if type_group == 'boys' or type_group == 'girls':
        coast_students = 9.6
    elif type_group == 'mixed':
        coast_students = 10
elif season == 'Spring':
    if type_group == 'boys' or type_group == 'girls':
        coast_students = 7.2
    elif type_group == 'mixed':
        coast_students = 9.5
elif season == 'Summer':
    if type_group == 'boys' or type_group == 'girls':
        coast_students = 15
    elif type_group == 'mixed':
        coast_students = 20
total_coast = number_students * number_nights * coast_students
if 10 <= number_students < 20:
    total_coast = total_coast * 0.95
elif 20 <= number_students < 50:
    total_coast = total_coast * 0.85
elif 50 <= number_students:
    total_coast = total_coast * 0.50
if season == 'Winter':
    if type_group == 'boys':
        type_sport = 'Judo'
    elif type_group == 'girls':
        type_sport = 'Gymnastics'
    elif type_group == 'mixed':
        type_sport = 'Ski'
elif season == 'Spring':
    if type_group == 'boys':
        type_sport = 'Tennis'
    elif type_group == 'girls':
        type_sport = 'Athletics'
    elif type_group == 'mixed':
        type_sport = 'Cycling'
elif season == 'Summer':
    if type_group == 'boys':
        type_sport = 'Football'
    elif type_group == 'girls':
        type_sport = 'Volleyball'
    elif type_group == 'mixed':
        type_sport = 'Swimming'
print(f'{type_sport} {total_coast:.2f} lv.')
