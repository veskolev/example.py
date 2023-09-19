numbers_juinior_bikers = int(input())
numbers_senior_bikers = int(input())
type_trail = input()
total_sum = 0
expenses = 0
difference = 0
if type_trail == 'trail':
    total_sum = numbers_juinior_bikers * 5.5 + numbers_senior_bikers * 7
elif type_trail == 'cross-country':
    total_sum = numbers_juinior_bikers * 8 + numbers_senior_bikers * 9.5
    if 50 <= numbers_juinior_bikers + numbers_senior_bikers:
        total_sum = total_sum * 0.75
elif type_trail == 'downhill':
    total_sum = numbers_juinior_bikers * 12.25 + numbers_senior_bikers * 13.75
elif type_trail == 'road':
    total_sum = numbers_juinior_bikers * 20 + numbers_senior_bikers * 21.5
expenses = total_sum * 0.05
difference = total_sum - expenses
print(f'{difference:.2f}')
