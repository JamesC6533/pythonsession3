def rental_car_cost(days):

    daily_cost = 40
    total_cost = days * daily_cost

    if days >= 7:
        total_cost -= 50
    elif days >= 3:
        total_cost -= 20

    return total_cost




