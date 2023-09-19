budget = float(input())
category = input()
number_of_people_in_group = int(input())
pecent_per_budget_from_transport = 0
transportation_costs = 0
tiket_costs = 0
total_cost = 0
difference = 0
if 1 <= number_of_people_in_group <= 4:
    pecent_per_budget_from_transport = 0.75
elif 5 <= number_of_people_in_group <= 9:
    pecent_per_budget_from_transport = 0.60
elif 10 <= number_of_people_in_group <= 24:
    pecent_per_budget_from_transport = 0.50
elif 25 <= number_of_people_in_group <= 49:
    pecent_per_budget_from_transport = 0.40
elif 50 <= number_of_people_in_group:
    pecent_per_budget_from_transport = 0.25
transportation_costs = budget * pecent_per_budget_from_transport
if category == 'VIP':
    tiket_costs = number_of_people_in_group * 499.99
elif category == 'Normal':
    tiket_costs = number_of_people_in_group * 249.99
total_cost = transportation_costs + tiket_costs
if budget > total_cost:
    difference = budget - total_cost
    print(f'Yes! You have {difference:.2f} leva left.')
elif total_cost > budget:
    difference = total_cost - budget
    print(f'Not enough money! You need {difference:.2f} leva.')
