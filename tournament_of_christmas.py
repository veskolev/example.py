days = int(input())
total_cost = 0
total_cost_day = 0
count_game = 0
win_game = 0
for n in range(0, days-1):
    sport = input()
    win_lose = input()
    while sport != 'Finish':
        if win_lose == 'win':
            total_cost_day += 20
            win_game += 1
        count_game += 1
        sport = input ()
        win_lose = input()
        if count_game//2 > win_game:
            total_cost = total_cost_day * 1.1
        else:
            total_cost = total_cost_day
print(total_cost)
