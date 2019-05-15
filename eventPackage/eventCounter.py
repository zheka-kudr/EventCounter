def event(number_of_guests, number_of_vegans, number_of_vegetarians, number_of_kids, number_of_alco_drinkers):
    global meat, salad, cake, candy, alco
    if number_of_guests < 0:
        exit("Negative num")

    if number_of_vegans < 0:
        exit("Negative num")

    if number_of_vegetarians < 0:
        exit("Negative num")

    if number_of_kids < 0:
        exit("Negative num")

    if number_of_alco_drinkers > number_of_guests - number_of_kids:
        exit("Incorrect number")

    if number_of_vegetarians + number_of_vegans + number_of_kids < number_of_guests:
        meat_eaters = number_of_guests - (number_of_vegetarians + number_of_vegans)
        meat = meat_eaters * 0.4 + number_of_kids * 0.2
        salad = (meat_eaters / 2) * 0.5 + (number_of_vegans * 2) * 0.5 + (
                number_of_vegetarians * 1.5) * 0.5 + number_of_kids * 0.3
        cake = (number_of_guests - number_of_kids) * 0.2 + number_of_kids * 0.3
        candy = number_of_kids * 20 + (number_of_guests - number_of_kids) * 5
        alco = number_of_alco_drinkers * 0.5
        return print("%.1f kg of Meat\n%.1f kg of Salad\n%.1f kg of Cake\n%.0f Candys\n%0.1f l of Vodka" % (
            meat, salad, cake, candy, alco))


# "%.1f kg of Meat\n%.1f kg of Salad\n%.1f kg of Cake\n%.0f Candys\n%0.1f l of Vodka" %
def return_meat():
    return meat


def return_salad():
    return salad


def return_cake():
    return cake


def return_candys():
    return candy


def return_alco():
    return alco


def return_all():
    return meat, salad, cake, candy, alco
