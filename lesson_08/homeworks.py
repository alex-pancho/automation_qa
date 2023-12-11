def longest_word(words: list) -> str:
    """
    This function prints as result of the longest string in list.
    :param words: list of strings
    :return longer word in list
    """

    if not isinstance(words, list):
        raise TypeError("The type must be a list!")
    result = max(words, key=len)
    return result


def exclude(obj, excl: str) -> list:
    """
    This function can exclude item from list/set/tuple/dict and return result.
    Your original variable won't be changed.
    :param obj: list/set/tuple/dict
    :param excl: str
    :return: Your variable (list) without excluding item
    """

    if isinstance(obj, int or str or float):
        raise TypeError("The type of obj must be list, dict, tuple or set!")
    if not isinstance(excl, str):
        raise TypeError("The type of excluding item must be str!")

    res = [item for item in obj if item != excl]
    return res


def distance_costs(dist: int, capacity: int, flow_100: int) -> str:
    """
    This function can calculate how much litters of gasoline you need for trip and how many times should refuel.
    :param dist: int (km)
    :param capacity: int (litter)
    :param flow_100: int (litter)
    :return result(str) with a message
    """

    if not all(isinstance(arg, int) for arg in (dist, capacity, flow_100)):
        raise TypeError("The type of each param must be int!")

    total_gas = int(dist / 100 * flow_100)
    refuel = int(total_gas / capacity)

    if total_gas < 1:
        result = (f"The trip of {dist} is very short, so you should refuel only one time before the trip, because you "
                  f"need less than 1 litter of gasoline.")
        return result
    if refuel < 1:
        result = (f"The trip of {dist} is very short, so you should refuel only one time before the trip, because you "
                  f"need only {total_gas} litters of gasoline.")
        return result

    result = (f"The trip of {dist} km will require {total_gas} liters of gasoline, "
              f"so you will have to refuel at least {refuel} times.")
    return result


def multiplication_table(number: int) -> str:
    """
    This function prints the multiplication table of a given digit up to 25.
    :param number: positive value int
    :return: multiplication table
    """

    if not isinstance(number, int):
        raise TypeError("The number must be int!")

    if number <= 0:
        raise ValueError("The number must be positive and greater than 0.")

    result_table = ''
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        result_table += f"{number}x{multiplier}={result}\n"
        multiplier += 1
    return result_table