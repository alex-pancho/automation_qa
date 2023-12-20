def calculate_bananas(apples):
    if apples < 0:
        raise ValueError
    banana = apples * 4
    return banana


def calculate_total_trees(apple_tree):
    pearl_tree = apple_tree + 5
    plump_tree = apple_tree - 2
    total_trees = apple_tree + pearl_tree + plump_tree
    return total_trees


def calculate_temperatures(morning_temperature):
    day_temperature = morning_temperature - 10
    evening_temperature = day_temperature + 4
    return morning_temperature, day_temperature, evening_temperature


def calculate_total_cost_books(cost_book_1):
    cost_book_2 = cost_book_1 + 2
    cost_book_3 = (cost_book_1 + cost_book_2) / 2
    total_cost_books = cost_book_1 + cost_book_2 + cost_book_3
    return total_cost_books


