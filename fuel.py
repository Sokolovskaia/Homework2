def fuel(fuel_flow, remaining_fuel):
    """
    >>> fuel(15, 45)
    300
    """
    return int(remaining_fuel / fuel_flow * 100)


print("Оставшегося топлива Вам хватит примерно на", fuel(15, 45), "км")

